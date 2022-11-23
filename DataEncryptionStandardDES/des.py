from Crypto.Cipher import DES
import binascii

def remove_padding(text, blocksize = 64):
    counter = 0
    for c in text[::-1]:
        if c == '$':
            counter += 1
        else:
            break
    return text[:-counter]

def add_padding(text, blocksize = 64):
    pad_len = blocksize - (len(text) % blocksize)
    padding = '$' * pad_len
    return text + padding

def encrypt(plain_text,key):
    des = DES.new(key, DES.MODE_CBC)
    return des.encrypt(bytearray(plain_text.encode()))

def decrypt(cipher_text,key):
    des = DES.new(key, DES.MODE_CBC)
    return des.decrypt(cipher_text)

