# Convertir el ejercicio de encriptacion, al sistema binario
# Las letras en programacion son numeros.
from functools import reduce
BITS_CHAR = 8
BINARY_CODE = [128,64,32,16,8,4,2,1]
def decipher(message):
    characters_total = len(message)//BITS_CHAR
    characters_binary_array = []
    i = 0
    j = 1
    while j <= characters_total:
        char_binary = list(message[i:(j*BITS_CHAR)])
        i +=8
        j +=1
        characters_binary_array.append(char_binary)
    characters_int = decoder_int(characters_binary_array)
    string_message = decoder(characters_int)
    return string_message

def decoder(character_int):
    string_array = []
    for integer_char in character_int:
        character_transform = chr(integer_char)
        string_array.append(character_transform)
    decypher_message = ''.join(string_array)
    return decypher_message


def decoder_int(characters_binary_array):
    char_binary_to_int =[]
    char_int = []
    for binary_char in characters_binary_array:
        binary_to_int = []
        idx = 0
        for binary in binary_char:
            if binary == '1':
                binary_to_int.append(BINARY_CODE[idx])
                idx += 1
            else:
                binary_to_int.append(0)
                idx +=1
        char_int = reduce(lambda a , b: a + b, binary_to_int)        
        char_binary_to_int.append(char_int)        
    return char_binary_to_int


def cypher(message):
    message_array = list(message) #verificar esta variable
    message_int_array = []
    for character in message:
        char_transform = ord(character)
        message_int_array.append(char_transform)
    cypher_message_array = integer_to_binary(message_int_array)
    print(cypher_message_array)
    # cypher_message_binary = ''.join(cypher_message_array)
    cypher_message_binary = binary_to_string(cypher_message_array)
    return cypher_message_binary

def integer_to_binary(message_int):
    
    binary_string_array = []
    binary_code = BINARY_CODE[::-1]
    for character_int in message_int:
        char_binary = []
        idx = len(binary_code) - 1
        char_value = character_int
        while idx >= 0:
            if char_value >= binary_code[idx]:
                char_value -= binary_code[idx]
                idx -= 1
                char_binary.append(1)
            elif char_value < binary_code[idx]:
                idx -= 1
                char_binary.append(0)
        binary_string_array.append(char_binary)   
    return binary_string_array            

# Function that change each character transformed in binary array to in a string.
def binary_to_string(cypher_message_array):
    binary_string = []
    for binary_int_array in cypher_message_array:
        sub_arrays = []
        for digit in binary_int_array:
            digit_string = str(digit)
            sub_arrays.append(digit_string)
        binary_string.append(''.join(sub_arrays))
    return ''.join(binary_string)

def run():
    while True:
        command = str(input('''---*---*---*---*---*---*---
            Bienvenido a criptografia.¿Que deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
            '''))
        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)
        elif command == 'd':
            message = str(input('Escribe tu mensaje cifrado: '))
            decypher_message = decipher(message)
            print(decypher_message)
        elif command == 's':
            exit()
        else:
            print('Comando no encontrado')




if __name__ == '__main__':
    print('M E N S A J E S  C I F R A D O S')
    run()
