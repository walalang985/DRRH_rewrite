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

class CipherType:
    rsa = "RSA"
    fernet = "FERNET"
class cipher:
    type = None
    def __init__(self, type = CipherType.fernet or CipherType.rsa or None):
        if type == CipherType.fernet and type == CipherType.rsa and type == None:
            self.type = type
        return
    def exec(self,msg,key = None):
        if self.type == CipherType.rsa:
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
        key = None
        def __init__(self,key):
            self.key = key
            return
        def isRSA(self):
            try:
                RSA.importKey(self.key)
                return True
            except Exception:
                return False
        def isFernet(self):
            try:
                Fernet(self.key)
                return True
            except Exception:
                return False
a = cipher("#!@#")
print(a.type)

