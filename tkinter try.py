# First GUI using tkinter 
from tkinter import *
from tkinter import messagebox

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

# show any item (here this label) on window with pack() or 
# place(x= , y=) for specific location
label.pack() 

# configure window 
tk.config(
    background= "#1664e0"
)

# Create button
def click_hi():
  if (hi_btn['state'] == NORMAL):
    hi_msg = "Hi there! Nice to meet you.👋 "
    print(hi_msg)
    hi_btn['state'] = ACTIVE
    hi_btn['text'] = "Saying hi!"
    return messagebox.showinfo('Saying hi!', hi_msg)
  else:
    # hi_btn[]
    hi_btn['state'] = NORMAL
    hi_btn['text'] = "Say hi.."
  
hi_btn = Button(tk,
             text="Say hi..",
             command=click_hi,
             )

hi_btn.config(bg="green",
           fg="white",
           activebackground="red",
           activeforeground="black",
           state=NORMAL,
                 
           )


hi_btn.pack()






tk.mainloop()