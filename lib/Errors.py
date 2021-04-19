class NoneTypeError(Exception):
    def __init__(self,msg="The value is None"):
        super().__init__(msg)
class UnknownCipherMethodError(Exception):
    def __init__(self,msg="The method of cipher is not supported"):
        super().__init__(msg)