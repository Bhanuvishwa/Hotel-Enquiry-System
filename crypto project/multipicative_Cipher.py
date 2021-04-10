# Multiplicative cipher:

def encrypt():
    pt=input("enter the plaintext ")
    key=int(input("enter key "))

    pt=pt.replace(' ','')
    a=""
    for i in range(len(pt)):
        x=pt[i]
        y=ord(x)-ord("a")
        z=(y*key%26)
        p=z+ord("a")
        a += chr(p)
    print(a)

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
    ct=str(input("enter the ciphertext "))   
    key=int(input("enter key "))
    k=modulo_multiplicative_inverse(key)
    a=""
    for i in range(len(ct)):
        x=ct[i]
        y=ord(x)-ord("a")
        z=(y*k%26)
        p=z+ord("a")
        a += chr(p)
    print(a)
    
print("MULTIPLICATIVE CIPHER press 1. Encryption and 2. Decryption")
r=int(input("enter your choice \n==>"))
if(r==1):
    encrypt()
elif(r==2):
    decrypt()
else:
    print("Invalid choice")
