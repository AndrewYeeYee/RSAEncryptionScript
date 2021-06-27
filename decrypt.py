from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--key', dest='key', action='store', type=str, default='private_key.pem', help='filename for key')
parser.add_argument('-i', '--input', dest='input', action='store', type=str, default='input.txt', help='encrypted input filename to decrypt')
parser.add_argument('-o', '--output', dest='output', action='store', type=str, default='output.txt', help='plaintext output filename')

args = parser.parse_args()

with open(args.key, 'r') as f:
    rsa_key = RSA.importKey(f.read())

cipher = PKCS1_OAEP.new(rsa_key)

with open(args.input, 'rb') as f:
    ciphertext = f.read()

with open(args.output, 'wb') as f:
    f.write(cipher.decrypt(ciphertext))