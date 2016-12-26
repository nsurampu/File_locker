import os
import PyPDF2

def pdfLock():
    filename = raw_input("Enter file name with extension: ")
    user_pass = raw_input("Enter password to be set: ")
    owner_pass = user_pass
    input_file = filename
    output_file = "temp"

    output = PyPDF2.PdfFileWriter()

    input_stream = PyPDF2.PdfFileReader(open(input_file, "rb"))

    for i in range(0, input_stream.getNumPages()):
	output.addPage(inputstream.getPage(i))

    outputStream = open(output_file, "wb")

    output.encrypt(user_pass, owner_pass, use_128bit = True)
    output.write(outputStream)
    outputStream.close()
    os.rename(output_file, input_file)
    print "Lock applied successfully"

def txtLock():
    txtChoice = raw_input("Do you wish to encrypt or decrypt your file?: ")
    txtChoice = txtChoice.lower()

    if txtChoice == "encrypt":
	txtEncrypt()
    elif txtChoice == "decrypt":
	txtDecrypt()
    else:
	print("Invalid choice")

def txtEncrypt():
    input_file = raw_input("Enter name of text file to be encrypted with extension: ")
    key = int(raw_input("Enter encryption key: "))

    plain_file = open(input_file, "r+")

    enc_file = open("encrypted_" + input_file, "w+")

    plain = plain_file.read()
    plain = plain.upper()

    for letter in plain:
        enc_file.write(str(ord(letter) + key))

    enc_file.close()
  
    print "Encrypted successfully"
    choice = raw_input("Do you wish to keep the unencrypted file?y/n: ")
    choice = choice.lower()

    if choice == "n":
	os.remove(input_file)

def txtDecrypt():
    efile = raw_input("Enter name of text file to be decrypted with extension: ")
    key = int(raw_input("Enter encryption key to decrypt: "))

    enc_file = open(efile, "r+")

    temp_file = open("temp.txt", "w+")

    name = efile.split("_")[1]

    dec_file = open("decrypted_" + name, "w+")

    cipher = enc_file.read()

    i = 1

    for letter in cipher:
        temp_file.write(letter)
        if (i % 2 == 0):
            temp_file.write(".")
        i += 1

    temp_file.close()

    temp_file = open("temp.txt", "r+")

    cipher = temp_file.read()

    cipher = cipher.split(".")
    cipher.pop()
    cipher = [(int(x) - key) for x in cipher]

    for item in cipher:
        dec_file.write(str(chr(item)))

    temp_file.close()
    enc_file.close()

    os.remove("temp.txt")
    os.remove(efile)
    print "Decrypted successfully"


choice = raw_input("Which file type do you wish to secure- pdf or txt?: ")
choice = choice.lower()

if choice == "pdf":
    pdfLock()
elif choice == "txt":
    txtLock()
else:
    print "The current file type is currently not suppported by the application"
