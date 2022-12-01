from rest_framework import status
from rest_framework.test import APITestCase


class TestClient(APITestCase):

    def setUp(self):
        self.wrong_cl_data = {"phone_number": 1,
                              "phone_code": 0,
                              "tag": "some tag",
                              "time_zone": "3"}
        self.correct_cl_data = {"phone_number": 79992221100,
                                "phone_code": 999,
                                "tag": "some tag",
                                "time_zone": "1"}

    def test_registration_correct_user(self):
        response = self.client.post('/api/v1/clients/', self.correct_cl_data)
        print(response.json()['id'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_wrong_user(self):
        response = self.client.post('/api/v1/clients/', self.wrong_cl_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

