from Crypto.PublicKey import RSA

#Generate a public/ private key pair
new_key = RSA.generate(2048)

#The private key in PEM format
private_key = new_key.exportKey("PEM")

#The public key in PEM Format
public_key = new_key.publickey().exportKey("PEM")

with open("public_key.pem", "wb") as f:
    f.write(public_key)

with open("private_key.pem", "wb") as f:
    f.write(private_key)