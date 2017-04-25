#File choosing window test
import tkinter as tk
from tkinter import filedialog

import os

for i in range(1):
    root = tk.Tk()
    root.withdraw()
    options = {"title":"Choose FILE!"}
    file_path = filedialog.askopenfilename(**options)
    print(os.path.dirname(file_path))
