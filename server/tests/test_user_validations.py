from ..model.validations.user.user_validations import UserValidations


class TestUserValidations:
    v = UserValidations()

    def test_parameters_are_valid(self):
        assert self.v.are_parameters_valid("", 1)

    def test_password_is_not_a_string(self):
        assert not self.v.are_parameters_valid(True, 1)

    def test_min_characters_is_not_a_numeric_value(self):
        assert not self.v.are_parameters_valid("", False)

    def test_parameters_are_not_valid(self):
        assert not self.v.are_parameters_valid(1, False)

    def test_string_length_is_8(self):
        password = "Hello World"
        assert self.v.min_length(password, 8)

    def test_string_length_is_less_than_8(self):
        password = "Failure"
        assert not self.v.min_length(password, 8)

    def test_password_contains_min_2_uppercase_letters(self):
        password = "Hello World"
        assert self.v.min_uppercase_characters(password, 2)

    def test_password_contains_no_uppercase_letters(self):
        password = "hello_world"
        assert not self.v.min_uppercase_characters(password, 2)

    def test_password_contains_min_4_lowercase_letters(self):
        password = "Hello World"
        assert self.v.min_lowercase_characters(password, 2)

    def test_password_contains_no_lowercase_letters(self):
        password = "hello_world"
        assert not self.v.min_lowercase_characters(password.upper(), 1)

    def test_password_contains_min_4_special_characters_letters(self):
        password = "~.Hello World$"
        assert self.v.min_special_characters(password, 2)

    def test_password_contains_no_special_characters_letters(self):
        password = "hello world"
        assert not self.v.min_special_characters(password.upper(), 1)

    def test_password_is_strong(self):
        assert self.v.is_password_strong("I'm_a $trong-password")
        assert self.v.is_password_strong("yRAg6JGK%Rba")
        assert self.v.is_password_strong("i7z@!LfWTsw6")
        assert self.v.is_password_strong("z6*%h&wdcSia")
        assert self.v.is_password_strong(
            "Labrador-Ecosystem6-Resource-Disengage-Lego")

    def test_password_is_weak(self):
        assert not self.v.is_password_strong("")
        assert not self.v.is_password_strong("fV7J%p")
        assert not self.v.is_password_strong("Pfh*6")
