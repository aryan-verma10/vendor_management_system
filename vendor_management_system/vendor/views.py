from django.shortcuts import render
from rest_framework import status
from vendor_management_system.global_variables import generic_json_response
from .constants import ResponseConstant
from vendor.models import (Vendor, PurchaseOrder, VendorPerformanceHistory)
from .serializers import (VendorSerializer, VendorByIdSerializer,
                          PurchaseOrderSerializer, PurchaseOrderByIdSerializer,
                          PurchaseOrderEditSerializer, VendorPerformanceHistorySerializer)
from rest_framework.views import APIView
from datetime import datetime, timedelta
from django.db.models import Q
from django.utils import timezone
# Create your views here.


class VendorApi(APIView):
    '''
        API collection to implement operations on Vendor model
    '''
    def post(self, request):
        '''
            POST api to add new vendor
        '''
        try:
            request_body = request.data
            if not request_body:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_400_BAD_REQUEST,
                                             message = ResponseConstant.REQUEST_BODY_NOT_PROVIDED)
            
            
            serializer = VendorSerializer(data = request_body)
            
            # if all validations passed
            if serializer.is_valid():
                serializer.save()
                return generic_json_response(success = True,
                                             status_code = status.HTTP_200_OK,
                                             message = ResponseConstant.NEW_VENDOR_CREATED_SUCCESSFULLY)
            
            # if any validation do not pass
            else:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_400_BAD_REQUEST,
                                             message = ResponseConstant.VALIDATION_ERROR,
                                             error = str(serializer.errors))

        except Exception as err:
            return generic_json_response(success = False,
                                         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                                         message = ResponseConstant.SOMETHING_WENT_WRONG,
                                         error = str(err))
        

    def get(self, request):
        '''
            Get api to get all the vendor lists
        '''
        try:
            # getting all the list object of vendors
            vendor_objs = Vendor.objects.all()
            serializer = VendorSerializer(instance = vendor_objs, many = True)

            return generic_json_response(success = True,
                                         status_code = status.HTTP_200_OK,
                                         message = ResponseConstant.VENDORS_LIST_FETCHED_SUCCESSFULLY,
                                         result = serializer.data)                                                                                                                                                                                                                               
        except Exception as err:
            return generic_json_response(success = False,
                                         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                                         message = ResponseConstant.SOMETHING_WENT_WRONG,
                                         error = str(err))
        

    

class VendorByIdApi(APIView):
    '''
        API collection to get and update the vendor on basis of ID
    '''
    def get(self, request, vendor_id):
        try:
            # finding the vendor using id
            vendor_obj = Vendor.objects.filter(pk = vendor_id).first()
            if not vendor_obj:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_404_NOT_FOUND,
                                             message = ResponseConstant.VENDOR_NOT_FOUND)
            

            serializer = VendorByIdSerializer(vendor_obj)
            return generic_json_response(success = True,
                                         status_code = status.HTTP_200_OK,
                                         message = ResponseConstant.VENDOR_DATA_FETCHED_SUCCESSFULLY,
                                         result = serializer.data)

        except Exception as err:
            return generic_json_response(success = False,
                                         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                                         message = ResponseConstant.SOMETHING_WENT_WRONG,
                                         error = str(err))
        


    def put(self, request, vendor_id):
        try:
            request_body = request.data

            if not request_body:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_400_BAD_REQUEST,
                                             message = ResponseConstant.REQUEST_BODY_NOT_PROVIDED)

            # finding the vendor on the basis of vendor_id
            vendor_obj = Vendor.objects.filter(pk = vendor_id).first()
            if not vendor_obj:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_404_NOT_FOUND,
                                             message = ResponseConstant.VENDOR_NOT_FOUND)
            
            serializer = VendorSerializer(instance = vendor_obj, data = request_body, partial = True)
            if serializer.is_valid():
                serializer.save()
                return generic_json_response(success = True,
                                             status_code = status.HTTP_200_OK,
                                             message = ResponseConstant.VENDOR_DETAILS_UPDATED_SUCCESSFULLY)
            
            else:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_400_BAD_REQUEST,
                                             message = ResponseConstant.VALIDATION_ERROR,
                                             error = str(serializer.errors))
        
        except Exception as err:
            return generic_json_response(success = False,
                                         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                                         message = ResponseConstant.SOMETHING_WENT_WRONG,
                                         error = str(err))


    def delete(self, request, vendor_id):
        '''
            Delete api to delete a particular vendor
        '''
        try:
            vendor_obj = Vendor.objects.filter(pk = vendor_id).first()
            if not vendor_obj:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_404_NOT_FOUND,
                                             message = ResponseConstant.VENDOR_NOT_FOUND)

            # deleting vendor from the database
            vendor_obj.delete()

            return generic_json_response(success = True,
                                         status_code = status.HTTP_200_OK,
                                         message = ResponseConstant.VENDOR_DELETED_SUCCESSFULLY)
        
        except Exception as err:
            return generic_json_response(success = False,
                                         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                                         message = ResponseConstant.SOMETHING_WENT_WRONG,
                                         error = str(err))
        



class PurchaseOrderApi(APIView):
    '''
        API collection to perform actions on Purchase order model
    '''
    def post(self, request): 
        '''
            POST api to add new purchase order
        '''
        try:
            request_body = request.data
            if not request_body:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_400_BAD_REQUEST,
                                             message = ResponseConstant.REQUEST_BODY_NOT_PROVIDED)
            
            
            # timestamp on which the order is issued to vendor is current timestamp  
            request_body["issue_date"] = timezone.now()

            
            serializer = PurchaseOrderSerializer(data = request_body)
            if serializer.is_valid():
                serializer.save()
                return generic_json_response(success = True,
                                             status_code = status.HTTP_200_OK,
                                             message = ResponseConstant.PURCHASE_ORDER_CREATED_SUCCESSFULLY)
            
            else:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_400_BAD_REQUEST,
                                             message = ResponseConstant.VALIDATION_ERROR,
                                             error = str(serializer.errors))

        except Exception as err:
            print("error->", err)
            return generic_json_response(success = False,
                                             status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                                             message = ResponseConstant.SOMETHING_WENT_WRONG,
                                             error = str(err))
        

    def get(self, request):
        '''
            Get api to view all purchase orders with filter on
            [vendor name and vendor_id]
        '''
        try:
            vendor_search = request.query_params.get("vendor_search", None)

            # if vendor search is given
            purchase_order_objs = None
            if vendor_search:
                purchase_order_objs = PurchaseOrder.objects.filter(Q(vendor_id__icontains = vendor_search)| Q(vendor_id__name__icontains = vendor_search))
            
            else:
                purchase_order_objs = PurchaseOrder.objects.all()

            serializer = PurchaseOrderSerializer(purchase_order_objs, many = True)
            return generic_json_response(success = True,
                                         status_code = status.HTTP_200_OK,
                                         message = ResponseConstant.PURCHASE_ORDERS_LIST_FETCHED_SUCCESSFULLY,
                                         result = serializer.data)

        except Exception as err:
            return generic_json_response(success = False,
                                             status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                                             message = ResponseConstant.SOMETHING_WENT_WRONG,
                                             error = str(err))
        

class PurchaseOrderByIdApi(APIView):
    '''
        API collection to implement action on purchase order table
        by ID
    '''
    def get(self, request, po_id):
        '''
            GET api to get the purchase order data by ID
        '''
        try:
            purchase_order_obj = PurchaseOrder.objects.filter(pk = po_id).first()
            if not purchase_order_obj:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_404_NOT_FOUND,
                                             message = ResponseConstant.PURCHASE_ORDER_ID_NOT_FOUND)
            
            
            serializer = PurchaseOrderByIdSerializer(purchase_order_obj)
            return generic_json_response(success = True,
                                         status_code = status.HTTP_200_OK,
                                         message = ResponseConstant.PURCHASE_ORDER_DETAIL_FETCHED_SUCCESSFULLY,
                                         result = serializer.data)
            
        except Exception as err:
            return generic_json_response(success = False,
                                         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                                         message = ResponseConstant.SOMETHING_WENT_WRONG,
                                         error = str(err))
        
    
    def put(self, request, po_id):
        '''
            PUT api to update the 
        '''
        try:
            request_body = request.data

            if not request_body:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_400_BAD_REQUEST,
                                             message = ResponseConstant.REQUEST_BODY_NOT_PROVIDED)

            purchase_order_obj = PurchaseOrder.objects.filter(pk = po_id).first()
            if not purchase_order_obj:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_404_NOT_FOUND,
                                             message = ResponseConstant.PURCHASE_ORDER_ID_NOT_FOUND)
            
            serializer = PurchaseOrderEditSerializer(data = request_body, instance = purchase_order_obj, partial = True)
            if serializer.is_valid():
                return generic_json_response(success = True,
                                             status_code = status.HTTP_200_OK,
                                             message = ResponseConstant.PURCHASE_ORDER_UPDATED_SUCCESSFULLY)
            
            else:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_400_BAD_REQUEST,
                                             message = ResponseConstant.VALIDATION_ERROR,
                                             error = str(serializer.errors))

                        
        except Exception as err:
            return generic_json_response(success = False,
                                         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                                         message = ResponseConstant.SOMETHING_WENT_WRONG,
                                         error = str(err))
        

    def delete(self, request, po_id):
        '''
            Delete api to delete the purchase order
        '''
        try:
            purchase_order_obj = PurchaseOrder.objects.filter(pk = po_id).first()
            if not purchase_order_obj:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_404_NOT_FOUND,
                                             message = ResponseConstant.PURCHASE_ORDER_NOT_FOUND)
            
            # deleting the purchase order
            purchase_order_obj.delete()
            return generic_json_response(success = True,
                                         status_code = status.HTTP_200_OK,
                                         message = ResponseConstant.PURCHASE_ORDER_DELETED_SUCCESSFULLY)


        except Exception as err:
            return generic_json_response(success = False,
                                         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                                         message = ResponseConstant.SOMETHING_WENT_WRONG,
                                         error = str(err))
        


class VendorPerformanceHistoryApi(APIView):
    '''
        API collection to get the vendor performance history by 
        vendor_id
    '''
    def get(self, request, vendor_id):
        try:
            vendor_performance_history_objs = VendorPerformanceHistory.objects.filter(vendor_id = vendor_id)
            if not vendor_performance_history_objs:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_404_NOT_FOUND,
                                             message = ResponseConstant.NO_PERFORMANCE_HISTORY_OF_VENDOR_FOUND)

            serializer = VendorPerformanceHistorySerializer(vendor_performance_history_objs, many = True)

            return generic_json_response(success = True,
                                         status_code = status.HTTP_200_OK,
                                         message = ResponseConstant.PERFORMANCE_HISTORY_DATA_FETCHED_SUCCESSFULLY,
                                         result = serializer.data)
              
        except Exception as err:
            return generic_json_response(success = False,
                                         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                                         message = ResponseConstant.SOMETHING_WENT_WRONG,
                                         error = str(err))
        

class PurchaseOrderAcknowledgementApi(APIView):
    '''
        API collection to acknowledge that the order is completed or failed.
    '''
    def post(self, request, po_id):
        '''
            POST api to acknowledge or accept the order by vendor
        '''
        try:
            current_timestamp = timezone.now()
            purchase_order_obj = PurchaseOrder.objects.filter(pk = po_id).first()
            if not purchase_order_obj:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_404_NOT_FOUND,
                                             message = ResponseConstant.PURCHASE_ORDER_NOT_FOUND)
            
            # issue date of the order
            issue_datetime = purchase_order_obj.issue_date
            purchase_order_obj.acknowledgment_date = current_timestamp
            # once the order is acknowledged expected delivery date is 3 days after the 
            # order is accepted by the vendor
            purchase_order_obj.expected_delivery_date = current_timestamp + timedelta(days = 3)
            purchase_order_obj.response_time = current_timestamp.timestamp() - issue_datetime.timestamp()
            
            
            # Save only the fields that were updated
            purchase_order_obj.save(update_fields=['acknowledgment_date', 'expected_delivery_date', 'response_time'])
            
            return generic_json_response(success = True,
                                         status_code = status.HTTP_200_OK,
                                         message = ResponseConstant.PURCHASE_ORDER_ACKNOWLEDGED_BY_VENDOR_SUCCESSFULLY)

        except Exception as err:
            return generic_json_response(success = False,
                                         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                                         message = ResponseConstant.SOMETHING_WENT_WRONG,
                                         error = str(err))

    

class PurchaseOrderCompleteStatusApi(APIView):
    '''
        Api collection purchase order complete status 
    '''
    COMPLETED = "COMPLETED"
    CANCELED = "CANCELED"

    def put(self, request, po_id, po_status):
        '''
            Post api to change the status for the order
        '''
        try:
            quality_rating = request.query_params.get("quality_rating", None)

            purchase_order_obj = PurchaseOrder.objects.filter(pk = po_id).first()
            if not purchase_order_obj:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_404_NOT_FOUND,
                                             message = ResponseConstant.PURCHASE_ORDER_NOT_FOUND)
            
            if not po_status.upper() == self.COMPLETED \
               and not po_status.upper() == self.CANCELED:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_400_BAD_REQUEST,
                                             message = ResponseConstant.INVALID_PO_STATUS)
            
            if quality_rating<0 or quality_rating>10:
                # rating should be between 0 and 10
                return generic_json_response(success = False,
                                             status_code = status.HTTP_400_BAD_REQUEST,
                                             message = ResponseConstant.INVALID_QUALITY_RATING)
            

            if not purchase_order_obj.acknowledgment_date:
                return generic_json_response(success = False,
                                             status_code = status.HTTP_400_BAD_REQUEST,
                                             message = ResponseConstant.ORDER_IS_NOT_ACKNOWLEDGED_BY_VENDOR)
            
            # add the if the order is already completed or canceled
            purchase_order_obj.status = po_status.upper()

            if po_status.upper() == self.CANCELED:
                # order is canceled
                purchase_order_obj.save(update_fields=["status"])

            else:
                # order is completed
                purchase_order_obj.actual_delivery_date = timezone.now()
                purchase_order_obj.quality_rating = quality_rating
            
            purchase_order_obj.save(update_fields=['status', 'actual_delivery_date', 'quality_rating'])
            return generic_json_response(success = True,
                                         status_code = status.HTTP_200_OK,
                                         message = ResponseConstant.PURCHASE_ORDER_STATUS_CHANGED_SUCCESSFULLY)

        except Exception as err:
            return generic_json_response(success = False,
                                         status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                                         message = ResponseConstant.SOMETHING_WENT_WRONG,
                                         error = str(err))