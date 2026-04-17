from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()


def hash_password(password: str):
    return ph.hash(password)


def verify_hash(plain: str, hashed: str):
    try:
        return ph.verify(hashed, plain)
    except VerifyMismatchError:
        return False
