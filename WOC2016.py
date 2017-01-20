#An application to lock pdf files and encrypt txt files
#This application has been written as a part of Winter Of Code 2016 of BITS Pilani-Hyderabad Campus
#Author: Naren, Mentor: Nischay

import os
import base64
import PyPDF2
from Crypto.Cipher import AES
from Crypto import Random
from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)   #This will ensure that the text in the files are mutiples of 16
unpad = lambda s: s [:-ord(s[len(s) - 1:])]   #This will remove the 'pads' that were added to the original text while encrypting

def pdfLock(event):   #This function takes care of locking the pdf files and setting a password to them
    try:
        filename = fileEntry.get()
        user_pass = passEntry.get()
        owner_pass = user_pass
        input_file = filename
        output_file = "temp"   #Creating a temporary pdf file where all the contents of the original file will be copied to. This will be the one that will be locked

        output = PyPDF2.PdfFileWriter()
        inputf = open(input_file, "rb")

        input_stream = PyPDF2.PdfFileReader(inputf)

        for i in range(0, input_stream.getNumPages()):  #Reading the pages in the pdf file and adding them one by one to the 'temp' file
            output.addPage(input_stream.getPage(i))

            outputStream = open(output_file, "wb")

        output.encrypt(user_pass, owner_pass, use_128bit = True)   #This will set the password of the lock using 128 bit encryption
        output.write(outputStream)
        outputStream.close()
        inputf.close()
        os.remove(input_file)   #Need to remove the file first to rename the 'temp' file, else won't work on Windows
        os.rename(output_file, input_file)
        statusPop()
        disabler()
    except Exception as e:
        showerror("Error", e)
        disabler()

def txtEncrypt(event):   #This takes care of the txt files encryption
    try:
        input_file = fileEntry.get()
        key = keyEntry.get()

        ifile = open(input_file, "r+")
        plain = ifile.read()
        ifile.close()
        ofile = open(input_file, "w+")
        plain = pad(plain)
        IV = Random.new().read(AES.block_size)   #Creating a random initialization vector
        cipher = AES.new(key, AES.MODE_CBC, IV)   #Creating the cipher for encrypting the text
        encrypted = base64.b64encode(IV + cipher.encrypt(plain))   #Encrypting the text
        ofile.write(encrypted)
        ofile.close()
        statusPop()
        disabler()
    except Exception as e:
        showerror("Error", e)
        disabler()

def txtDecrypt(event):   #This takes care of the txt files decryption
    try:
        efile = fileEntry.get()
        key = keyEntry.get()

        ifile = open(efile, "r+")
        enc  = ifile.read()
        ifile.close()
        ofile = open(efile, "w+")
        enc = base64.b64decode(enc)
        IV = enc[:16]   #Extracting the IV from the encrypted text
        cipher = AES.new(key, AES.MODE_CBC, IV)   #Creating the cipher for decrypting text
        decrypted = unpad(cipher.decrypt(enc[16:]))   #Decrypting the text
        ofile.write(decrypted)
        ofile.close()
        statusPop()
        disabler()
    except Exception as e:
        showerror("Error", e)
        disabler()

def enabler(event):   #Enables the various GUI components
    try:
        text = fileEntry.get()
        ext = text.split(".")[1]

        if(ext == "pdf"):
            lockButton.config(state = NORMAL)
            lockButton.bind("<Button-1>", pdfLock)
        elif(ext == "txt"):
            encryptButton.config(state = NORMAL)
            decryptButton.config(state = NORMAL)
            encryptButton.bind("<Button-1>", txtEncrypt)
            decryptButton.bind("<Button-1>", txtDecrypt)
        else:

            showwarning("Warning", "The file type is currently not supported.\nOnly pdf and txt files are allowed")
    except Exception as e:
        showerror("Error", e)

def disabler():   #Disables the various GUI components
    lockButton.config(state = DISABLED)
    encryptButton.config(state = DISABLED)
    decryptButton.config(state = DISABLED)
    lockButton.unbind("<Button-1>")
    encryptButton.unbind("<Button-1>")
    decryptButton.unbind("<Button-1>")
    passEntry.delete(0, END)
    keyEntry.delete(0, END)

def aboutPop():
    showinfo("About", "Author : Naren Surampudi\nVersion : 2.1")

def statusPop():
    showinfo("Message", "Process completed successfully")

def fileTray():
    tray = askopenfilename(parent = root, title = "Choose file")
    fileEntry.delete(0, END)
    fileEntry.insert(0, tray)

     
#The GUI for the application

root = Tk()
root.geometry("420x400+0+0")
root.wm_title("Secure Files")

fileLabel = Label(text = "Enter file name here:")
passLabel = Label(text = "Enter password to be set:")
keyLabel = Label(text = "Enter encryption key:")
okButton = Button(text = "OK")
lockButton = Button(text = "Lock")
encryptButton = Button(text = "Encrypt")
decryptButton = Button(text = "Decrypt")
fileEntry = Entry(root)
passEntry = Entry(root)
keyEntry = Entry(root)
menu = Menu(root)
root.config(menu = menu)
filemenu = Menu(menu)
menu.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "  Open... ", command = fileTray)
filemenu.add_command(label = "  About   ", command = aboutPop)
filemenu.add_command(label = "  Quit    ", command = root.quit)

fileLabel.place(x = 50, y = 30)
passLabel.place(x = 50, y = 140)
fileEntry.place(x = 220, y = 30)
passEntry.place(x = 220, y = 140)
okButton.place(x = 175, y = 60)
lockButton.place(x = 170, y = 170)
keyLabel.place(x = 50, y = 250)
keyEntry.place(x = 220, y = 250)
encryptButton.place(x = 110, y = 280)
decryptButton.place(x = 210, y = 280)

lockButton.config(state = DISABLED)
encryptButton.config(state = DISABLED)
decryptButton.config(state = DISABLED)

okButton.bind("<Button-1>", enabler)

root.mainloop()
