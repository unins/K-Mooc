# import tkinter as tki
# import sys
#
# def close():
# 	sys.exit()
#
# tk = tki.Tk()
# tk.title('Dirty Bomb (64bit)')
# tk.wm_resizable(width=False, height=False)
# tk.wm_geometry(newGeometry='500x300+600+300')
#
# lb1 = tki.Label(tk,text="USERNAME: ")
# lb2 = tki.Label(tk,text="PASSWORD: ")
#
# lb1.grid(row=0, column=0, sticky=tki.W)
# lb2.grid(row=1, column=0, sticky=tki.W)
#
# e1 = tki.Entry(tk,width=10,bd=2)
# e2 = tki.Entry(tk,width=10,bd=2)
#
# e1.grid(row=0, column=1, sticky=tki.W)
# e2.grid(row=1, column=1, sticky=tki.W)
#
# b1 = tki.Button(tk,text="LOGIN", command=close, fg='red')
#
# b1.grid(row=3, column=1, sticky=tki.W)
#
#
#
# tk.mainloop()


import tkinter as tki
import sys

WIND_WIDTH = 500
WIND_HEIGHT = 300

DESTIN_DIR = '../static/imgs/'

def close():
    sys.exit()

tk = tki.Tk()
tk.title('THIS IS SIMPLE TEXT (%sx%s)' %(WIND_WIDTH,WIND_HEIGHT))
tk.wm_resizable(width=True, height=True)
tk.wm_geometry(newGeometry='%sx%s+100+100' %(WIND_WIDTH,WIND_HEIGHT))

lb0 = tki.Label(tk,text=" ")
lb1 = tki.Label(tk,text="USERNAME: ", padx=10)
lb2 = tki.Label(tk,text="PASSWORD: ", padx=10)

lb0.grid(row=0, column=0, sticky=tki.W)
lb1.grid(row=1, column=0, sticky=tki.W)
lb2.grid(row=2, column=0, sticky=tki.W)

# ----------------
e1 = tki.Entry(tk,width=10, bd=5)
e2 = tki.Entry(tk,width=10, bd=5)

e1.grid(row=1, column=1, sticky=tki.W)
e2.grid(row=2, column=1, sticky=tki.W)

#--------------------
b1 = tki.Button(tk, text="SUBMIT")
b2 = tki.Button(tk, text="CANCEL", command=close, fg='red')

b1.grid(row=3, column=0, columnspan=2, sticky=tki.W)
b2.grid(row=3, column=1, sticky=tki.W)

#---------------------
c = tki.Canvas(tk,width=400, height=150, bd=1, bg='white')
# fname = tki.PhotoImage(file=DESTIN_DIR+'SD-run.gif')
fname = tki.PhotoImage(file=DESTIN_DIR+'DB.png')
ph = c.create_image(0,0, anchor='nw', image=fname)
c.grid(row=5, column=0, columnspan=3, sticky=tki.W)

tk.mainloop()
