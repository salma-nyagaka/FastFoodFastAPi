import re


class Validators:
    def valid_food_name(self, name):
        regex = "^[a-zA-Z_ ]+$"
        return re.match(regex, name)

    def valid_food_description(self, description):
        regex = "^[a-zA-Z_ ]+$"
        return re.match(regex, description)

    def valid_destination(self, destination):
        regex = "^[a-zA-Z0-9_ ]+$"
        return re.match(regex, destination)

    def valid_name(self, name):
        regex = "^[a-zA-Z_ ]+$"
        return re.match(regex, name)
    
    def valid_username(self, username):
        regex = "^[a-zA-Z0-9_ ]+$"
        return re.match(regex, username)

    def valid_password(self, password):
        """ valid password """
        regex = "^[a-zA-Z0-9_ ]+$"
        return re.match(regex, password)

    def valid_email(self, email):
        """valid email"""
        regex = "^[a-zA-Z0-9_+-]+@[a-zA-Z-]+\.[a-zA-Z0-]+$"
        return re.match(regex, email)
    


