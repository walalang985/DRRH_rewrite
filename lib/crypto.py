from scripts import CipherType
from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from cryptography.fernet import Fernet
import hashlib
from base64 import b64encode,b64decode
class NoneTypeError(Exception):
    def __init__(self,msg="The value is None"):
        super().__init__(msg)
class UnknownCipherMethodError(Exception):
    def __init__(self,msg="The method of cipher is not supported"):
        super().__init__(msg)

class cipher:
    type = None
    class CipherMode:
        enc = "ENC"
    class CipherType:
        rsa = "RSA"
        fernet = "FERNET"
        def __init__(self):
            return
    class KeyLoad(object):        
        type = None
        def __init__(self,type=CipherType.fernet or CipherType.rsa):
            self.type = type
            return
        def load(self,key):
            if self.type == CipherType.rsa:
                return RSA.importKey(key)
            elif self.type == CipherType.fernet:
                return Fernet(key)
    class KeyGen(object):
        type = None
        def __init__(self,type = None):
            if type != CipherType.fernet or CipherType.rsa:
                raise ValueError
            else:
                self.type = type
            return
        def generate(self):
            if self.type == CipherType.rsa:
                key = RSA.generate(2048)
                return key.public_key().export_key().decode(),key.export_key().decode()
            elif self.type == CipherType.fernet:
                return Fernet.generate_key().decode()        
    class KeyCheck(object):
        keyType = None
        def __init__(self,key):
            try:
                RSA.importKey(key)
                self.keyType = "RSA"
            except:
                pass
            try:
                Fernet(key)
                self.keyType = "FERNET"
            except:
                pass

            return
    def __init__(self, type = CipherType.fernet or CipherType.rsa or None, key = None):
        self.type = type
        return
    def exec(self,msg,key = None):
        if key == None:
            return hashlib.sha512(hashlib.sha3_512(msg.encode()).hexdigest()).hexdigest()
        else:
            if self.KeyCheck(key).keyType == "RSA":
                


