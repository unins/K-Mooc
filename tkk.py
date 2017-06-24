from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sys

# --------------------------------------------------------------------------
# # def close():
#     # sys.exit()
#
# def showinfo():
#     tkinter.messagebox.showinfo("warning","function in development")
#
#
# root = Tk()
#
# frame = Frame(root)
#
# labelText = StringVar()
#
# label = Label(frame, textvariable=labelText)
# button = Button(frame, text="Click Me", command = showinfo)
#
# labelText.set("I am a Label")
#
# label.pack()
# button.pack()
# frame.pack()
#
# root.mainloop()
# --------------------------------------------------------------------------
# tk = Tk()
#
# tk.wm_geometry(newGeometry='500x300+600+300')
# ttk.Button(tk, text="rwqrqwrqwrqwrqwrqwrqwrqwrqwrqwrqwrqwrqwrqwrqwrqwrqwr").pack()
# tkinter.Button(tk, text="UGLY").pack()
#
# tk.mainloop()
#---------------------------------------------------------------------------
#
# tk = Tk()
# tk.wm_geometry(newGeometry='400x400+800+100')
# tk.wm_attributes("-topmost",1)
#
# DESTIN_DIR = './static/imgs/'
#
# f=Frame(tk)
#
# Label(f, text="Uh-Oh.. You're in a BIG trouble").pack()
# Button(f, text='fire nuke').pack(side=LEFT, fill=Y)
# Button(f, text='fire nuke').pack(side=TOP, fill=X)
# Button(f, text='fire nuke').pack(side=RIGHT, fill=X)
# Button(f, text='fire nuke').pack(side=LEFT, fill=X)
#
# c = tkinter.Canvas(tk,width=400, height=150, bd=1, bg='white')
# # fname = tkinter.PhotoImage(file=DESTIN_DIR+'SD-run.gif')
# fname = tkinter.PhotoImage(file=DESTIN_DIR+'DB.png')
# ph = c.create_image(0,0, anchor='nw', image=fname)
# c.pack()
#

# f.pack()
#
# tk.mainloop()
# ---------------------------------------------------------------------

# tk = Tk()
# tk.wm_geometry(newGeometry='400x400+800+100')
# tk.wm_attributes("-topmost",1)
#
# Label(tk, text='Description').grid(row=0,column=0,sticky=W)
# Entry(tk, width=40).grid(row=0,column=1, padx=10)
# Button(tk, text='SUBMIT').grid(row=10, column=1, sticky=W, padx=15)
#
# Label(tk, text='Graphics Config').grid(row=1, column=0, sticky=W)
# Radiobutton(tk, text='Super', value=1).grid(row=2, column=0,sticky=W, padx=15)
# Radiobutton(tk, text='High', value=2).grid(row=3, column=0,sticky=W, padx=15)
# Radiobutton(tk, text='Medium', value=3).grid(row=4, column=0,sticky=W, padx=15)
# Radiobutton(tk, text='Low', value=4).grid(row=5, column=0,sticky=W, padx=15)
# Radiobutton(tk, text='Minimal', value=5).grid(row=6, column=0,sticky=W, padx=15)
#
# Label(tk, text='Advanced Settings').grid(row=1, column=1, sticky=W)
# Checkbutton(tk, text='Vertical Sync').grid(row=2, column=1, sticky=W, padx=15)
# Checkbutton(tk, text='Motion Blur').grid(row=3, column=1, sticky=W, padx=15)
# Checkbutton(tk, text='Anti-Aliasing').grid(row=4, column=1, sticky=W, padx=15)
# Checkbutton(tk, text='High Quality Material').grid(row=5, column=1, sticky=W, padx=15)
# Checkbutton(tk, text='Dynamic Lights').grid(row=6, column=1, sticky=W, padx=15)
# Checkbutton(tk, text='Dynamic Decals').grid(row=7, column=1, sticky=W, padx=15)
#
# tk.mainloop()
#-------------------------------------------------------------------------
tk = Tk()
tk.wm_geometry(newGeometry='400x400+800+100')
tk.wm_attributes("-topmost",1)

def get_sum(event):
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    sum = num1 * num2

    sumEntry.delete(0,'end')
    sumEntry.insert(0, sum)

def window_close():
    sys.exit()

def clear_all():
    num1Entry.delete(0, 'end')
    num2Entry.delete(0, 'end')
    sumEntry.delete(0, 'end')

f1 = Frame(tk)
f2 = Frame(tk)
f3 = Frame(tk)
f4 = Frame(tk)
f5 = Frame(tk)

num1Entry = Entry(f1, width=5)
num1Entry.pack(side=LEFT)

Label(f1, text='x').pack(side=LEFT)

num2Entry = Entry(f1, width=5)
num2Entry.pack(side=LEFT)

equalButton = Button(f1, text='=')
equalButton.bind('<Button-1>', get_sum)
equalButton.pack(side=LEFT)

sumEntry = Entry(f1)
sumEntry.pack(side=LEFT)

f1.pack(side=TOP)

#------------------------------------------------
b1 = Button(f2, text='1', width=8, pady=8)
b1.pack(side=LEFT)

b2 = Button(f2, text='2', width=8, pady=8)
b2.pack(side=LEFT)

b3 = Button(f2, text='3', width=8, pady=8)
b3.pack(side=LEFT)

f2.pack(side=TOP)
#------------------------------------------------
b4 = Button(f3, text='4', width=8, pady=8)
b4.pack(side=LEFT)

b5 = Button(f3, text='5', width=8, pady=8)
b5.pack(side=LEFT)

b6 = Button(f3, text='6', width=8, pady=8)
b6.pack(side=LEFT)

f3.pack(side=TOP)
#------------------------------------------------
b7 = Button(f4, text='7', width=8, pady=8)
b7.pack(side=LEFT)

b8 = Button(f4, text='8', width=8, pady=8)
b8.pack(side=LEFT)

b9 = Button(f4, text='9', width=8, pady=8)
b9.pack(side=LEFT)

f4.pack(side=TOP)
#------------------------------------------------
b10 = Button(f5, text='AC', width=8, pady=8, fg='red', command = clear_all)
b10.pack(side=LEFT)

b11 = Button(f5, text='0', width=8, pady=8)
b11.pack(side=LEFT)

b12 = Button(f5, text='CLOSE', width=8, pady=8, fg='red', command = window_close)
b12.pack(side=LEFT)

f5.pack(side=TOP)


tk.mainloop()
