#!/usr/bin/env python3.8
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
    
