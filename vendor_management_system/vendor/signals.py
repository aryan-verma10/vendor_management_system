from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (VendorPerformanceHistory, PurchaseOrder, Vendor)
from .utilities import converting_seconds_to_timefield_format
from .constants import VendorConstants
from django.db.models import F
from .serializers import VendorPerformanceHistorySerializer
from django.utils import timezone


def on_time_delivery_rate(vendor_id: str):
    '''
        Helper function to calculate the on_time delivery rate
    '''
    total_po_completed_objs = PurchaseOrder.objects.filter(vendor_id = vendor_id,\
                                                           status = VendorConstants.STATUS_COMPLETED)
    
    on_time_po_completed_count = total_po_completed_objs.filter(actual_delivery_date__lte = F('expected_delivery_date')).count()

    total_po_completed_count = len(total_po_completed_objs)

    vendor_obj = Vendor.objects.filter(vendor_code = vendor_id).first()
    if total_po_completed_objs == 0:
        on_time_delivery_rate_value = 0
        vendor_obj.on_time_delivery_rate = on_time_delivery_rate_value
    
    else:
        on_time_delivery_rate_value = float(on_time_po_completed_count)/float(total_po_completed_count)
        vendor_obj.on_time_delivery_rate = on_time_delivery_rate_value
    
    # updated the on_time_delivery_rate
    vendor_obj.save(update_fields=["on_time_delivery_rate"])
    return on_time_delivery_rate_value
    


def average_quality_rating_function(vendor_id: str):
    '''
        Helper function to calculate the average_quality_rating for 
        particular vendor
    '''
    quality_rating_list = list(PurchaseOrder.objects.filter(vendor_id = vendor_id, 
                                                            status = VendorConstants.STATUS_COMPLETED,
                                                            quality_rating__isnull = False).values_list("quality_rating", flat = True))
    
    sum_of_quality_rating = sum(quality_rating_list)

    average_quality_rating = float(sum_of_quality_rating)/float(len(quality_rating_list))
    vendor_obj = Vendor.objects.filter(vendor_code = vendor_id).first()
    vendor_obj.quality_rating_avg = average_quality_rating
    vendor_obj.save()

    # returning average_quality_rating
    return average_quality_rating


def fulfillment_rate_func(vendor_id: str):
    '''
        Helper function to calculate and update the fulfillment_rate for a
        particular vendor
    '''
    total_purchase_order_objs_count = PurchaseOrder.objects.filter(vendor_id = vendor_id).count()
    purchase_order_completed_count = PurchaseOrder.objects.filter(vendor_id = vendor_id, status = VendorConstants.STATUS_COMPLETED).count()

    fulfillment_rate = float(purchase_order_completed_count)/float(total_purchase_order_objs_count)
    
    vendor_obj = Vendor.objects.filter(vendor_code = vendor_id).first()
    vendor_obj.fulfillment_rate = fulfillment_rate
    vendor_obj.save()

    return fulfillment_rate



@receiver(post_save, sender = PurchaseOrder)
def average_response_time_update(sender, instance, update_fields, **kwargs):
    '''
        Signal function to update the average_response_time once
        acknowledgment for order is filled
    '''

    if update_fields and "acknowledgment_date" in update_fields:

        issue_date = instance.issue_date
        acknowledgment_date = instance.acknowledgment_date

        # current response_time
        current_response_time_in_seconds = acknowledgment_date.timestamp()-issue_date.timestamp()

        
        # finding the sum of previous_response_time for average
        vendor_id = instance.vendor_id.vendor_code
        response_time_list = list(PurchaseOrder.objects.filter(vendor_id = vendor_id, response_time__isnull = False).values_list("response_time", flat = True))
        iterators = len(response_time_list)+1
        
        total_sum_response_time = float(sum(td for td in response_time_list))+current_response_time_in_seconds
        
        # average_response_time_calculation
        average_response_time = float(total_sum_response_time)/float(iterators)
        
        vendor_code = instance.vendor_id.vendor_code
        vendor_obj = Vendor.objects.filter(pk = vendor_code).first()

        # average_response_time for vendor updated successfully
        converted_avg_response_time = converting_seconds_to_timefield_format(average_response_time)
        vendor_obj.average_response_time = converted_avg_response_time

        vendor_obj.save()
        


@receiver(post_save, sender = PurchaseOrder)
def po_metrics_after_completion(sender, instance, update_fields, **kwargs):
    '''
        Signal function to fill the metrics of order when
        purchase order is completed. 
    '''
    if update_fields and 'status' in update_fields:
        avg_on_time_delivery_rate_value = on_time_delivery_rate(instance.vendor_id.vendor_code)

        avg_quality_rating_value = average_quality_rating_function(instance.vendor_id.vendor_code)           

        fulfillment_rate = fulfillment_rate_func(instance.vendor_id.vendor_code)


        payload = {
            "vendor_id": instance.vendor_id.vendor_code,
            "performance_date": timezone.now(),
            "on_time_delivery_rate": avg_on_time_delivery_rate_value,
            "quality_rating_avg": avg_quality_rating_value,
            "average_response_time": instance.vendor_id.average_response_time,
            "fulfillment_rate": fulfillment_rate
        }
        serializer = VendorPerformanceHistorySerializer(data = payload)
        if serializer.is_valid():
            serializer.save()

        else:
            raise Exception(f"error->{serializer.errors}")


        










