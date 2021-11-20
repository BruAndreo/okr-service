import hashlib

def encrypt(value: str) -> str:
    hash = hashlib.md5(value.encode())
    return hash.hexdigest()