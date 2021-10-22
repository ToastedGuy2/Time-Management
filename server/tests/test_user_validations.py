from ..utils.validations.user.user_validations import UserValidations


class TestUserValidations:
    v = UserValidations()

    def test_parameters_are_valid(self):
        assert self.v.are_parameters_valid("", 1) is True

    def test_parameters_are_not_valid(self):
        assert self.v.are_parameters_valid(1, False) is False
        assert self.v.are_parameters_valid(True, 1) is False
        assert self.v.are_parameters_valid({}, UserValidations()) is False
        assert self.v.are_parameters_valid([], UserValidations) is False

    def test_password_has_a_correct_length(self):
        assert self.v.min_length("Hello World", 8) is True
        assert self.v.min_length("1111111111", 10) is True
        assert self.v.min_length("World", 4) is True

    def test_password_has_an_incorrect_length(self):
        assert self.v.min_length("1", 2) is False
        assert self.v.min_length("two", 4) is False
        assert self.v.min_length("three", 12) is False
        assert self.v.min_length("four", 5) is False

    def test_password_contains_min_n_uppercase_letters(self):
        assert self.v.min_uppercase_characters(
            "Password", 1) is True
        assert self.v.min_uppercase_characters("Heavy Storm", 2) is True
        assert self.v.min_uppercase_characters(
            "DARK world".upper(), 3) is True
        assert self.v.min_uppercase_characters(
            "Storm Troopers".upper(), 2) is True
        assert self.v.min_uppercase_characters(
            "YODA".upper(), 4) is True
        assert self.v.min_uppercase_characters(
            "CRASH!!!".upper(), 5) is True

    def test_password_contains_wrong__min_n_uppercase_letters(self):
        self.v.min_uppercase_characters("Megaman", 2) is False
        self.v.min_uppercase_characters("Megaman X", 3) is False
        self.v.min_uppercase_characters("GTA San Andreas", 5) is False
        self.v.min_uppercase_characters(
            "Shadow of the Tomb Raider", 6) is False
        self.v.min_uppercase_characters("Shadow of Colossus", 10) is False
        self.v.min_uppercase_characters("Resident Evil", 4) is False

    def test_password_contains_min_n_lower_letters(self):
        assert self.v.min_lowercase_characters("Black Clover", 1) is True
        assert self.v.min_lowercase_characters("Naruto", 2) is True
        assert self.v.min_lowercase_characters("One Piece", 3) is True
        assert self.v.min_lowercase_characters("Bleach", 4) is True
        assert self.v.min_lowercase_characters("D-gray man", 6) is True
        assert self.v.min_lowercase_characters("Dragon Ball Kai", 9) is True
        assert self.v.min_lowercase_characters(
            "Fullmetal Alchemist", 10) is True

    def test_password_contains_wrong__min_n_lowercase_letters(self):
        assert self.v.min_lowercase_characters("Getsuga Tenshou", 15) is False
        assert self.v.min_lowercase_characters("Zero", 5) is False
        assert self.v.min_lowercase_characters("Code Geass", 8) is False
        assert self.v.min_lowercase_characters(
            "Monogatari Series", 15) is False
        assert self.v.min_lowercase_characters("Kingdom", 7) is False
        assert self.v.min_lowercase_characters(
            "Boku no hero academia", 20) is False
        assert self.v.min_lowercase_characters(
            "Shingeki no Kyojin", 17) is False

    def test_password_contains_min_n_special_characters(self):
        assert self.v.min_special_characters("T.w.o", 2) is True
        assert self.v.min_special_characters("T_hr_e_e", 3) is True
        assert self.v.min_special_characters("$F$i$v$e$", 5) is True
        assert self.v.min_special_characters("__S__i__x", 4) is True

    def test_password_contains_wrong_min_n_special_characters(self):
        assert self.v.min_special_characters("AlgoExpert.io", 3) is False
        assert self.v.min_special_characters("+_+", 4) is False
        assert self.v.min_special_characters(
            "1.25 + 1.25 = 2.5", 5) is False  # = is an invalid character
        assert self.v.min_special_characters(".___.", 7) is False
        assert self.v.min_special_characters("--__--", 8) is False

    def test_password_contains_min_n_numbers(self):
        assert self.v.min_numerical_characters("22", 2) is True
        assert self.v.min_numerical_characters("333", 3) is True
        assert self.v.min_numerical_characters("4444", 4) is True
        assert self.v.min_numerical_characters("55555", 5) is True
        assert self.v.min_numerical_characters("10_10_10_10_10", 8) is True

    def test_password_contains_wrong_min_n_numbers(self):
        assert self.v.min_numerical_characters("0_0", 3) is False
        assert self.v.min_numerical_characters("o_o", 2) is False
        assert self.v.min_numerical_characters(
            "1.25 + 1.25 = 2.5", 10) is False  # = is an invalid character
        assert self.v.min_numerical_characters("i7z@!LfWTsw6", 3) is False
        assert self.v.min_numerical_characters("z6*%h&wdcSia", 4) is False

    def test_password_is_strong(self):
        assert self.v.is_password_strong("I'm_a $trong-password2") is True
        assert self.v.is_password_strong("yRAg6JGK%Rba") is True
        assert self.v.is_password_strong("i7z@!LfWTsw6") is True
        assert self.v.is_password_strong("z6*%h&wdcSia") is True
        assert self.v.is_password_strong(
            "Labrador-Ecosystem6-Resource-Disengage-Lego") is True

    def test_password_is_weak(self):
        assert self.v.is_password_strong("") is False
        assert self.v.is_password_strong("fV7J%p") is False
        assert self.v.is_password_strong("Pfh*6") is False
