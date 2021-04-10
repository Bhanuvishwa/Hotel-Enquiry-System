
def encrypt():
    text = str(input("Enter your plain text:"))
    s = int(input("Enter your shift key:"))
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    print(result)

key = 'abcdefghijklmnopqrstuvwxyz'
def decrypt():
    ciphertext=str(input("Enter the Cipher text:"))
    n=int(input("Enter the Shift key:"))
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    print(result)
    
choice= int(input("Enter your choice [1 for encryption and 2 for decryption] :"))
if(choice==1):
    encrypt()
elif(choice==2):
    decrypt()
else:
    print("Invalid choice")

