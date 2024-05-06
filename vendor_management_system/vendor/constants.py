class ResponseConstant:
    '''
        class contains all response message constant
    '''
    SOMETHING_WENT_WRONG = "Something went wrong."
    REQUEST_BODY_NOT_PROVIDED = "Request body not provided."
    NEW_VENDOR_CREATED_SUCCESSFULLY = "New vendor created successfully."
    VALIDATION_ERROR = "Validation failed."
    NAME_FIELD_NOT_PROVIDED = "Name field not provided."
    NAME_IS_INVALID = "Name provided is invalid."
    VENDORS_LIST_FETCHED_SUCCESSFULLY = "Vendors list fetched successfully."
    VENDOR_NOT_FOUND = "Vendor not found."
    VENDOR_DATA_FETCHED_SUCCESSFULLY = "Vendor data fetched successfully."
    VENDOR_DETAILS_UPDATED_SUCCESSFULLY = "Vendor details updated successfully."
    VENDOR_DELETED_SUCCESSFULLY = "Vendor deleted successfully."
    PURCHASE_ORDER_CREATED_SUCCESSFULLY = "Purchase order created successfully."
    PURCHASE_ORDERS_LIST_FETCHED_SUCCESSFULLY = "Purchase orders list fetched successfully."
    PURCHASE_ORDER_ID_NOT_FOUND = "Purchase order id not found."
    PURCHASE_ORDER_DETAIL_FETCHED_SUCCESSFULLY = "Purchase order details fetched successfully."
    PURCHASE_ORDER_UPDATED_SUCCESSFULLY = "Purchase order updated successfully."
    PURCHASE_ORDER_NOT_FOUND = "Purchase order not found."
    PURCHASE_ORDER_DELETED_SUCCESSFULLY = "Purchase order deleted successfully."
    NO_PERFORMANCE_HISTORY_OF_VENDOR_FOUND = "No performance history of vendor found."
    PERFORMANCE_HISTORY_DATA_FETCHED_SUCCESSFULLY = "Performance history data fetched successfully."
    PURCHASE_ORDER_ACKNOWLEDGED_BY_VENDOR_SUCCESSFULLY = "Purchase order acknowledged by vendor successfully."
    INVALID_PO_STATUS = "Invalid po_status. Provide 'COMPLETED' or 'CANCELED'."
    PURCHASE_ORDER_STATUS_CHANGED_SUCCESSFULLY = "Purchase order status changed successfully."
    INVALID_QUALITY_RATING = "Quality rating should be between 0 and 10."
    ORDER_IS_NOT_ACKNOWLEDGED_BY_VENDOR = "Order is not acknowledged by the vendor."


class VendorConstants:
    '''
        Class contains all the constants used in vendor app
    '''
    STATUS_COMPLETED = 'COMPLETED'
    STATUS_PENDING = 'PENDING'
    STATUS_CANCELED = 'CANCELED'