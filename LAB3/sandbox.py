import tkinter as tk
from tkinter import PhotoImage
def choice1():
    global choice 
    choice = 'r'
def choice2():
    global choice 
    choice = 'p'
def choice3():
    global choice 
    choice = 's'
def choice4():
    global choice 
    choice = 'q'

def new_display():
    result_label.config(image=None)

    new_image = PhotoImage(file="new_image.png")
    result_label.config(image=new_image)
    result_label.image = new_image  

root = tk.Tk()
root.geometry("880x200")

rock = PhotoImage(file="rock.png")
paper = PhotoImage(file="paper.png")
scissor = PhotoImage(file="scissor.png")
stop = PhotoImage(file="skull.png")
result = PhotoImage(file="")
choice1 = tk.Button(root, image = rock, command=choice1, width=100, height=100)
choice1.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)
choice2 = tk.Button(root, image = paper, command=choice2, width=100, height=100)
choice2.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)
choice3 = tk.Button(root, image = scissor, command=choice3, width=100, height=100)
choice3.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)
choice4 = tk.Button(root, image = stop, command=choice4, width=100, height=100)
choice4.pack(side=tk.LEFT, padx=20, fill=tk.BOTH, expand=True)

result_label = tk.Label(root, text="Result will be displayed here.")
result_label.pack(side=tk.BOTTOM, pady=10)

display_result_btn = tk.Button(root, text="Display Result")
display_result_btn.pack()

root.mainloop()
