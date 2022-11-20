from random import randint

ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def encrypt(text,key):
    text = text.upper()
    cipher_text = ''
    
    for index, char in enumerate(text):
        #value with which we shift the given letter
        key_index = key[index]
        #the given letter in the plain text
        char_index = ALPHABET.find(char)
        cipher_text += ALPHABET[(char_index + key_index) % len(ALPHABET)]
        
    return cipher_text
    
def decrypt(cipher_text,key):
    plain = ''
    
    for index, char in enumerate(cipher_text):
        key_index = key[index]
        char_index = ALPHABET.find(char)
        plain += ALPHABET[(char_index - key_index) % len(ALPHABET)]
    
    return plain

def random_sequence(text):
    random = []
    
    for _ in range(len(text)):
        random.append(randint(0, len(ALPHABET) - 1))
    
    return random

if __name__ == '__main__':
    message = 'Research shows that students who make learning a habit are more likely to reach their goals'
    seq = random_sequence(message)
    print('Original message: %s' % message.upper())
    cipher = encrypt(message,seq)
    print('Encrypted message: %s' % cipher)
    decrypted_message = decrypt(cipher,seq)
    print('Decrypted message: %s' % decrypted_message)