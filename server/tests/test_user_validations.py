from ..utils.validations.user.user_validations import UserValidations
from password_generator import PasswordGenerator
from random import randint
from unittest import TestCase
class TestUserValidations(TestCase):
    def setUp(self):
        self.v = UserValidations()
        self.pwg = PasswordGenerator()
        self.pwg._schars = list("@%+\/'!#$^?:.(){[]}~-_`")

    def test_password_has_a_correct_length(self):
        for i in range(100):
            rng_length = randint(1, 100)
            self.pwg.minlen = rng_length
            self.pwg.maxlen = rng_length * 2
            pw = self.pwg.generate()
            self.assertTrue(self.v.min_length(pw, rng_length))

    def test_password_has_an_incorrect_length(self):
        for i in range(100):
            pw = self.pwg.generate()
            wrong_length = len(pw) * 1.5
            self.assertFalse(self.v.min_length(pw, wrong_length))

    def test_password_contains_min_n_uppercase_letters(self):
        for i in range(100):
            min_uppercase_chars = randint(0, 10)
            self.pwg.minuchars = min_uppercase_chars
            pw = self.pwg.generate()
            self.assertTrue(self.v.min_uppercase_characters(
                pw, min_uppercase_chars))

    def test_password_contains_wrong__min_n_uppercase_letters(self):
        for i in range(100):
            min_uppercase_chars = randint(0, 10)
            self.pwg.minuchars = min_uppercase_chars
            pw = self.pwg.generate()
            self.assertFalse(self.v.min_uppercase_characters(
                pw, len(pw) * 2))

    def test_password_contains_min_n_lower_letters(self):
        for i in range(100):
            min_lowercase_chars = randint(0, 10)
            self.pwg.minlchars = min_lowercase_chars
            pw = self.pwg.generate()
            self.assertTrue(self.v.min_lowercase_characters(
                pw, min_lowercase_chars))

    def test_password_contains_wrong__min_n_lowercase_letters(self):
        for i in range(100):
            min_lowercase_chars = randint(0, 10)
            self.pwg.minlchars = min_lowercase_chars
            pw = self.pwg.generate()
            self.assertFalse(self.v.min_lowercase_characters(
                pw, len(pw) * 4))

    def test_password_contains_min_n_special_characters(self):
        for i in range(100):
            min_special_chars = randint(0, 10)
            self.pwg.minschars = min_special_chars
            pw = self.pwg.generate()
            self.assertTrue(self.v.min_special_characters(
                pw, min_special_chars))

    def test_password_contains_min_n_numbers(self):
        for i in range(100):
            min_numbers = randint(0, 10)
            self.pwg.minnumbers = min_numbers
            pw = self.pwg.generate()
            self.assertTrue(self.v.min_numerical_characters(
                pw, min_numbers))

    def test_password_contains_wrong_min_n_numbers(self):
        for i in range(100):
            min_numbers = randint(0, 10)
            self.pwg.minnumbers = min_numbers
            pw = self.pwg.generate()
            self.assertFalse(self.v.min_numerical_characters(
                pw, len(pw) * 4))

    def test_password_is_strong(self):
        for i in range(100):
            self.pwg.minschars = 10
            pw = self.pwg.generate()
            self.assertTrue(self.v.is_password_strong(pw))

    def test_password_is_weak(self):
        self.pwg._schars
        for i in range(1000):
            self.pwg.maxlen = 7
            pw = self.pwg.generate()
            self.assertFalse(self.v.is_password_strong(pw))
