# Password-Locker

## Author 
[Barnabas-Kamau] (https://github.com/barnabas27)

## Description.
Password Locker this is python project that enables user to creates an accounts as well as save their social media credentials i.e the social media, username used and the password. The app also generates passwords for user who are making new accounts in the social media of choice.

## User Stories
What the user does:
* Create an account
* Store existing account credentials
* log in into account once one signs up.
* display credentials once one is signed up.
* The app by the users choice can be generated for a random password to use in signing up to a social media account.
* The user can delete the credential once user is logged in.

## Installation / Setup instruction.

#### For the user to operate you need to install:
* Python3 and its subsequent versions.
* pip

#### Cloning
* Through the terminal
* make a directory where you will get to clone this project.
* access the directory
* access it using your favorite editor
### Running the app:
* To run the app, open the terminal and run the command:
                    python3 run.py
* to run test for the app:
                    python3 user_test.py


## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./run.py```|Let me make your work easy:select any of these abbreviations to manoever<br>* new ---  Create New Account * lg ---  Login |
|Select  new| create account then enter your username ----enter your credentials----do you want to input your own password or generate| Welcome ```username```, Your account has been created succesfully! You want to add your own credentials|
|Select lg  | Enter your password and username you signed up with|  Choices to help you navigate through the application|
|Save new credential in the application| In the prompt to save just save|Enter Account's name, Accounts' username, Account's password alternatively you can have a password generated for you automatically<br>choose ```n``` to enter your password or ```y``` for the application to generate a password for you |
|Display all stored credentials | Enter ```y```in the prompt to see your credentials|A list of all credentials that has been stored or ```You don't have any credentials saved``` |



## Technologies used
* python3.8

## known bugs
* No known bugs at the moment
## Contact information
* for questions of contributions:
[bkamau032@gmail.com]

## License
* [[License:MIT]](LICENSE.md)
* copyright (c) 2020 **Barnabas Kamau**
