import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z']


print(art.logo)
restart = 'yes'
while restart != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    while shift > 26:
        shift  = shift % 26
    def ceaser(start_text, shift_amount, cipher_direction):
        end_text = ''
        new_position = 0
        for letter in start_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                if cipher_direction == "encode":
                    new_position = position + shift_amount
                    end_text += alphabet[new_position]
                elif cipher_direction == "decode":
                    new_position = position - shift_amount
                    end_text += alphabet[new_position]
            else:
                end_text += letter        
        print(f"The {cipher_direction}ed text is {end_text}")

    ceaser(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'")
