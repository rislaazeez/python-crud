# from Crypto.Cipher import DES
#
# key = 'abcdefgh'
#
# def pad(text):
#     while len(text) % 8 != 0:
#         text += ' '
#     return text
#
#
# des = DES.new(key.encode(), DES.MODE_ECB)
# text = 'Python rocks!'
# padded_text = pad(text)
# encrypted_text = des.encrypt(text.encode())
# print(encrypted_text.decode())

import base64 , sys

def encrypt(message):
                encoded_data = base64.b64encode(message.encode())
                print(encoded_data.decode())
def decrypt(message):
                decoded_data = base64.b64decode(message.encode)
                print(decoded_data.decode())

if __name__ == "__main__":
    argumentList = sys.argv
    # print(argumentList)
    message = argumentList[4]
    encrypt(message)
    decrypt(message)