import random
import string

class User:
    '''
    Class that generates new instances ofCredentials user i.e: username and password
    '''
    User_List = []
    
    def save_user(self):
        
        User.User_List.append(self)
    
    def __init__(self,username,password):
        
        """
        intro of the __init__method to define properties for our objects
        """  
        
    
        self.username = username
        self.password = password
        
        
    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.User_List.remove(self)
        
    @classmethod
    def user_exist(cls,number):
        '''
        checks whether our user exists
        '''
        for user in cls.User_List:
            if user.password == number:
                return True
            
        return False     
    
    @classmethod
    def display_user(cls):
        '''
        this method returns users' list
        '''
        return cls.User_List   
    

class Credentials:
    
    
        
    """
    Class Credentials generates instances of what will be contained in the class
    """
        
    User_Credentials_list = []
        
    def save_credential(self):
        
            
        Credentials.User_Credentials_list.append(self)
            
        """
        save_credential method that saves credential objects into the user_credential_list
        """
    def __init__(self,sm_account,username,password):
        
        self.sm_account = sm_account
        self.username = username
        self.password = password
        
    def delete_credential(self):
        """
        gets to delete a saved credential
        """
        Credentials.User_Credentials_list.remove(self)
        
        
    @classmethod
    def display_credentials(cls):
        """
        this returns the credential list
        """
        return cls.User_Credentials_list
        
    def generate_password(self):
        '''
        generates random password
        '''
        password = string.ascii_uppercase + string.ascii_lowercase + "damzie"
        return ''.join(random.choice(password) for i in range(1,9))
        
   
        

            