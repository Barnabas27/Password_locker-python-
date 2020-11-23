import unittest

from user import User

from user import Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        
        self.new_user = User("Barbez","123")
        
    def test_init(self):
        
        self.assertEqual(self.new_user.username,"Barbez")
        self.assertEqual(self.new_user.password,"123")
        
    def tearDown(self):
        
        '''
        this cleans up after each test case
        '''
        User.User_List = []
    def test_save_multiple_user(self):
        '''
        this test is to check whether one can save multiple user object to the
        User_List
        '''
        self.new_user.save_user()
        test_user = User("barbez","12345")
        test_user.save_user()
        self.assertEqual(len(User.User_List),2)
        
        
    def test_delete_user(self):
        '''
        this is to test whether we can delete user from User_List
        '''
        self.new_user.save_user()
        test_user = User("barbez","12345")
        test_user.save_user()
        
        self.new_user.delete_user()
        self.assertEqual(len(User.User_List),1)
        
    def test_user_exist(self):
        '''
        checks whether User exists
        '''
        self.new_user.save_user()
        test_user = User("barbez","12345")
        test_user.save_user()
        
        
        user_exist = User.user_exist("12345")
        
        self.assertTrue(user_exist)
        
    def test_display_all_user(self):
        
        '''
        returns the whole list of users list
        '''
        self.assertEqual(User.display_user(),User.User_List)
        
        
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
        
    def test_save_credential(self):
        
        self.new_credential.save_credential()
        self.assertEqual(len(Credentials.User_Credentials_list),1)
        
    def tearDown(self):
        Credentials.User_Credentials_list = []
        """
        the clean up after each test is run
        """
    def test_save_multiple_credential(self):
        
        """
        this is to check whether we can save multiple contacts
        """
        self.new_credential.save_credential()
        test_credential = Credentials("facebook","@Prada","1234") #this is a new credential
        test_credential.save_credential()
        self.assertEqual(len(Credentials.User_Credentials_list),2)
    
    def test_delete_credential(self):
        
        """
        this is to test whether a credential can be deleted
        """
        self.new_credential.save_credential()
        test_credential = Credentials("facebook","@Prada","1234") #the new credential created
        test_credential.save_credential()
        
        self.new_credential.delete_credential() 
        """
        this will delete a credential
        """
        self.assertEqual(len(Credentials.User_Credentials_list),1)
        
    def test_display_all_credentials(self):
        
        """
        shows a list of all saved user credentials
        """
        self.assertEqual(Credentials.display_credentials(),Credentials.User_Credentials_list)
        
if __name__ =='__main__':
    unittest.main()