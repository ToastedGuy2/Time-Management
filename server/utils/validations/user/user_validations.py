from ....repositories.user_repository import UserRepository


class UserValidations:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    special_characters = "@%+\/'!#$^?:.(){[]}~-_`"

    def are_parameters_valid(self, string, n):
        return True if type(string) is str and type(n) is int else False

    def min_length(self, string, length):
        if not self.are_parameters_valid(string, length):
            return False
        return len(string) >= length

    def min_numerical_characters(self, string, n):
        if not self.are_parameters_valid(string, n):
            return False
        numerical_characters = 0
        for char in string:
            if(char.isdigit()):
                numerical_characters += 1
            if(numerical_characters >= n):
                return True
        return False

    def min_uppercase_characters(self, string, n):
        if not self.are_parameters_valid(string, n):
            return False
        uppercase_alphabet = self.alphabet.upper()
        n_uppercase = 0
        for letter in uppercase_alphabet:
            n_uppercase += string.count(letter)
            if(n_uppercase >= n):
                return True
        return False

    def min_lowercase_characters(self, string, n):
        if not self.are_parameters_valid(string, n):
            return False
        lowercase_alphabet = self.alphabet.lower()
        n_lowercase = 0
        for letter in lowercase_alphabet:
            n_lowercase += string.count(letter)
            if(n_lowercase >= n):
                return True
        return False

    def min_special_characters(self, string, n):
        if not self.are_parameters_valid(string, n):
            return False
        n_special_characters = 0
        for character in self.special_characters:
            n_special_characters += string.count(character)
            if(n_special_characters >= n):
                return True
        return False

    def is_password_strong(self, password):
        if not self.min_length(password, 8):
            return False
        if not self.min_special_characters(password, 1):
            return False
        if not self.min_numerical_characters(password, 1):
            return False
        if not self.min_uppercase_characters(password, 1):
            return False
        if not self.min_lowercase_characters(password, 1):
            return False
        return True
