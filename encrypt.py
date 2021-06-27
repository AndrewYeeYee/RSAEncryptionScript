from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--key', dest='key', action='store', type=str, default='', help='filename for key for encryption')
parser.add_argument('-t', '--text', dest='text', action='store', type=str, default='', help='plaintext file to encrypt')
parser.add_argument('-o', '--output', dest='out', action='store', type=str, default='output.txt', help='output filename')

args = parser.parse_args()

with open(args.key, 'r') as f:
    rsa_key = RSA.importKey(f.read())

cipher = PKCS1_OAEP.new(rsa_key)

with open(args.text, 'r') as f:
    text = f.read()

with open(args.out, 'wb') as f:
    f.write(cipher.encrypt(text.encode()))