from django.urls import path
from vendor.views import (VendorApi, VendorByIdApi,
                           PurchaseOrderApi, PurchaseOrderByIdApi,
                           VendorPerformanceHistoryApi, PurchaseOrderAcknowledgementApi,
                           PurchaseOrderCompleteStatusApi)

urlpatterns = [
    path("vendors/", VendorApi.as_view(), name = "vendor_collection_apis"),
    path("vendors/<str:vendor_id>/", VendorByIdApi.as_view(), name = "vendor_by_id_api"),
    path("purchase_orders/", PurchaseOrderApi.as_view(), name = "purchase_orders_api"),
    path("purchase_orders/<str:po_id>/", PurchaseOrderByIdApi.as_view(), name = "purchase_order_by_id_api"),
    path("vendors/<str:vendor_id>/performance/", VendorPerformanceHistoryApi.as_view(), name = "vendor_performance_history_api"),
    path("purchase_orders/<str:po_id>/acknowledge/", PurchaseOrderAcknowledgementApi.as_view(), name = "purchase_order_ack_api"),
    path('purchase_orders/<str:po_id>/po_status/<str:po_status>/', PurchaseOrderCompleteStatusApi.as_view(), name = "purchase_order_completed_status_api")
]