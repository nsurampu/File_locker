# File_locker
An application for locking PDF files and encrypting text files

Run the installation script first before running the application. To run it, follow these steps:

1. Type sudo apt-get update in the terminal. This will update all the necessary packages for running the installation              script.

2. Run the installationScript.sh file.
   Eg.- if the file's path is /home/user/Files, then type
        chmod 700 /home/user/Files/installationScript.sh
        then type
        /home/user/Files/installationScript.sh  This will install the necessary modules required for running the  program

This application can be used to password lock PDF files and to encrypt text files using AES block encryption.

The text files are encrypted using a user entered key, that will have to be entered later to decrypt the text file.

Windows users can now download the zip file and extract it to run the application. Python need not be installed for this.

Version History:

1. Ver 1.0   - Console based application capable of locking only pdf files.
2. Ver 1.1   - Application can now also encrypt txt files using Caesar cipher.
3. Ver 1.2   - Made the switch from Caesar cipher to RC4 encryption.
4. Ver 2.0   - Application now has a GUI.
5. Ver 2.0.1 - File tray added to GUI which now enables users to select files from various locations on PC.
6. Ver 2.1   - Made the switch from RC4 to AES encryption (Special thanks to Marcus from stackoverflow.com for the pad-unpad algorithm).
