import unittest
# import polls
from polls.views import convertTo62


class TestCal(unittest.TestCase):
    def test_encode(self):
        res = convertTo62(100)
        self.assertEqual(res, 10)


if __name__ == '__main__':
         unittest.main()