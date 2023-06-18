import unittest
import json
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_calculate_min(self):
        payload = {
            "numbers": [4, 2, 6, 1, 9],
            "quantifier": 2
        }
        response = self.app.post("/min", json=payload)
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["min_numbers"], [1, 2])

    def test_calculate_min_invalid(self):
        payload = {
            "numbers": [4, 2, 6, 1, 9]
        }
        response = self.app.post("/min", json=payload)
        self.assertEqual(response.status_code, 400)


    def test_calculate_max(self):
        payload = {
            "numbers": [4, 2, 6, 1, 9],
            "quantifier": 2
        }
        response = self.app.post("/max", json=payload)
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["max_numbers"], [9, 6])

    def test_calculate_average(self):
        payload = {
            "numbers": [4, 2, 6, 1, 9]
        }
        response = self.app.post("/avg", json=payload)
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["average"], 4.4)

    def test_calculate_median(self):
        payload = {
            "numbers": [4, 2, 6, 1, 9]
        }
        response = self.app.post("/median", json=payload)
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["median"], 4)

    def test_calculate_percentile(self):
        payload = {
            "numbers": [4, 2, 6, 1, 9],
            "quantifier": 75
        }
        response = self.app.post("/percentile", json=payload)
        data = json.loads(response.data.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["percentile"], 6)

if __name__ == "__main__":
    unittest.main()