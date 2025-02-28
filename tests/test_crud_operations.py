import unittest
from api.crud_operations import save_data, get_cryptos, update_price, delete

class TestCRUDOperations(unittest.TestCase):

    def setUp(self):
        self.sample_data = [{"name": "Bitcoin", "current_price": 45000}]
        save_data(self.sample_data)

    def test_update_price(self):
        result = update_price("Bitcoin", 50000)
        self.assertEqual(result)

    def test_delete(self):
        result = delete("Bitcoin")
        self.assertEqual(result)

if __name__ == "__main__":
    unittest.main()
