#!/usr/bin/env python3
import os
import pty
import subprocess

""" Path to croc "/bin/croc" for Manjaro and "/usr/local/bin/croc" for Ubuntu """
CROC_PATH = "/bin/croc"
if os.path.exists(CROC_PATH):
    """ don't touch the path.. maybe Manjaro """
else:
    """ We modify path.. maybe Ubuntu """
    CROC_PATH = "/usr/local/bin/croc"

def get_selected_files():
    """ Returns the list of absolute paths of selected files in Nemo. """
    files = os.environ.get("NEMO_SCRIPT_SELECTED_FILE_PATHS")
    if files is None:
        return None
    return files.split(";;")

def send_files_with_croc(files):
    """ Sends files with Croc. """
    cmd = [CROC_PATH, "send"] + files
    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", " ".join(cmd)])

if __name__ == "__main__":
    files = get_selected_files()
    if files:
        send_files_with_croc(files)

