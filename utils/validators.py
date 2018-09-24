import re 


class Validators:
    def valid_food_name(self, name):
        regex = "^[a-zA-Z0-9_ ]+$"
        return re.match(regex, name)


    def valid_food_description(self, description):
        regex = "^[a-zA-Z0-9_ ]+$"
        return re.match(regex, description)
