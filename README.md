# nautilus-sendwithcroc
A python script for Nautilus or Nemo to be able to select one or multiple files or folder and send it with croc (github.com/schollz/croc)

Nautilus 'Send with Croc.py'

This script allows you to send selected files with Croc via Nautilus or Nemo on Manjaro or Ubuntu.
Prerequisites

Make sure you have Croc (tested with version v9.6.4-1fce28e) and python (tested on python 3) installed on your system by following the installation instructions.
Installation

Download the 'Send with Croc.py' file from the repository.
    
Open the file with a text editor and modify the CROC_PATH variable with the path to your Croc executable. The default value is /bin/croc for Manjaro and /usr/local/bin/croc for Ubuntu.
You can also replace NAUTILUS by NEMO (stay in CAPS..) to use this script under nemo.

Save the file and close the text editor.

Make the file executable by running the following command in the terminal: 
    chmod +x 'Send with Croc.py'
Move the file to the Nautilus or Nemo scripts directory by running the following command in the terminal:  
    mv 'Send with Croc.py' ~/.local/share/nautilus/scripts/
    or
    mv 'Send with Croc.py' ~/.local/share/nemo/scripts/
    
Restart Nautilus.

Usage

Select one or more files in Nautilus.
    Right-click on the selected files and go to "Scripts".
    Click on "Send with Croc.py".
    A new terminal window will appear with the Croc command to send the selected files.
    Follow the instructions in the terminal window to complete the file transfer.

Note: The terminal window will remain open until the file transfer is complete.

I also put a French version of the script 'Envoyer avec Croc.py', it's the same program with a french title and french comments..
if you encouter any problem you can contact me at archesys@gmail.com, I did this program with the help of chatGPT and I hope you will enjoy it !

Eric ENDELIN

