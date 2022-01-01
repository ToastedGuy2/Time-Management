from ..utils.validations.user.user_validations import UserValidations
from password_generator import PasswordGenerator
from pytest import fixture
from random import randint
class TestUserValidations():
    @fixture
    def v(self):
        return UserValidations()
    @fixture
    def pwg(self):
        pwg = PasswordGenerator()
        pwg._schars = list("@%+\/'!#$^?:.(){[]}~-_`")
        return pwg

    def test_password_has_a_correct_length(self,pwg,v):
        for i in range(100):
            rng_length = randint(1, 100)
            pwg.minlen = rng_length
            pwg.maxlen = rng_length * 2
            pw = pwg.generate()
            assert v.min_length(pw, rng_length) is True

    def test_password_has_an_incorrect_length(self,pwg,v):
        for i in range(100):
            pw = pwg.generate()
            wrong_length = len(pw) * 1.5
            assert v.min_length(pw, wrong_length) is False

    def test_password_contains_min_n_uppercase_letters(self,pwg,v):
        for i in range(100):
            min_uppercase_chars = randint(0, 10)
            pwg.minuchars = min_uppercase_chars
            pw = pwg.generate()
            assert v.min_uppercase_characters(
                pw, min_uppercase_chars) is True

    def test_password_contains_wrong__min_n_uppercase_letters(self,pwg,v):
        for i in range(100):
            min_uppercase_chars = randint(0, 10)
            pwg.minuchars = min_uppercase_chars
            pw = pwg.generate()
            assert v.min_uppercase_characters(
                pw, len(pw) * 2) is False

    def test_password_contains_min_n_lower_letters(self,pwg,v):
        for i in range(100):
            min_lowercase_chars = randint(0, 10)
            pwg.minlchars = min_lowercase_chars
            pw = pwg.generate()
            assert v.min_lowercase_characters(
                pw, min_lowercase_chars) is True

    def test_password_contains_wrong__min_n_lowercase_letters(self,pwg,v):
        for i in range(100):
            min_lowercase_chars = randint(0, 10)
            pwg.minlchars = min_lowercase_chars
            pw = pwg.generate()
            assert v.min_lowercase_characters(
                pw, len(pw) * 4) is False

    def test_password_contains_min_n_special_characters(self,pwg,v):
        for i in range(100):
            min_special_chars = randint(0, 10)
            pwg.minschars = min_special_chars
            pw = pwg.generate()
            assert v.min_special_characters(
                pw, min_special_chars) is True

    def test_password_contains_min_n_numbers(self,pwg,v):
        for i in range(100):
            min_numbers = randint(0, 10)
            pwg.minnumbers = min_numbers
            pw = pwg.generate()
            assert v.min_numerical_characters(
                pw, min_numbers) is True

    def test_password_contains_wrong_min_n_numbers(self,pwg,v):
        for i in range(100):
            min_numbers = randint(0, 10)
            pwg.minnumbers = min_numbers
            pw = pwg.generate()
            assert v.min_numerical_characters(
                pw, len(pw) * 4) is False

    def test_password_is_strong(self,pwg,v):
        for i in range(100):
            pwg.minschars = 10
            pw = pwg.generate()
            assert v.is_password_strong(pw) is True

    def test_password_is_weak(self,pwg,v):
        pwg._schars
        for i in range(1000):
            pwg.maxlen = 7
            pw = pwg.generate()
            assert v.is_password_strong(pw) is False
