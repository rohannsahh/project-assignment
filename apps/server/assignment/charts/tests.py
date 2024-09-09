from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class ChartDataAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_candlestick_data_view(self):
        response = self.client.get('/api/candlestick-data/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("data", response.data)
        self.assertEqual(len(response.data["data"]), 4)

    def test_line_chart_data_view(self):
        response = self.client.get('/api/line-chart-data/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["labels"], ["Jan", "Feb", "Mar", "Apr"])
        self.assertEqual(response.data["data"], [10, 20, 30, 40])

    def test_bar_chart_data_view(self):
        response = self.client.get('/api/bar-chart-data/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["labels"], ["Product A", "Product B", "Product C"])
        self.assertEqual(response.data["data"], [100, 150, 200])

    def test_pie_chart_data_view(self):
        response = self.client.get('/api/pie-chart-data/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["labels"], ["Red", "Blue", "Yellow"])
        self.assertEqual(response.data["data"], [300, 50, 100])

class ChartDataIntegrationTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_full_data_flow(self):
        candlestick_response = self.client.get('/api/candlestick-data/')
        self.assertEqual(candlestick_response.status_code, status.HTTP_200_OK)
        self.assertIn("data", candlestick_response.data)
