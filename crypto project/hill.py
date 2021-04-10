import numpy as np


def encrypt(messages, key, n):
    messages_list = [(ord(i) - ord('a') + 1) for i in messages]
    messages_list = np.reshape(messages_list, (n, n))
    key = np.reshape(key, (n, n))
    outputs_list = []
    for i in messages_list:
        outputs_list.append(np.dot(key, i) % 26)

    outputs_list = np.reshape(outputs_list, (1, n ** 2))[0]
    o = [chr(i + ord('a')) for i in outputs_list]
    print(''.join(o))


def isPerfectSquare(x):
    sr = np.sqrt(x)
    return ((sr - np.floor(sr)) == 0), np.ceil(sr - np.floor(sr))


def decrypt(messages_decdecrypted, key, n):
    messages_decdecrypted_list = [(ord(i) - ord('a')) for i in messages_decdecrypted]
    messages_list = np.reshape(messages_decdecrypted_list, (n, n))
    print(messages_decdecrypted_list)
    key = np.reshape(key, (n, n))
    # print(key)
    key = np.linalg.inv(key) % 26
    print(key)
    outputs_list = []
    for i in messages_list:
        outputs_list.append(np.dot(key, i) % 26)

    outputs_list = np.reshape(outputs_list, (1, n ** 2))[0]
    print(outputs_list)
    o = [chr(round(i) + ord('a')-1) for i in outputs_list]
    print(''.join(o))



choice=int(input("select\n 1 for encrypt\n 2 for decrypt"))
if choice==1:
    messages = input("enter the message: ")
    key = list(map(int, input("in 1xn spaces array: ").split(" ")))
    n=int(np.sqrt(len(key)))
    encrypt(messages,key,n)
else:
    messages = input("enter the encrypted message: ")
    key = list(map(int, input("in 1xn spaces array: ").split(" ")))
    n=int(np.sqrt(len(key)))
    decrypt(messages, key, n)

# messages = 'hwkb'#input('message')
# conditions = isPerfectSquare(len(key))
# print(conditions)
# decrypt(messages, key, n=2)
