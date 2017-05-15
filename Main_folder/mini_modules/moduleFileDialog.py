"""Module used to open GUI dialog in which user can choose file.

This module uses python module tkinter to open dialog in which user
can choose file. This dialog is opened using function file_dialog().
"""
import tkinter as tk
from tkinter import filedialog

def file_dialog(title="Choose file"):
    """Opens GUI dialog in which user can choose file,

    path to chosen file is returned"""
    root = tk.Tk()
    root.withdraw()
    options = {"title":title}
    file_path = filedialog.askopenfilename(**options)

    return file_path
