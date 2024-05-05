import random

def generate_key():
    qwerty = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()"
    key = list(qwerty)
    random.shuffle(key)
    return "".join(key)

def qwerty_encrypt(plaintext, key):
    qwerty = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()"
    ciphertext = ""
    for char in plaintext:
        if char.isascii():
            index = qwerty.index(char.lower())
            ciphertext += key[index]
        else:
            ciphertext += char
    return ciphertext

def qwerty_decrypt(ciphertext, key):
    qwerty = "qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()"
    plaintext = ""
    for char in ciphertext:
        if char.isascii():
            index = key.index(char.lower())
            plaintext += qwerty[index]
        else:
            plaintext += char
    return plaintext

key = generate_key()
plaintext = input("Write the text you want to encrypt (without spaces): ")
ciphertext = qwerty_encrypt(plaintext, key)
print("Original Text: ", plaintext)
print("Encripted Text: ", ciphertext)
print("Desencripted Text: ", qwerty_decrypt(ciphertext, key))
