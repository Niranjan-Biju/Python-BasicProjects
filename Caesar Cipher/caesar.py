alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo

def caesar(original_text,shift_amount,encode_or_decode):
    cipher_text=""
    if encode_or_decode=="decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            pos=(alphabet.index(letter)+shift_amount)%26
            cipher_text+=alphabet[pos]
        else:
            cipher_text+=letter
    print(f"The {encode_or_decode}d word is : " + cipher_text)

condition="yes"
while condition=="yes":
    print(logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text,shift,direction)
    
    condition=input("Would you like to continue? Yes or No.").lower()
