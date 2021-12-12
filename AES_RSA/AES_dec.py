import crypto
import sys
sys.modules['Crypto'] = crypto
from crypto.Cipher import AES


def aes_dec(ciphertext, key, iv):
    aes = AES.new(key, AES.MODE_CBC, iv)
    decmsg = aes.decrypt(ciphertext)

    header = decmsg[:16].decode()
    fillersize = int(header.split('#') [0])
    if fillersize != 0:
        decmsg = decmsg[16:-fillersize]
    else:
        decmsg = decmsg[16:]

    return decmsg

if __name__ == '__main__':
    a = open('d1.txt', 'rb')
    b = open('d2.txt', 'rb')
    c = open('d3.txt', 'rb')
    cipher_txt = a.read()
    decipherd_key = b.read()
    decipherd_iv = c.read()
    decmsg = aes_dec(cipher_txt, decipherd_key, decipherd_iv)
    dec_result = decmsg.decode()
    
    f = open('plain_text.txt', 'w')
    f.write(dec_result)
    f.close()
    