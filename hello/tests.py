import unittest
from greetings import greet

def test_greet1():
    # Set Up
    name = 'Ron'
    
    # Execute 
    greeting  = greet(name)
    
    # Validate
    assert(greeting=='Hello, Ron!')
    
    # Cleanup
    # Nothing to do here... Could delete variables etc.    
    
    
class SomeTests(unittest.TestCase):
    
    def test_greet2(self):
        self.assertEqual(greet('Ron'), 'Hello, Ron!')
    
    def test_greet3(self):
        self.assertNotEqual(greet('Charles'), 'Hello, Charlie!')

if __name__ == '__main__':
    unittest.main()