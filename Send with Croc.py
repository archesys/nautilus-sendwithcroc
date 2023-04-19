#!/usr/bin/env python3
import os
import pty
import subprocess

# Path to the Croc executable "/bin/croc" for Manjaro and "/usr/local/bin/croc" for Ubuntu
CROC_PATH = "/bin/croc"

def get_selected_files():
    """
    Returns the list of absolute paths of selected files in Nautilus.
    """
    files = os.environ.get("NAUTILUS_SCRIPT_SELECTED_FILE_PATHS")
    if files is None:
        return None
    return files.split(";;")

def send_files_with_croc(files):
    """
    Sends files with Croc.
    """
    cmd = [CROC_PATH, "send"] + files
    subprocess.Popen(["gnome-terminal", "--", "bash", "-c", " ".join(cmd)])

if __name__ == "__main__":
    files = get_selected_files()
    if files:
        send_files_with_croc(files)

