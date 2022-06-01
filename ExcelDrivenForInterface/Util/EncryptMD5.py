import hashlib
import time


def encryptMD5(sourceString):
    # MD5加密
    m5 = hashlib.md5()
    m5.update(sourceString.encode())
    return m5.hexdigest()