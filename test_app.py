import unittest

from app import helloWorld

class TestApp(unittest.TestCase):
    def testHelloWorld(self):
        self.assertEqual(helloWorld(),"Hello world")
        
if __name__ == "__main__":
    unittest.main()