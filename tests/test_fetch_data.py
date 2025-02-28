import unittest
from api.fetch_data import fetch_crypto_data

class TestFetchData(unittest.TestCase):

    def test_fetch_crypto_data(self):
        data = fetch_crypto_data()
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)

if __name__ == "__main__":
    unittest.main()
