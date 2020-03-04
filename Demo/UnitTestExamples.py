import unittest
from Example import Example


class MyTestCase(unittest.TestCase):

    def test_add(self):
        result = Example.add(self, 10, 20)
        self.assertEqual(result, 30)

    def test_sub(self):
        result = Example.sub(self, 50, 30)
        self.assertEqual(result, 20)


if __name__ == '__main__':
    unittest.main()
