# Vendor Management System

## Overview
The Vendor Management System (VMS) provides a comprehensive solution for managing vendor relationships and performance tracking within an organization. It offers a suite of APIs to facilitate vendor onboarding, performance evaluation, and tracking. The system enables efficient management of vendor-related activities, including vendor registration, performance monitoring, and assessment.

This document describes the RESTful API endpoints provided by the Vendor Management System. The API allows interaction with vendor data, performance metrics, and tracking features.

## Installation and Setup

### 1. Clone the Repository
First clone this git repository in your local machine. Run below commands to clone the repository.
```bash
git clone https://github.com/aryan-verma10/vendor_management_system.git
cd vendor_management_system
```

### 2. Create and Activate a Virtual Environment (optional but recommended):
It's a good practice to create a virtual environment to manage your project dependencies independently of other Python projects on your system.

#### Create a Virtual Environment and activate it (on linux).
```bash
virtualenv venv
source venv/bin/activate
```
### 3. Install Required Libraries:
Now we need to install all the required libraries.
Ensure you have Python and pip installed on your system. Use pip to install the project dependencies listed in requirements.txt.
```python
pip install -r requirements.txt
```
### 4. Apply migrations:
As I have used sqlite3 as the database for the projects but you can use whichever database you like by changing the configurations of database in settings.py file.
After setting up the database we can run migration commands to make or connect us to the database and add the tables defined in our project.

 ```python
python manage.py makemigrations
python manage.py migrate
```
### 5. Start the Development Server:
Now the project is setup and we can start the development server. Run the below command on the terminal.
```python
python manage.py runserver
```
Server will be run on the localhost.(http://127.0.0.1:8000)

## Endpoints structure
Below are the endpoint structures to use which are present in this project.
### 1. Get All Vendors
- **Method**: `GET`
- **URL**: `/api/vendors/`
- **Description**: Fetches a list of all vendors.

#### Request

- No parameters required.

#### Response

- **Status Code**: 200 OK
- **Response Body**:
  ```json
  {
    "success": true,
    "status_code": 200,
    "message": "Vendors list fetched successfully.",
    "result": [
        {
            "vendor_id": "922419ed-64cb-4d5c-945b-36c290d36bb8",
            "name": "shivam dubey"
        },
        {
            "vendor_id": "0d24cd6a-2024-4595-8f26-a8b8907301de",
            "name": "aryan verma"
        }
    ],
    "error": {}}

### 2. Create Vendor
- **Method**: `POST`
- **URL**: `/api/vendors/`
- **Description**: Create a new vendor.

#### Request

- **Request body**
```json
{
    "name": "john",
    "contact_details": "john@gmail.com",
    "address": "cv street, LA"
}
```

#### Response

- **Status Code**: 200 OK
- **Response Body**:
  ```json
  {
    "success": true,
    "status_code": 200,
    "message": "New vendor created successfully.",
    "result": {},
    "error": {}}

### 3. Get Vendor Details by vendor-id
- **Method**: `GET`
- **URL**: `/api/vendors/{vendor_code}/`
- **Description**: Get vendor complete detail.

#### Request

- fill the above vendor_code with uuid of the vendor (example- `/api/vendors/922419ed-64cb-4d5c-945b-36c290d36bb8/`)

#### Response

- **Status Code**: 200 OK
- **Response Body**:
  ```json
  {
    "success": true,
    "status_code": 200,
    "message": "Vendor data fetched successfully.",
    "result": {
        "vendor_code": "922419ed-64cb-4d5c-945b-36c290d36bb8",
        "created_at": "2024-05-04T15:57:38.752871Z",
        "updated_at": "2024-05-05T11:18:02.073261Z",
        "deleted_at": null,
        "name": "suraj dubey",
        "contact_details": "dpsaks11036@gmail.com",
        "address": "hello world",
        "on_time_delivery_rate": 1.0,
        "quality_rating_avg": 4.0,
        "average_response_time": "00:09:42",
        "fulfillment_rate": 0.4444444444444444
    },
    "error": {}
  }
  ```

### 4. Get Vendor Details by vendor-id
- **Method**: `PUT`
- **URL**: `/api/vendors/{vendor_code}/`
- **Description**: Update the details for vendor.

#### Request

- fill the above vendor_code with uuid of the vendor (example- `/api/vendors/922419ed-64cb-4d5c-945b-36c290d36bb8/`)

- **Request Body**

```json
{
    "name": "shivam dubey",
    "contact_details": "aks1@gmail.com"
}
```
#### Response

- **Status Code**: 200 OK

- **Response Body**: 
```json
{
    "success": true,
    "status_code": 200,
    "message": "Vendor details updated successfully.",
    "result": {},
    "error": {}
}
```

### 5. Delete a Vendor
- **Method**: `DELETE`
- **URL**: `/api/vendors/{vendor_code}/`
- **Description**: Delete the vendor and its related performance data.

#### Request

- fill the above vendor_code with uuid of the vendor (example- `/api/vendors/922419ed-64cb-4d5c-945b-36c290d36bb8/`)

#### Response

- **Status Code**: 200 OK

- **Response Body**: 
```json
{
  "success": true,
  "status_code": 200,
  "message": "Vendor deleted successfully.",
  "result": {},
  "error": {}
}
```
### 6. Create Purchase Order
- **Method**: `POST`
- **URL**: `/api/purchase_orders/`
- **Description**: Creating a purchase order.

#### Request 
- Request body
```json
{
    "vendor_id": "922419ed-64cb-4d5c-945b-36c290d36bb8",
    "order_date": "2024-05-05",
    "items": [{
        "order_name": "john wick 1",
        "price": 500
    }, {
        "order_name": "haloball",
        "price": 1000
    }],
    "quantity": 4
}
```
#### Response

- **Status Code**: 200 OK

- **Response Body**: 
```json
{
    "success": true,
    "status_code": 200,
    "message": "Purchase order created successfully.",
    "result": {},
    "error": {}
}
```

### 7. Get all Purchase Orders
- **Method**: `GET`
- **URL**: `/api/purchase_orders/`
- **Description**: Get all the purchase orders.

#### Request
- query_params - `vendor_code` 
This query parameter used to filter the result on the basis of vendor_name and vendor_code(vendor-id)

#### Response

- **Status Code**: 200 OK

- **Response Body**: 
```json
{
    "success": true,
    "status_code": 200,
    "message": "Purchase orders list fetched successfully.",
    "result": [
        {
            "po_number": "990fb358-59d8-47fd-95d8-7ab80094f67a",
            "vendor_id": "922419ed-64cb-4d5c-945b-36c290d36bb8",
            "order_date": "2024-05-05T00:00:00Z",
            "items": [
                {
                    "order_name": "john wick 1",
                    "price": 500
                },
                {
                    "order_name": "haloball",
                    "price": 1000
                }
            ],
            "quantity": 4,
            "issue_date": "2024-05-05T11:10:25.205588Z"
        },
        {
            "po_number": "dbb73020-2ed1-4d6b-821a-3bde5bae8dde",
            "vendor_id": "922419ed-64cb-4d5c-945b-36c290d36bb8",
            "order_date": "2024-05-05T00:00:00Z",
            "items": [
                {
                    "order_name": "chewing gum",
                    "price": 500
                },
                {
                    "order_name": "haloball",
                    "price": 1000
                }
            ],
            "quantity": 1,
            "issue_date": "2024-05-05T06:27:14.452105Z"
        },
        {
            "po_number": "6eb3efd6-ebb1-472f-89e4-413775ccd958",
            "vendor_id": "922419ed-64cb-4d5c-945b-36c290d36bb8",
            "order_date": "2024-05-05T00:00:00Z",
            "items": [
                {
                    "order_name": "chewing gum",
                    "price": 500
                },
                {
                    "order_name": "haloball",
                    "price": 1000
                }
            ],
            "quantity": 1,
            "issue_date": "2024-05-05T05:35:23.897990Z"
        }]
}
   ```
### 8. Acknowledge purchase order by the Vendor
- **Method**: `POST`
- **URL**: `/api/purchase_orders/{po_number}/acknowledge/`
- **Description**: Purchase order is acknowledged by the vendor.

#### Request

- Provide the `po_number` in dynamic url to acknowledge the order

#### Response
- **Status Code**: 200 OK
- **Response Body**
```json
{
    "success": true,
    "status_code": 200,
    "message": "Purchase order acknowledged by vendor successfully.",
    "result": {},
    "error": {}
}
```
### 9. COMPLETE/CANCEL Purchase order
- **Method**: `PUT`
- **URL**: `/api/purchase_orders/{po_number}/po_status/{status}/`
- **Description**: Change the status of purchase order whether it is completed or cancelled.

#### Request

- Provide the `po_number` as well as `status` (COMPLETED OR CANCELLED) to define the purchase order.
- We can also provide the `quality_rating` in `query_params` to rate the quality of order by the vendor.

#### Response
- **Status Code**: 200 OK
- **Response Body**
```json
{
    "success": true,
    "status_code": 200,
    "message": "Purchase order status changed successfully.",
    "result": {},
    "error": {}
}
```

### 10. Vendor Performance History
- **Method**: `GET`
- **URL**: `/api/vendors/{vendor_code}/performance/`
- **Description**: Get the performance history of a vendor.

#### Request

- `vendor_code` provided in dynamic url to get the performance history of that particular vendor.

#### Response
- **Status Code**: 200 OK
- **Response Body**
```json
{
    "success": true,
    "status_code": 200,
    "message": "Performance history data fetched successfully.",
    "result": [
        {
            "id": 1,
            "created_at": "2024-05-05T11:18:02.078318Z",
            "updated_at": "2024-05-05T11:18:02.078347Z",
            "deleted_at": null,
            "performance_date": "2024-05-05T11:18:02.076744Z",
            "on_time_delivery_rate": 1.0,
            "quality_rating_avg": 4.0,
            "average_response_time": "00:09:42",
            "fulfillment_rate": 0.4444444444444444,
            "vendor_id": "922419ed-64cb-4d5c-945b-36c290d36bb8"
        }
    ],
    "error": {}
}
```

#### Below is the link to the postcollection for all apis used in the project.
This is a link to [Postman Collection](https://www.postman.com/speeding-flare-523969/workspace/vendor-management/collection/29181282-6fd94575-4fda-424d-987a-f670e4e16555?action=share&creator=29181282).


## *NOTE
**_It contains basic CRUD operations and uses of signals to update the metrics for real time updation to vendor performance. We can also apply the JWT authentication with sign-up sign-in apis added in the project. Also we have used sqlite3 but we could use any type of Relational database such as Postgresql, mssql and mysql when the project is scaled._**