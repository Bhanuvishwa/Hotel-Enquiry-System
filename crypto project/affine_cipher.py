# Affine cipher:


def encrypt():
    k1=int(input("enter key1"))
    k2=int(input("enter key2"))
    pt=input("enter plain text")
    ct=""
    for i in range(len(pt)):
        x=pt[i]
        y=ord(x)-ord("a")
        z=(y*k1+k2)%26
        ct+=chr(z+ord("a"))
    print(ct)
    
def modulo_multiplicative_inverse(A):
    """
    Returns multiplicative modulo inverse of A under M, if exists
    Returns -1 if doesn't exist
    """
    # This will iterate from 0 to M-1
    for i in range(0, 26):
        if (A*i) % 26 == 1:
            return i
    return -1
    
def decrypt():
    k1=int(input("enter key1"))
    k2=int(input("enter key2"))
    ct=input("enter cipher text")
    key=modulo_multiplicative_inverse(k1)
    pt=""
    for i in range(len(ct)):
        x=ct[i]
        y=ord(x)-ord("a")
        z=(y-k2)*key%26
        pt+=chr(z+ord("a"))
    print(pt)

print("AFFINE CIPHER press 1. Encryption and 2. Decryption")
r=int(input("enter your choice"))
if(r==1):
    encrypt()
elif(r==2):
    decrypt()
else:
    print("Invalid choice")

