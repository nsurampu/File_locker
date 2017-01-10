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
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s [:-ord(s[len(s) - 1:])]

def pdfLock(event):
    try:
        filename = fileEntry.get()
        user_pass = passEntry.get()
        owner_pass = user_pass
        input_file = filename
        output_file = "temp"

        output = PyPDF2.PdfFileWriter()
        inputf = open(input_file, "rb")

        input_stream = PyPDF2.PdfFileReader(inputf)

        for i in range(0, input_stream.getNumPages()):
            output.addPage(input_stream.getPage(i))

            outputStream = open(output_file, "wb")

        output.encrypt(user_pass, owner_pass, use_128bit = True)
        output.write(outputStream)
        outputStream.close()
        inputf.close()
        os.remove(input_file)
        os.rename(output_file, input_file)
        statusPop()
        disabler()
    except Exception as e:
        showerror("Error", e)
        disabler()

def txtEncrypt(event):
    try:
        input_file = fileEntry.get()
        key = keyEntry.get()

        ifile = open(input_file, "r+")
        plain = ifile.read()
        ifile.close()
        ofile = open(input_file, "w+")
        plain = pad(plain)
        IV = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, IV)
        encrypted = base64.b64encode(IV + cipher.encrypt(plain))
        ofile.write(encrypted)
        ofile.close()
        statusPop()
        disabler()
    except Exception as e:
        showerror("Error", e)
        disabler()

def txtDecrypt(event):
    try:
        efile = fileEntry.get()
        key = keyEntry.get()

        ifile = open(efile, "r+")
        enc  = ifile.read()
        ifile.close()
        ofile = open(efile, "w+")
        enc = base64.b64decode(enc)
        IV = enc[:16]
        cipher = AES.new(key, AES.MODE_CBC, IV)
        decrypted = unpad(cipher.decrypt(enc[16:]))
        ofile.write(decrypted)
        ofile.close()
        statusPop()
        disabler()
    except Exception as e:
        showerror("Error", e)
        disabler()

def enabler(event):
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

def disabler():
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
