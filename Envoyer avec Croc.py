#!/usr/bin/env python3
import os
import pty
import subprocess

""" Chemin vers l'exécutable Croc "/bin/croc" pour Manjaro et "/usr/local/bin/croc" pour Ubuntu """
CROC_PATH = "/bin/croc"
if os.path.exists(CROC_PATH):
    """ On ne touche pas au path.. sans doute Manjaro """
else:
    """ On modifie path.. sans doute Ubuntu """
    CROC_PATH = "/usr/local/bin/croc"

def get_selected_files():
    """ Retourne la liste des chemins absolus des fichiers sélectionnés dans Nemo. """
    files = os.environ.get("NEMO_SCRIPT_SELECTED_FILE_PATHS")
    if files is None:
        return None
    return files.split(";;")

def send_files_with_croc(files):
    """ Envoie les fichiers avec Croc. """
    cmd = [CROC_PATH, "send"] + files
    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", " ".join(cmd)])

if __name__ == "__main__":
    files = get_selected_files()
    if files:
        send_files_with_croc(files)

