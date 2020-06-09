# import os
# root_dir = os.getcwd()
# print(root_dir)
# for root,folders,files in os.walk(root_dir):
#     for filename in files:
#         print("root: ",root)
#         print("folders: ", folders)
#         print("files: ", files)
#         print("filename: ", filename)

# import multiprocessing
# def count1():
#     for i in range(10):
#         print("count1: ",i)
# def count2():
#     for i in range(10):
#         print("count2: ",i)
# if __name__=="__main__":
#     worker1= multiprocessing.Process(target=count1())
#     worker2=multiprocessing.Process(target=count2())
#     worker1.start()
#     worker2.start()
#     worker1.join()
#     worker2.join()

# #heapq
# import heapq as h
#
# numbers = [100,45,67,23,89,54,12,2,7,121,567,44,78,1,9,87]
# #print(h.nlargest(6,numbers))
# print(numbers)
# h.heapify(numbers)
# print(numbers)
# h.heappop(numbers)
# print(numbers)
# h.heapify(numbers)
# print(numbers)

# #advanced password generation
# from string import punctuation , ascii_letters ,digits
# symbol = punctuation + ascii_letters + digits
# import random
# secured_pass = random.SystemRandom()
# passwrd = "".join(secured_pass.choice(symbol) for i in range(10))
# print(passwrd)
import base64
import os

from cryptography.fernet import Fernet
import sys

argumentList = sys.argv
#print(argumentList)
message = argumentList[2].encode()
#For Generating and storing key
#key = Fernet.generate_key()
# file = open('key.key', 'wb')
# file.write(key) # The key is type bytes still
# file.close()

# file = open('key.key', 'rb')
# key = file.read() # The key will be type bytes
# file.close()
# f = Fernet(key)
key=base64.urlsafe_b64encode(os.urandom(32))
f=Fernet(key)
try :
    for i in argumentList:
        if i == "encrypt":
            encrypted = f.encrypt(message)
            print(encrypted.decode())
        elif i == "decrypt":
            decrypted = f.decrypt(message)
            print(decrypted.decode())
        else:
            continue
except Exception:
    print(" error occured ")




