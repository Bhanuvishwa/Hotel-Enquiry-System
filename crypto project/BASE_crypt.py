from banner import *
import os
print("""
[1] - BASE FORMATS
[2] - CEASER CIPHER
[3] - VIGNERE CIPHER
[4] - MULTIPLICATIVE CIPHER
[5] - AFFINE CIPHER
[6] - SIMPLE SUBSTITUTION CIPHER
[7] - ONE TIME PAD
[8] - AUTOKEY CIPHER
[9] - HILL CIPHER
[10]- TRANSPOSITION CIPHER 
[0] - Exit
""")
check = int(input("==> "))
if check == 1:
    os.system('CLS')
    import bases
elif check == 2:
    #banner()
    print("""
[1] - ROT-5
[2] - ROT-13
[0] - Exit
	""")
    z = int(input("==> "))
    if z == 1:
        os.system('CLS')
        import ceaser_rot5
    elif z == 2:
        os.system('CLS')
        import ceaser_rot13
    else:
        exit()

elif check == 3:
    os.system('CLS')
    import vignere_cipher
elif check == 4:
    os.system('CLS')
    import multipicative_Cipher
elif check == 5:
    os.system('CLS')
    import affine_cipher
elif check == 6:
    os.system('CLS')
    import simple_Substitution
elif check == 7:
    os.system('CLS')
    import OTP
elif check == 8:
    os.system('CLS')
    import autokey_cipher
elif check == 9:
    os.system('CLS')
    import hill
elif check == 10:
    os.system('CLS')
    import transposition_cipher
else:
     exit()