#Small module used to select file using friendly dialog
import tkinter as tk
from tkinter import filedialog

def file_dialog(title="Choose file"): #Pops up window in which user
    #can choose file like using windows explorer

    #It will have entered title
    
    root = tk.Tk()
    root.withdraw()
    options = {"title":title}
    file_path = filedialog.askopenfilename(**options)

    return file_path
