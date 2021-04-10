import hashlib
from time import time


characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
              'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
              'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
              'Y', 'Z']
#             ['!', "'", '#', '$', '%', '&', '(', ')',
#             '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
#             '>', '?', '@', '[', ']', '^', '_', '`', '{', '|',
#             '}', '~', '"']

built_password = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']  # 16


def decorator(ugly_list):
    return "".join(ugly_list)


# Fastest < Slowest / Weakest < Strongest
# blake2s < md5 < sha1 < sha224 < sha256 < blake2b < sha384 < sha3_224 < sha512 < sha3_256 < sha3_384 < sha3_512
def encrypt_password(password_str, encryption_type_str):
    if encryption_type_str == "md5":
        return hashlib.md5(password_str.encode()).hexdigest()
    elif encryption_type_str == "sha1":
        return hashlib.sha1(password_str.encode()).hexdigest()
    elif encryption_type_str == "sha224":
        return hashlib.sha224(password_str.encode()).hexdigest()
    elif encryption_type_str == "sha256":
        return hashlib.sha256(password_str.encode()).hexdigest()
    elif encryption_type_str == "sha384":
        return hashlib.sha384(password_str.encode()).hexdigest()
    elif encryption_type_str == "sha512":
        return hashlib.sha512(password_str.encode()).hexdigest()
    elif encryption_type_str == "blake2b":
        return hashlib.blake2b(password_str.encode()).hexdigest()
    elif encryption_type_str == "blake2s":
        return hashlib.blake2s(password_str.encode()).hexdigest()
    elif encryption_type_str == "sha3_224":
        return hashlib.sha3_224(password_str.encode()).hexdigest()
    elif encryption_type_str == "sha3_256":
        return hashlib.sha3_256(password_str.encode()).hexdigest()
    elif encryption_type_str == "sha3_384":
        return hashlib.sha3_384(password_str.encode()).hexdigest()
    elif encryption_type_str == "sha3_512":
        return hashlib.sha3_512(password_str.encode()).hexdigest()
    else:
        raise TypeError("NO DISPONIBLE")


def test_password(password_to_test_str):
    global PASSWORD_HASH
    if PASSWORD_HASH == encrypt_password(password_to_test_str, ENCRYPTION_INPUT):
        return True


def decrypt(letters_amount_int):
    global built_password

    for letter in range(len(characters)):
        built_password[letters_amount_int - 1] = characters[letter]
        if letters_amount_int > 1:
            guess = decrypt(letters_amount_int - 1)
            if guess:
                return guess
        elif test_password(decorator(built_password)):
            return decorator(built_password)


# Start

PASSWORD_INPUT = input("Introduce una contraseña: ")
ENCRYPTION_INPUT = input("Elige una encriptación: ")
PASSWORD_HASH = encrypt_password(PASSWORD_INPUT, ENCRYPTION_INPUT)
print(f'El HASH ({ENCRYPTION_INPUT}) de "{PASSWORD_INPUT}" es: {PASSWORD_HASH}\n')

starting_time = time()
n = 1
while True:
    print(f"Probando con {n} letras", end="\r")
    returned = decrypt(n)
    try:
        print('Se ha encontrado el HASH de ' + returned + f' en {round(time() - starting_time, 2)} segundos')
        break
    except TypeError:
        n += 1
