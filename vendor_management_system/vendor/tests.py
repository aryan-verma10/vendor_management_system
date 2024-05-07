from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status


class VendorManagementAPITestCase(TestCase):
    

    def setUpClass(cls):
        super().setUpClass()
        cls.client = APIClient()
        


    def test_create_vendor(self):
        '''
            Create a new vendor to test
        '''
        data = {
                "name": "aryan verma",
                "contact_details": "dpsary9339@gmail.com",
                "address": "hello world"
            }
        

        response = self.client.post('/api/vendors/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('message' in response.data)   

        print("Vendor_created successfully")
        


    def test_get_vendors(self):
        '''
            Get all the vendor list
        '''
        response = self.client.get('/api/vendors/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('result' in response.data)
        print(response.data)

    
    
    def test_get_vendor_by_id(self):
        '''
            Test to get a vendor by its id complete details
        ''' 
        vendor_id = '922419ed64cb4d5c945b36c290d36bb8'

        response = self.client.get(f'/api/vendors/{vendor_id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    
