# File_locker
An application for locking PDF files and encrypting text files

Run the installation script first before running the application. To run it, follow these steps:

1. Type sudo apt-get update in the terminal. This will update all the necessary packages for running the installation              script.

2. Run the installationScript.sh file.
   Eg.- if the file's path is /home/user/Files, then type
        chmod 700 /home/user/Files/installationScript.sh
        then type
        /home/user/Files/installationScript.sh  This will install the necessary modules required for running the  program

This application can be used to password lock PDF files and to encrypt text files using ARC4 stream encryption.

The PDF file remains locked unless the lock is removed.

The text files are encrypted using a user entered key, that will have to be entered later to decrypt the text file.

Windows users can now download the zip file and extract it to run the application. Python need not be installed for this.
