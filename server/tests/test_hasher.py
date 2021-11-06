from ..utils.hasher import Hasher
from password_generator import PasswordGenerator
import unittest


class TestHasher(unittest.TestCase):

    def setUp(self):
        self.hasher = Hasher()
        # Arrange
        pwo = PasswordGenerator()
        self.rng_passwords = [pwo.generate() for n in range(25)]
        # Act
        self.hash_passwords = [self.hasher.hash_password(
            password) for password in self.rng_passwords]

    def test_hash_password_length_is_120(self):
        # Assert
        for psw in self.hash_passwords:
            self.assertEqual(len(psw), 120)

    def test_verify_password_is_correct(self):
        # Assert
        for i in range(25):
            original_psw = self.rng_passwords[i]
            hash_psw = self.hash_passwords[i]
            self.assertIs(self.hasher.verify_password(
                original_psw, hash_psw), True)


if __name__ == '__main__':
    unittest.main()
