import unittest

from user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        
        self.new_user = User("Barbez","123")
        
    def test_init(self):
        
        self.assertEqual(self.new_user.username,"Barbez")
        self.assertEqual(self.new_user.password,"123")
        
        
if __name__ =='__main__':
    unittest.main()