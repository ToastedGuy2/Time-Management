from passlib.context import CryptContext


class Hasher:

    def __init__(self) -> None:
        self.myctx = CryptContext(schemes=["sha512_crypt"], deprecated="auto")

    def hash_password(self, password):
        return self.myctx.hash(password)

    def verify_password(self, password, hash):
        return self.myctx.verify(password, hash)
