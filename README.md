# nautilus-sendwithcroc
A python script for Nautilus or Nemo to be able to select one or multiple files or folder and send it with croc (github.com/schollz/croc)

Nautilus 'Send with Croc.py'

This script allows you to send selected files with Croc via Nautilus or Nemo on Manjaro or Ubuntu.
Prerequisites

Make sure you have Croc (tested with version v9.6.4-1fce28e) and python (tested on python 3) installed on your system.

The installation script is not ready yet, it can just give the informations about the dependencies for the moment..So just follow the instructions.

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
    
Restart Nautilus or Nemo.

Usage

Select one or more files in Nautilus or Nemo.
    Right-click on the selected files and go to "Scripts".
    Click on "Send with Croc.py".
    A new terminal window will appear with the Croc command to send the selected files.
    Follow the instructions in the terminal window to complete the file transfer.

Note: The terminal window will remain open until the file transfer is complete.

I also put a French version of the script 'Envoyer avec Croc.py', it's the same program with a french title and french comments..
if you encouter any problem you can contact me at archesys@gmail.com, I did this program with the help of chatGPT and I hope you will enjoy it !

Eric ENDELIN

French Translation

Un script python pour Nautilus ou Nemo pour pouvoir sélectionner un ou plusieurs fichiers ou dossier et l'envoyer avec croc (github.com/schollz/croc)

Nautilus 'Envoyer avec Croc.py'

Ce script permet d'envoyer des fichiers sélectionnés avec Croc via Nautilus ou Nemo sur Manjaro ou Ubuntu.

Conditions préalables

Assurez-vous que Croc (testé avec la version v9.6.4-1fce28e) et python (testé sur python 3) sont installés sur votre système.

Le script d'installation n'est pas encore prêt, il peut juste donner les informations sur les dépendances pour le moment..Donc suivez simplement les instructions.


Installation

Téléchargez le fichier "Envoyer avec Croc.py" depuis le github.

Ouvrez le fichier avec un éditeur de texte et modifiez la variable CROC_PATH avec le chemin de votre exécutable Croc. La valeur par défaut est /bin/croc pour Manjaro et /usr/local/bin/croc pour Ubuntu.
Vous pouvez aussi remplacer NAUTILUS par NEMO (restez en MAJ..) pour utiliser ce script sous nemo.

Enregistrez le fichier et fermez l'éditeur de texte.

Rendez le fichier exécutable en exécutant la commande suivante dans le terminal : chmod +x 'Send with Croc.py' Déplacez le fichier dans le répertoire des scripts Nautilus ou Nemo en exécutant la commande suivante dans le terminal :
mv 'Envoyer avec Croc.py' ~/.local/share/nautilus/scripts/ ou mv 'Envoyer avec Croc.py' ~/.local/share/nemo/scripts/

Redémarrez Nautilus ou Nemo.

Usage

Sélectionnez un ou plusieurs fichiers dans Nautilus ou Nemo. Faites un clic droit sur les fichiers sélectionnés et allez dans "Scripts". Cliquez sur "Envoyer avec Croc.py". Une nouvelle fenêtre de terminal apparaîtra avec la commande Croc pour envoyer les fichiers sélectionnés. Suivez les instructions dans la fenêtre du terminal pour terminer le transfert de fichiers.

Remarque : La fenêtre du terminal restera ouverte jusqu'à ce que le transfert de fichier soit terminé.

J'ai aussi mis une version anglaise du script 'Send with Croc.py', c'est le même programme avec un titre en Anglais et des commentaires en Anglais.. si vous rencontrez un problème vous pouvez me contacter à archesys@gmail.com, j'ai fait ce programme avec l'aide de chatGPT et j'espère que vous l'apprécierez !

Eric ENDELIN
