# VIGNERE CIPHER

def encrypt():
    pt=str(input("enter plaintext"))
    key=str(input("enter key"))
    k=[]
    ct=""
    for i in range(len(key)):
        x=ord(key[i])-ord("a")
        k.append(x)
    #print(k)
    p=0
    for j in range(len(pt)):
        y=ord(pt[j])-ord("a")
        #print(y)
        z=(y+k[p])%26
        #print(k[p])
        #print(z)
        ct+=chr(z+ord("a"))
        #print(p)
        if(p+1>=len(k)):
            p=0
        else:
            p+=1
            #print("hi")
    print(ct)
     

def decrypt():
    ct=str(input("enter ciphertext"))
    key=str(input("enter key"))
    k=[]
    pt=""
    for i in range(len(key)):
        x=ord(key[i])-ord("a")
        k.append(x)
    #print(k)
    p=0
    for j in range(len(ct)):
        #print("hello")
        y=ord(ct[j])-ord("a")
        #print(y)
        z=(y-k[p])%26
        #print(k[p])
        #print(z)
        pt+=chr(z+ord("a"))
        #print(p)
        if(p+1>=len(k)):
            p=0
        else:
            p+=1
            #print("hi")
    print(pt)
    

   
print("VIGNERE CIPHER press 1. Encryption and 2. Decryption")
r=int(input("enter your choice"))
if(r==1):
    encrypt()
elif(r==2):
    decrypt()
else:
    print("Invalid choice")