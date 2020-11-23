#!/usr/bin/env python3.8
import random

from user import User

from user import Credentials


def create_user(username, password):
    """
    with this function a username and password is created
    """
    new_user = User(username, password)
    return new_user
def save_user(self):
    """
    this function saves user
    """
    
def delete_user(self):
    """
    this functions deletes user
    """
def create_credential(sm_account,username,password):
    '''
    Function creates new credentials
    '''
    new_credential = Credentials(sm_account,username,password)
    return new_credential


def save_credential(credential):
    """
    function to save credentials
    """
    credential.save_credential()
    
   


def del_credential(credential):
    """
    this functions deletes credentials
    """
    credential.delete_contact()


def display_credential():
    """
    this function displays credentials
    """
    return Credentials.display_credentials()


def main():
    while True:
        print("Let me make your work easy:select these abbreviations to manouver:to creat an acc use 'new': To display user 'du':To log in 'lg': To exit'x'")
        print('\n')
        abbreviation = input().lower()

        print('\n')

        if abbreviation == 'new':
            print('Create account:')
            account_created = input()

            print('Create password:')
            password_created = input()

            print('Please confirm password:')
            password_confirmed = input()
            

            while password_confirmed != password_created:
                print('Your passwords do not match,please try again!')
                password_confirmed = input()
                
                if password_created != password_confirmed:
                    
                    print('Make sure your passwords match:')
                    password_confirmed = input()
                    
                    if password_confirmed != password_created:
                        
                        print("You cannot create account.")
                        
                    else:
                        
                        print(f'You have successfully created the account{account_created}')
                        
                        print('Now log in:')
                        
                        print('Username:')
                        Username = input()
                        
                        print('Password:')
                        Password = input()
                        
                        while  Username != account_created or Password != password_created:
                            
                
                            print("Your Username or Password is incorrect.")
                
                
                            print('Username:')

                            Username = input()
                            print('Enter your password:')

                            Password = input()
                            
                            
                
            else:
                print(f'Welcome {account_created}')
                
                print (' Create your social media accounts:')  
                print('Enter your social media account:') 
                sm_account = input()
                print('Enter the username you use here:')
                username = input()
                print('The password you use in this account:')
                password = input()   
                
                save_credential(create_credential(sm_account,username,password))#creates and saves new credentials
                print('\n')
                print(f'Social media account{sm_account} with username {username} created.')
                print('Do you want to display your credentials?(y/n')
                answer = input()
                if answer == "y":
                    
                    display_credential()
                        
                    print('Here are alll your credentials:')
                    print('\n')
                        
                    for credential in display_credential():
                        print(f"{sm_account} {username} {password}")
                        
                        print('\n')
                else:
                    print('You don\'t have a credential_list yet.')
                
                
                
                
                
                
                
                
            
                
            
                    

                    
                
            # else:
            #     print(f"You have successfully created {account_created}")
        #     print('Now log in:')

        #     print('Username')
        #     Username = input()

        #     print('Enter password:')
        #     Password = input()

        #     while Username != account_created or Password != password_created:
        #         print('Check your username or password and try again.')
        #         print('Username:')

        #         Username = input()
        #         print('Enter your password:')

        #         Password = input()
        #     print(f'welcome {Username}')
            
        # elif abbreviation == 'lg':
        #     print('Enter your username:')
        #     regular_user = input()

        #     print('Enter your Password:')
        #     previous_user = input()
            
         
        #     while regular_user != Username or previous_user != Password:
        #         print('You are a scam: Would you want to create an account?')
        #         print('Username:')
        #         regular_user = input()
        #         print('Enter your password:')
        #         previous_user = input()            
        
        #     print(f"Welcome back {regular_user}!I have missed you")
        #     # print("Login user")

        # elif abbreviation == 'x':
        #     print('Take your time you are home')
        #     break


if __name__ == '__main__':
    main()
