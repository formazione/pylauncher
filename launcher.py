import os
import tkinter as tk
import tkinter.ttk as ttk
from glob import glob

root = tk.Tk()
root.title("Launcher")
root.geometry("400x400")

class Button:

  def __init__(self, file, row, col):
    self.file = file
    self.button = ttk.Button(
        root,
        text=file,
        command=self.open_text)
    self.button.grid(row=row, column=col, sticky=tk.NW, pady=0)

  def open_text(self):
    # with open(self.file) as file:
    #   testo = file.read()
    # area.insert(tk.END, testo)
    os.startfile(self.file)

# area = tk.Text()
# area.grid(row=0, column=1)


files = glob("*.py")
print(files)
for n, fname in enumerate(files):
  Button(fname, n, 0)


root.mainloop()