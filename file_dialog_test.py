#File choosing window test
import tkinter as tk
from tkinter import filedialog

for i in range(3):
    root = tk.Tk()
    root.withdraw()
    options = {"title":"Choose FILE!"}
    file_path = filedialog.askopenfilename(**options)
    print(file_path)
