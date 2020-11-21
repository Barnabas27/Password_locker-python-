#!/usr/bin/env python3.8
import random

from user import User

from user import Credentials

def create_user(username,password):
    """
    with this function a username and password is created
    """
    new_user = User(username,password)
    return new_user

def save_credential(self):
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
        print("Let me make your work easy:select these abbreviations to manouver:to creat an acc use 'new': To log in 'lg': To exit'x'")
        print('\n')
        abbreviation = input().lower()
        
        print('\n')
        
        if abbreviation == 'new':
            print('Create account')
            account_created = input()
            print('Create password')
            password_created = input()
            print('Please confirm password')
            password_confirmed = input()
            while password_confirmed != password_created:
                print('Your passwords do not match')
                password_created = input()
                print('Make sure your passwords match:')
                password_confirmed = input()
            else:
                print(f"You have successfully created {account_created}")
            
        
if __name__ =='__main__':
    main()
