import unittest

from user import User

from user import Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        
        self.new_user = User("Barbez","123")
        
    def test_init(self):
        
        self.assertEqual(self.new_user.username,"Barbez")
        self.assertEqual(self.new_user.password,"123")
        
        
class TestCredentials(unittest.TestCase):
    """
    Test subclass that defines test cases for the credentials class behaviours
    """
    
    def setUp(self):
        
        self.new_credential = Credentials("twitter","@owslemy","456")
        
    def test_init(self):
        self.assertEqual(self.new_credential.sm_account,"twitter")
        self.assertEqual(self.new_credential.username,"@owslemy")
        self.assertEqual(self.new_credential.pass_word,"456")
        
        
if __name__ =='__main__':
    unittest.main()