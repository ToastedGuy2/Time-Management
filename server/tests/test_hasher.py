from ..utils.hasher import Hasher
from password_generator import PasswordGenerator
from pytest import fixture
class TestHasher():

    @fixture
    def hasher(self):
        return Hasher()
    @fixture
    def rng_passwords(self):
        pwo = PasswordGenerator()
        return [pwo.generate() for n in range(25)]
    @fixture
    def hashed_passwords(self,hasher,rng_passwords):
        return [hasher.hash_password(
            password) for password in rng_passwords]

    def test_hash_password_length_is_120(self,hashed_passwords):
        for psw in hashed_passwords:
           assert len(psw) is 120

    def test_verify_password_is_correct(self,hasher,rng_passwords,hashed_passwords):
        for i in range(25):
            original_psw = rng_passwords[i]
            hash_psw = hashed_passwords[i]
            assert hasher.verify_password(
                original_psw, hash_psw) is True
