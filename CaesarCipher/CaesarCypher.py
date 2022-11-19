import matplotlib.pyplot as plt

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
KEY = 3

def caesar_encrypt(plain_text):
    
    cipher_text = ''
    plain_text = plain_text.upper()

    for c in plain_text:
        index = ALPHABET.find(c)
        index = (index + KEY) % len(ALPHABET)
        cipher_text = cipher_text + ALPHABET[index]
    
    return cipher_text


def caesar_decrypt(cipher_text):
    
    plain_text = ''
    cipher_text = cipher_text.upper()

    for c in cipher_text:
        index = ALPHABET.find(c)
        index = (index - KEY) % len(ALPHABET)
        plain_text = plain_text + ALPHABET[index]
    
    return plain_text

#brute force
def crack_caesar(cipher_text):
    #we try all the possible key values so the size of the alphabet
    plain_text = ''
    for key in range(len(ALPHABET)):
        for c in cipher_text:
            index = ALPHABET.find(c)
            index = (index - key) % len(ALPHABET)
            plain_text = plain_text + ALPHABET[index]
        print("With key %s, the result is: %s" % (key,plain_text))
        plain_text = ''

#frequency analysis
def grequency_analysis(text):
    #text to analyse
    text = text.upper()

    #use a dictionary to store the letter frequency pair
    letter_frequencies = {}

    #initialize the dictionary
    for letter in ALPHABET:
        letter_frequencies[letter] = 0
    
    for letter in text:
        if letter in ALPHABET:
            letter_frequencies[letter] += 1

    return letter_frequencies

def plot_distribution(frequencies):
    plt.bar(frequencies.keys(), frequencies.values())
    plt.show()

def frequency_caesar_crack(cipher_text):
    freq = grequency_analysis(cipher_text)
    freq = sorted(freq.items(), key = lambda x: x[1], reverse=True)
    print("The possible key value: %s" % (ALPHABET.find(freq[0][0]) - ALPHABET.find('E')))
    

if __name__ == '__main__':
    plain_text = 'DCEHVWCSUDFWLFHCDPRQJCSBWKRQCGHYHORSHUVCLVCWRCDYRLGCLQVWDOOLQJCSDFNDJHVCLQWRCDCJOREDOCLQWHUSUHWHUCHQYLURQPHQWCCBRXCLQVWHDGCXVHCDCSURMHFWCVSHFLILFCYLUWXDOCHQYLURQPHQWCWKDWCFRQWDLQVCDCFRSBCRICDCJOREDOCLQWHUSUHWHUCCRQFHCBRXCDFWLYDWHCWKDWCHQYLURQPHQWCCDQBCSDFNDJHVCBRXCWKHQCLQVWDOOCDUHCLVRODWHGCIURPCRWKHUCHQYLURQPHQWVCCVXFKCLVRODWLRQCUHGXFHVCPDQBCFRPSOLFDWLRQVCWKDWCFDQCDULVHCIURPCFRQIOLFWLQJCSDFNDJHCYHUVLRQVCCWRCFUHDWHCDCYLUWXDOCHQYLURQPHQWCDQGCLQVWDOOCWKHCUHTXLUHGCSDFNDJHVCCHQWHUCWKHCIROORZLQJCFRPPDQGVCDVCDSSURSULDWHCIRUCBRXUCRSHUDWLQJCVBVWHPC'
    frequency_caesar_crack(plain_text)
 
