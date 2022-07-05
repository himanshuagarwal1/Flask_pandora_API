import unittest

import requests


class ApiTest(unittest.TestCase):
    URL = "http://127.0.0.1:5000/"


    def test_1_people(self):
        response = requests.get(ApiTest.URL + "people/" + "Decker&Mckenzie")
        self.assertEqual(response.status_code, 200)
        
        
    def test_2_common_friends(self):
        response = requests.get(ApiTest.URL+"peopletwo/" + "Bonnie_Bass&Rosemary_Hayes")
        self.assertEqual(response.status_code , 200)
        
    
    def test_3_get_employees(self):
        response = requests.get(ApiTest.URL +"company/" + "MAINELAND")
        self.assertEqual(response.status_code, 200)
            



    
    


if __name__ == '__main__':
    
    
    unittest.main()