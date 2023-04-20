# 733x434
from tkinter import *
root = Tk()

root.geometry("733x434")
# root.minsize(400, 200)

# root.maxsize(733, 434)

# images = PhotoImage(file="D:\\Code\\Python\\Modules\\Tkinter\\pycharm.png")

label = Label(text="Welcome to PyCharm\n", font=(
    "Ariel", 20, "bold"), bg='red', fg="white", borderwidth=4, relief=SUNKEN, padx=5, pady=3)

label.pack(anchor='sw', side=BOTTOM, fill=X)
root.mainloop()
