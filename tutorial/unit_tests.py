import unittest
class SomeUnitTests(unittest.TestCase):
    """
    Extend unittest.TestCase to make use of various tests.
    Python unittest is actually inpired by JUnit.
    """
    def setUp(self) -> None:
        """
        this runs BEFORE test function
        """
        print("setUp")

    def tearDown(self) -> None:
        """
        this runs AFTER every test function
        :return:
        """
        print("tearDown")

    def test_upper(self):
        print("test_upper")
        self.assertEqual("HELLO", 'hello'.upper())
        #self.assertEqual(1, 2)
        self.assertIn(1, [1,2,3])
        ok = None
        self.assertIs(ok, None)

    def test_lower(self):
        print("test_lower")

    def test_exceptions(self):
        with self.assertRaises(ZeroDivisionError):
            val = 2 / 0

if __name__ == '__main__':
    unittest.main()
