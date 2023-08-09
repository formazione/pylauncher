# pylauncher
# crate a button for every python script; click to open file

import os
import tkinter as tk
import tkinter.ttk as ttk
from glob import glob

root = tk.Tk()
root.geometry("400x400")

numfile = 0
class Button:

  def __init__(self, file, row, col):
    self.file = file
    self.row = row
    self.col = col
    self.button()

  def button(self):
    self.button = ttk.Button(
        root,
        text=self.file,
        command=self.open_pythonfile)
    self.position()

  def position(self):
    self.button.grid(row=self.row,
        column=self.col,
        sticky=tk.NW, pady=0)

  def open_pythonfile(self):
    os.system(f"start {self.file}")


files = glob("*.py")
for n, fname in enumerate(files):
  Button(fname, n, 0)
  numfile += 1

root.title(f"PyLauncher - num. Files: {numfile}")

root.mainloop()