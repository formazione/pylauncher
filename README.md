# pylauncher
A laucher of programs and apps through a GUI made with Python and tkinter

This script creates a GUI with buttons that can open a file or a website with a python GUI made with the tkinter module.

This is the code

    import os
    import tkinter as tk
    import tkinter.ttk as ttk


    root = tk.Tk()
    root.title("Launcher")
    root.geometry("400x400")

    class Button:

      def __init__(self, text, func, row, col):
          self.button = ttk.Button(
              root,
              text=text,
              command=func)
          self.button.grid(row=row, column=col, sticky=tk.NW, pady=0)

      def open_text(text):
        os.startfile(text)


    Button("Open example text", lambda x: Button.open_text("example_for_launch.txt"), 0, 0)
    Button("Open example text 2", lambda x: Button.open_text("Hello World 2.txt"), 1, 0)
    root.mainloop()
