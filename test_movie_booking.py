import unittest
from movie_booking import add_tickets

class TestBooking(unittest.TestCase):
    def test_total(self):
        self.assertEqual(add_tickets(150, 2), 300)

if __name__ == "__main__":
    unittest.main()