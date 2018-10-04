import re


class Validators:
    def valid_food(self, food):
        '''valid food item'''
        regex = "^[a-zA-Z_ ]+$"
        return re.match(regex, food)

    def valid_destination(self, destination):
        regex = "^[a-zA-Z0-9_ ]+$"
        return re.match(regex, destination)

    def valid_account(self, account):
        '''valid password and username'''
        regex = "^[a-zA-Z0-9_ ]+$"
        return re.match(regex, account)

    def valid_email(self, email):
        """valid email"""
        regex = "^[a-zA-Z0-9_+-]+@[a-zA-Z-]+\.[a-zA-Z0-]+$"
        return re.match(regex, email)
    


