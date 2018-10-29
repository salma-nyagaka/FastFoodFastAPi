'''validators for input fields'''
import re


class Validators:
    ''' The validaion method'''
    def valid_food(self, food):
        '''valid food item'''
        regex = "^[a-zA-Z,_ ]+$"
        return re.match(regex, food)

    def valid_destination(self, destination):
        '''valid destination'''
        regex = "^[a-zA-Z0-9_ ]+$"
        return re.match(regex, destination)  

    def valid_price(self, price):
        '''valid price'''
        regex = "^[1-10_ ]+$"
        return re.match(regex, price)

    def valid_contact(self, contact):
        '''valid contact'''
        regex = "^[1-10_]+$"
        return re.match(regex, contact)

    def valid_account(self, account):
        '''valid password and username'''
        regex = "^[a-zA-Z0-9_ ]+$"
        return re.match(regex, account)

    def valid_phone(self, phone):
        '''valid phone number'''
        regex = "^[0-9_ ]+$"
        return re.match(regex, phone)

    def valid_password(self, password):
        '''valid password'''
        regex = "^[a-zA-Z0-9.!£$%%^&*()__ ]+$"
        return re.match(regex, password)

    def valid_email(self, email):
        '''valid email'''
        regex = "^[a-zA-Z0-9_+-]+@[a-zA-Z-]+\.[a-zA-Z0-]+$"
        return re.match(regex, email)

