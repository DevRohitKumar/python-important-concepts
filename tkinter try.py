# First GUI using tkinter 
from tkinter import *

tk = Tk()

# set window size. here we set constant.
# you can change whatever minimum or maximum size you like👍
tk.geometry("450x450")
tk.minsize(450, 450)
tk.maxsize(450, 450)

# set window to fullscreen mode. doesn't work with maxsize
# tk.attributes("-fullscreen", True) 

# setting icon for window
icon = PhotoImage(file="codingicon.png")
tk.iconphoto(False, icon)

# set title
tk.title("First tkinter GUI")

# add label 
label = Label(tk,
              text= "Tkinter is fun!🥳",
              fg="white",
              font=("san serif", 30, "italic"),
              bg="grey",
              cursor="dot",
              bd=10,
              relief= GROOVE, 
            #   padx=50,
            #   pady=50,
              image=icon,
              compound= "bottom",
              )
label.pack() #we can also use place(x= , y=) for specific location

# configure window 
tk.config(
    background= "#1664e0"
)



tk.mainloop()