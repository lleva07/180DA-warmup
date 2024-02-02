import tkinter as tk
from tkinter import PhotoImage
def choice1():
    print("Button clicked!")
root = tk.Tk()
root.geometry("880x200")

rock = PhotoImage(file="rock.png")
paper = PhotoImage(file="paper.png")
scissor = PhotoImage(file="scissor.png")
stop = PhotoImage(file="skull.png")
choice1 = tk.Button(root, image = rock, command=on_button_click, width=100, height=100)
choice1.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)
choice2 = tk.Button(root, image = paper, command=on_button_click, width=100, height=100)
choice2.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)
choice3 = tk.Button(root, image = scissor, command=on_button_click, width=100, height=100)
choice3.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)
choice4 = tk.Button(root, image = stop, command=on_button_click, width=100, height=100)
choice4.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)
root.mainloop()