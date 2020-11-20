class User:
    '''
    Class that generates new instances ofCredentials user i.e: username and password
    '''
    
    def __init__(self,username,password):
        """
        intro of the __init__method to define properties for our objects
        """  
    
        self.username = username
        self.password = password

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
    def __init__(self,sm_account,username,pass_word):
        
        self.sm_account = sm_account
        self.username = username
        self.pass_word = pass_word
        
   
        

            