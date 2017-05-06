#File choosing window test
import tkinter as tk
from tkinter import filedialog

import os

class CustomError(Exception):
    pass

#raise CustomError("It does work")

value = "a"
try:
    value = int(value)
except ValueError:
    print(value)

for i in range(1):
    root = tk.Tk()
    root.withdraw()
    options = {"title":"Choose FILE!"}
    file_path = filedialog.askopenfilename(**options)
    print(os.path.dirname(file_path))

    new_path = file_path
    tail = "true"
    while not os.path.isdir(os.path.join(new_path,"Resources")) and tail:
        new_path, tail = os.path.split(new_path)
        print(tail)
        print(new_path)

    print(new_path)
