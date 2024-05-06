from rest_framework import serializers
from .models import Vendor, PurchaseOrder, VendorPerformanceHistory
from .constants import ResponseConstant
import re


class VendorSerializer(serializers.ModelSerializer):
    '''
        serializer for vendor create model
    '''
    class Meta:
        model = Vendor
        fields = ["vendor_code", "name", "contact_details", "address"]
    
    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError(ResponseConstant.NAME_FIELD_NOT_PROVIDED)
        
        name_pattern = r'^[a-zA-Z\s]+$'
        if not re.match(name_pattern, value):
            raise serializers.ValidationError(ResponseConstant.NAME_IS_INVALID)
        return value


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        response_body = {
            "vendor_id": representation["vendor_code"],
            "name": representation["name"]
        }

        return response_body
    


class VendorByIdSerializer(serializers.ModelSerializer):
    '''
        Get list of all vendors
    '''
    class Meta:
        model = Vendor
        fields = "__all__"

    
class PurchaseOrderSerializer(serializers.ModelSerializer):
    '''
        Serializer to perform operation on purchase order model
    ''' 
    class Meta:
        model = PurchaseOrder
        fields = ["po_number", "vendor_id", "order_date", "items", "quantity", "issue_date"]



class PurchaseOrderByIdSerializer(serializers.ModelSerializer):
    '''
        Purchase order by ID serializer
    '''
    class Meta:
        model = PurchaseOrder
        fields = "__all__"


class PurchaseOrderEditSerializer(serializers.ModelSerializer):
    '''
        Purchase order edit to serializer
    '''
    class Meta:
        model = PurchaseOrder
        fields = ["items", "quantity"]


class VendorPerformanceHistorySerializer(serializers.ModelSerializer):
    '''
        Vendor performance history serializer
    '''
    class Meta:
        model = VendorPerformanceHistory
        fields = "__all__"






