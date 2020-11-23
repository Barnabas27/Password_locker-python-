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
        
    

# class Credentials:
    
    
        
#     """
#     Class Credentials generates instances of what will be contained in the class
#     """
        
#     User_Credentials_list = []
        
#     def save_credential(self):
        
            
#         Credentials.User_Credentials_list.append(self)
            
#         """
#         save_credential method that saves credential objects into the user_credential_list
#         """
#     def __init__(self,sm_account,username,pass_word):
        
#         self.sm_account = sm_account
#         self.username = username
#         self.pass_word = pass_word
        
#     def delete_credential(self):
#         """
#         gets to delete a saved credential
#         """
#         Credentials.User_Credentials_list.remove(self)
        
        
#     @classmethod
#     def display_credentials(cls):
#         """
#         this returns the credential list
#         """
#         return cls.User_Credentials_list
        
        
   
        

            