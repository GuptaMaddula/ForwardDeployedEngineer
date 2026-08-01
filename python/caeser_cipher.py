alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").upper()
text=input("Type your message:\n").upper()
shift=int(input("Type the shift number:\n"))

def encrypt(text,shift):
    cipher_text=""
    for char in text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift)
            if new_position>25:
                new_position=new_position-26
                cipher_text+=alphabet[new_position]
            else:
                cipher_text+=alphabet[new_position]
            
    print(f"The encoded text is {cipher_text}")

def decrypt(text,shift):
    decipher_text=""
    for char in text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position-shift)
            if new_position<0:
                new_position=new_position+26
                decipher_text+=alphabet[new_position]
            else:
                decipher_text+=alphabet[new_position]
            
    print(f"The decoded text is {decipher_text}")


#decrypt(text,shift)