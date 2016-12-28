#An application that can be used to lock pdf files and encrypt txt files
#Text file encryption uses ARC4 encryption, which is stream encryption

import os
import PyPDF2
from Crypto.Cipher import ARC4

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
    key = raw_input("Enter encryption key: ")
    
    ifile = open(input_file, "r+")
    plain = ifile.read()
    ifile.close()
    ofile = open(input_file, "w+")

    obj = ARC4.new(key)
    cipher = obj.encrypt(plain)
    ofile.write(cipher)
    ofile.close()
    print "Encrypted successfully"

def txtDecrypt():
    efile = raw_input("Enter name of text file to be decrypted with extension: ")
    key = raw_input("Enter encryption key to decrypt: ")

    ifile = open(efile, "r+")
    cipher = ifile.read()
    ifile.close()
    ofile = open(efile, "w+")

    obj = ARC4.new(key)
    plain = obj.decrypt(cipher)
    ofile.write(plain)
    ofile.close()
    print "Decrypted successfully"


choice = raw_input("Which file type do you wish to secure- pdf or txt?: ")
choice = choice.lower()

if choice == "pdf":
    pdfLock()
elif choice == "txt":
    txtLock()
else:
    print "The current file type is currently not suppported by the application"
