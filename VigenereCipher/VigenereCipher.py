ALPHABET = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY = 'SECRET'

def vigenere_encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    
    cipher_text = ''
    
    #represents the index of the letters of the key 
    key_index = 0
    
    for char in plain_text:
        index = (ALPHABET.find(char) + ALPHABET.find(key[key_index])) % len(ALPHABET)
        cipher_text = cipher_text + ALPHABET[index]
        
        #increment the key index 
        key_index = key_index + 1
        
        if key_index == len(key):
            key_index = 0
    
    return cipher_text

def vigenere_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()
    
    plain_text = ''
    
    #represents the index of the letters of the key 
    key_index = 0
    
    for char in cipher_text:
        index = (ALPHABET.find(char) - ALPHABET.find(key[key_index])) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]
        
        #increment the key index 
        key_index = key_index + 1
        
        if key_index == len(key):
            key_index = 0
    
    return plain_text

if __name__ == '__main__':
    text = 'Research shows that students who make learning a habit are more likely to reach their goals'
    cipher_message = vigenere_encrypt(text,KEY)
    print(cipher_message)
    print(vigenere_decrypt(cipher_message,KEY))



