import crypto
import sys
sys.modules['Crypto'] = crypto
from crypto.Cipher import PKCS1_OAEP
from crypto.PublicKey import RSA


def readPEM(pemfile):
    h = open(pemfile, 'r')
    key = RSA.importKey(h.read())
    h.close()
    return key

def rsa_dec(msg):
    private_key = readPEM('private_shhan.pem')
    cipher = PKCS1_OAEP.new(private_key)
    decdata = cipher.decrypt(msg)
    
    return decdata

def decoded(f):
    ciphered = f.read()
    
    key = ciphered[:128]
    iv_ci = ciphered[128:256]
    cipher_txt = ciphered[256:]
    decipherd_key = rsa_dec(key)
    decipherd_iv = rsa_dec(iv_ci)
    
    return cipher_txt, decipherd_key, decipherd_iv

if __name__ == '__main__':
    f = open('exam_test.txt.enc', 'rb')
    d1, d2, d3 = decoded(f)
    a = open('d1.txt', 'wb')
    b = open('d2.txt', 'wb')
    c = open('d3.txt', 'wb')
    a.write(d1)
    b.write(d2)
    c.write(d3)
    a.close()
    b.close()
    c.close()