# RSAEncryptionScript

### Generate RSA keys
```
python gen_key.py
```

### Encrypt message
```
python encrypt.py -k {key} -i {input text file} -o {output text file}
```
Default arguement values are `public_key.pem`, `input.txt`, `output.txt` respectively

### Decrypt message
```
python decrypt.py -k {key} -i {input text file} -o {output text file}
```
Default arguement values are `private_key.pem`, `input.txt`, `output.txt` respectively
