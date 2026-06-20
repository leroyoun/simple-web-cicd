import sys
sys.path.insert(0,".")
from app import app
import unittest

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
    
    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        data = response.data.decode("utf-8")
        self.assertIn("CI", data)

if __name__ == "__main__":
    unittest.main()
