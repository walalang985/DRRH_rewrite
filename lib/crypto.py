from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from cryptography.fernet import Fernet
import base64 as b64,hashlib

class NoneTypeError(Exception):
    def __init__(self,msg="The value is None"):
        super().__init__(msg)
class UnknownCipherMethodError(Exception):
    def __init__(self,msg="The method of cipher is not supported"):
        super().__init__(msg)

class CipherType():
    ENC = "enc"
    DEC = "dec"
class CipherMode():
    RSA = "RSA"
    FERNET = "FERNET"
class KeyType():
    RSAKEY = "KEYRSA"
    FERKEY = "FERKEY"
class KeyLoader(object):
    keytype = None
    key = None
    def __init__(self,type:KeyType.RSAKEY or KeyType.FERKEY,key):
        self.keytype = type
        self.key = key
        return
    def load(self):
        if self.keytype == KeyType.RSAKEY:
            return RSA.importKey(self.key)
        elif self.keytype == KeyType.FERKEY:
            return Fernet(self.key)
class KeyGen(object):
    keytype = None
    def __init__(self,type:KeyType.FERKEY or KeyType.RSAKEY):
        self.keytype = type
        return
    def generate(self):
        if self.keytype == KeyType.RSAKEY:
            key = RSA.generate(2048)     
            return {"public" : key.public_key().export_key().decode(), "private" : key.export_key().decode()}
        elif self.keytype == KeyType.FERKEY:
            return Fernet.generate_key().decode()
        else:
            return None
class cipher(object):
    mode = None
    ctype = None
    key = None
    def __init__(self,key,type = CipherMode.RSA or CipherMode.FERNET or None):
        self.mode = type
        return
    def encrypt(self,msg,key):
        if self.mode == None:
            raise NoneTypeError
        if self.mode == CipherMode.RSA:
            rsakey = KeyLoader(KeyType.RSAKEY,key).load()
            return b64.b64encode(PKCS1_v1_5.new(rsakey).encrypt(msg.encode())).decode()
        elif self.mode == CipherMode.FERNET:
            fernet = KeyLoader(KeyType.FERKEY,key).load()
            return fernet.encrypt(msg.encode())
    def decrypt(self,msg,key):
        if self.mode == None:
            raise NoneTypeError
        if self.mode == CipherMode.RSA:
            rsakey = KeyLoader(KeyType.RSA,key).load()
            return PKCS1_v1_5.new(rsakey).decrypt(b64.b64decode(msg), Random.new(20+SHA.digest_size)).decode()
        elif self.mode == CipherMode.FERNET:
            fernet = KeyLoader(KeyType.FERKEY,key).load()
            return fernet.decrypt(msg).decode()
    def hash(self, msg):
        return hashlib.sha3_512(hashlib.sha512(msg.encode()).hexdigest().encode()).hexdigest()

def __init__():
    return
def generate(keysize=2048) -> dict:
        key = RSA.generate(keysize)
        return {"public" : key.public_key().export_key().decode(), "private" : key.export_key().decode()}
def encrypt(msg,pubkey) -> str:
    return b64.b64encode(PKCS1_v1_5.new(RSA.importKey(pubkey)).encrypt(msg.encode())).decode()
def decrypt(msg,privkey) -> str:
    return PKCS1_v1_5.new(RSA.importKey(privkey)).decrypt(b64.b64decode(msg), Random.new(20+SHA.digest_size)).decode()
def hash(msg) -> str:#dual hash implementation for a much secure verification
    return hashlib.sha3_512(hashlib.sha256(msg.encode()).hexdigest().encode()).hexdigest()

print(cipher().hash("TEST"))
