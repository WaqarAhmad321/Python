from tkinter import *

root = Tk()
root.title("My First GUI")
root.geometry("733x434")
frame = Frame(bg="grey", padx=20, pady=20, relief=SUNKEN)
label = Label(frame, text="Welcome To PyCharm")
frame.pack(fill=Y)
label.pack(fill=X)

  
root.mainloop()
