alphabet=['a','b','c','d','e','f','g','h',
          'i','j','k','l','m','n','o','p','q','r','s','t','u'
          'v','w','x','y','z','a','b','c','d','e','f','g','h',
          'i','j','k','l','m','n','o','p','q','r','s','t','u',
          'v','w','x','y','z']
direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text=input("Type your message:\n").lower()
shift=int(input("Type shift number:\n"))
shift=shift%26
def caesar(start_text,shift_amount,cypher_direction):
    end_text=""
    if cypher_direction == 'decode':
        shift_amount*=-1
    elif cypher_direction == 'encode':
        shift_amount*=1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f'The {cypher_direction}d text is {end_text} ')
caesar(start_text=text,shift_amount=shift,cypher_direction=direction)


