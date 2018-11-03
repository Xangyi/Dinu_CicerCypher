L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = 3


plaintext = "THE  DIE  HAS BEEN  CAST"


# encipher
ciphertext = ""
for c in plaintext.upper():
    if c.isalpha(): ciphertext =ciphertext + I2L[ (L2I[c] + key)%26 ]
    else: ciphertext += c

# decipher
plaintext2 = ""
for c in ciphertext.upper():
    if c.isalpha(): plaintext2 =plaintext2 + I2L[ (L2I[c] - key)%26 ]
    else: plaintext2 += c

print(plaintext)
print(ciphertext)
print(plaintext2)
