from django.db import models
from .utilities import CommonModel
import uuid

ORDER_STATUS_CHOICES = [("PENDING", "PENDING"), ("COMPLETED", "COMPLETED"), ("CANCELED", "CANCELED")]

class Vendor(CommonModel):
    '''
        Vendor model to store details related to vendor
    '''
    vendor_code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    contact_details = models.TextField()
    address = models.TextField()
    on_time_delivery_rate = models.FloatField(null = True, blank = True)
    quality_rating_avg = models.FloatField(null = True, blank = True)
    average_response_time = models.TimeField(null = True, blank = True)
    fulfillment_rate = models.FloatField(null = True, blank = True)

    class Meta:
        db_table = "vendor"
        ordering = ["-created_at"]



class PurchaseOrder(CommonModel):
    '''
        Purchase Order model to store order of each vendor
    '''
    po_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor_id = models.ForeignKey(Vendor, db_column = "vendor_id", on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    expected_delivery_date = models.DateTimeField(null = True, blank = True)
    actual_delivery_date = models.DateTimeField(null = True, blank = True)
    items = models.JSONField()
    quantity = models.IntegerField(default = 1)
    status = models.CharField(max_length = 30, choices = ORDER_STATUS_CHOICES, default = "PENDING")
    quality_rating = models.FloatField(null = True, blank = True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null = True, blank = True)
    response_time = models.DecimalField(null = True, blank = True, max_digits = 50, decimal_places=5)
    quality_rating = models.IntegerField(null = True, blank = True)

    class Meta:
        db_table = "purchase_order"
        ordering = ["-created_at"]



class VendorPerformanceHistory(CommonModel):
    '''
        Model to store the data for vendor performance history
    '''
    id = models.AutoField(primary_key=True)
    vendor_id = models.ForeignKey(Vendor, db_column = "vendor_id", on_delete = models.CASCADE)
    performance_date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.TimeField()
    fulfillment_rate = models.FloatField()

    class Meta:
        db_table = "vendor_performance_history"
        ordering = ["-created_at"]

