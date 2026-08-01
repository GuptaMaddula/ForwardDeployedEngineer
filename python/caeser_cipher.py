alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

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


should_continue=True

while should_continue:
    direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").upper()
    if direction!="ENCODE" and direction!="DECODE":
        print("Invalid input. Please type 'encode' or 'decode'.")  
    
      
    elif direction=="DECODE":
        text=input("Type your message:\n").upper()
        shift=int(input("Type the shift number:\n"))
        decrypt(text,shift)
    else:
        text=input("Type your message:\n").upper()
        shift=int(input("Type the shift number:\n"))
        encrypt(text,shift)
    restart=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart=="no":
        should_continue=False
        print("Goodbye!")





