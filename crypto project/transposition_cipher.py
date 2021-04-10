# Transposition cipher:
def encrypt():
    pt=input("enter the plaintext ")
    print("Make sure start you key doesn't have index:0 ")
    ke=str(input("enter the encryption key "))
    l=0
    o=0
    key=''
    for o in range(len(ke)):
        l=int(ke[o])
        l-=1
        key+=str(l)
        
    a=len(key)
    p=[]
    len_pt=len(pt)
    q=0
    b=''
    for i in range((len_pt//len(key))):
        b=''
        #print(q,a)
        b+=pt[q:a]
        q=q+len(key)
        a=a+len(key)
        p.append(b)

    a=a-len(key)
    c=len(pt)-a
    r=""
    #print(a,c,0)
    if(c!=0):
        f=pt[a:len(pt)]
        if(len(f)<len(key)):
            t=len(key)-len(f)
            for i in range(t):
                r+="x"
            f+=r
        p.append(f)
#print(a)
    print(p)
    g=""
    ct=""
    for l in range(len(key)):
        d=key[l]
        s=int(d)
    #print(s)
    #print(type(d))
        for m in range(len(p)):
            g=p[m]
            e=g[s]
        #print(e)
            ct+=e
    print(ct)
    
def decrypt():
    ct=input("enter the ciphertext ")
    print("Make sure start you key index from 0")
    ke=str(input("enter the decryption key "))
    l=0
    o=0
    key=''
    for o in range(len(ke)):
        l=int(ke[o])
        l-=1
        key+=str(l)

    a=len(key)
    p=[]
    len_ct=len(ct)
    q=0
    b=''
    for i in range((len_ct//len(key))):
        b=''
        #print(q,a)
        b+=ct[q:a]
        q=q+len(key)
        a=a+len(key)
        p.append(b)
    a=a-len(key)
    c=len(ct)-a
    r=""
    #print(a,c,0)
    if(c!=0):
        f=ct[a:len(ct)]
        if(len(f)<len(key)):
            t=len(key)-len(f)
            for i in range(t):
                r+="x"
            f+=r
        p.append(f)
    print(p)
    pt=''
    for j in range(len(p)):
        x=p[j]
        print(x)
        for k in range(len(key)):
            h=int(key[k])
            #print(h)
            g=x[h]
            pt+=g
            #print(x,h,g,e)
        print(pt)
            
        


print("TRANSPOSITION CIPHER press 1. Encryption and 2. Decryption")
r=int(input("enter your choice "))
if(r==1):
    encrypt()
elif(r==2):
    decrypt()
else:
    print("Invalid choice")
    
    
    