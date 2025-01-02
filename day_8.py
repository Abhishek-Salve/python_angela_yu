import string

# def greet(name):
#     print("What")
#     print("is")
#     print("up")
#     print(name)
#
# greet("Abhishek")
# # greet()
# greet()

# def life_in_weeks(curr_age):
#     years_left = 90-curr_age
#     weeks_left = years_left * 52
#     print(f"You have {weeks_left} weeks left.")
#
# life_in_weeks(20)

# def greet_3(name, location):
#     print(f"Hello {name}")
#     print(f"How is it in {location}")
#
# greet_3(location="Bangalore", name="A")
# greet_3(name="A", location="Bangalore")


# true_total = 0
# love_total = 0
#
#
# def calculate_love_score(name1="Angela Yu", name2="Jack Bauer", true_total=true_total, love_total=love_total):
#     true_list = ["T", "R", "U", "E"]
#     love_list = ["L", "O", "V", "E"]
#
#     for char in true_list:
#         for letter1 in name1:
#             if char.lower() == letter1.lower():
#                 true_total += 1
#
#         for letter2 in name2:
#             if char.lower() == letter2.lower():
#                 true_total += 1
#
#     for char in love_list:
#         for letter1 in name1:
#             if char.lower() == letter1.lower():
#                 love_total += 1
#
#         for letter2 in name2:
#             if char.lower() == letter2.lower():
#                 love_total += 1
#
#     return int(str(true_total) + str(love_total))
#
#
# print(calculate_love_score(true_total=true_total, love_total=love_total))



# List of lowercase letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# alphabet = list(string.ascii_lowercase)
print(alphabet)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type your shift amount:\n"))

# print(alphabet.index('c'))

def encrypt(input_text, shift_value):
    encrypted_word = ''
    for letter in input_text:
        original_index = alphabet.index(letter)
        shifted_pos = original_index + shift_value
        if  shifted_pos > len(alphabet):
            wrap_index = shifted_pos - len(alphabet)
            encrypted_word += alphabet[wrap_index]
        else:
            encrypted_word += alphabet[shifted_pos]

    return encrypted_word

# encrypt_word = encrypt(input_text=text, shift_value=shift)
# print(encrypt_word)

def decrypt(input_text, shift_value):
    decrypted_word = ''
    for letter in input_text:
        original_index = alphabet.index(letter)
        shifted_pos = original_index - shift_value
        if  shifted_pos < 0:
            wrap_index = len(alphabet) + shifted_pos
            decrypted_word += alphabet[wrap_index]
        else:
            decrypted_word += alphabet[shifted_pos]

    return decrypted_word


# decrypt_word = decrypt(input_text=text, shift_value=shift)
# print(decrypt_word)

def caesar(input_text, shift_value):
    coded_word = ''
    for letter in input_text:
        original_index = alphabet.index(letter)
        if direction == 'encode':
            shifted_pos = original_index + shift_value
        elif direction == 'decode':
            shifted_pos = original_index - shift_value
        else:
            print('wrong word was typed for encode/decode')
        if  shifted_pos > len(alphabet):
            wrap_index = shifted_pos - len(alphabet)
            coded_word += alphabet[wrap_index]
        elif  shifted_pos < 0:
            wrap_index = len(alphabet) + shifted_pos
            coded_word += alphabet[wrap_index]
        else:
            coded_word += alphabet[shifted_pos]
    return coded_word

cipher_word = caesar(input_text=text, shift_value=shift)
print(cipher_word)