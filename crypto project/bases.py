import base64

def b64():
	message = str(input("enter your message"))
	message_bytes = message.encode('ascii')
	base64_bytes = base64.b64encode(message_bytes)
	base64_message = base64_bytes.decode('ascii')

	print(base64_message)

def b16():
	message = str(input("enter your message"))
	message_bytes = message.encode('ascii')
	base16_bytes = base64.b16encode(message_bytes)
	base16_message = base16_bytes.decode('ascii')

	print(base16_message)

def b32():
	message = str(input("enter your message"))
	message_bytes = message.encode('ascii')
	base32_bytes = base64.b32encode(message_bytes)
	base32_message = base32_bytes.decode('ascii')

	print(base32_message)

def b85():
	message = str(input("enter your message"))
	message_bytes = message.encode('ascii')
	base85_bytes = base64.b85encode(message_bytes)
	base85_message = base85_bytes.decode('ascii')

	print(base85_message)

print(("enter your choice: \n 1.base-16 \n 2.base-32 \n 3.base-85 \n 4.base-64" ))
choice = int(input(" ==> "))

if(choice == 1):
	b16()
elif(choice==2):
	b32()
elif(choice==3):
	b85()
elif(choice==4):
	b64()
else:
	print("invalid choice")


