# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 10:23:52 2017

@author: pyh
"""

def nearby(lp_old,lp_new,pos):
    import numpy as np
    dpos=pos*lp_old
    pos_new=dpos*lp_new.I
    dis=dpos*np.transpose(dpos)
    dis_old=0
    while dis_old !=dis:
        dis_old=dis
        for i in range(3):
            for j in range(3):
                dpos_new=(pos_new+np.mat([i-1,j-1]))*lp_new
                dis_new=dpos_new*np.transpose(dpos_new)
                if dis > dis_new:
                    dis = dis_new
                    pos_n=pos_new+np.mat([i-1,j-1])
        pos_new=pos_n       
    return pos_new
                    
    

def calculator():
    import numpy as np
    n=int(entryn.get())
    x=float(entryx.get())
    y=float(entryy.get())
    pos=np.mat([x,y])
    if n!=1:
        lp_old = np.mat([[3/2,np.sqrt(3)/2],[0,np.sqrt(3)]])
        lp_new = lp_old/n
        pos_new = nearby(lp_old,lp_new,pos)
    else:
        pos_new=pos
    p.config(text= '%f %f'%(pos_new[0,0],pos_new[0,1]))
    
import tkinter as tk

top = tk.Tk()

top.title('RC Calculator')

tk.Label(top,text='n',height = 0,font=("Arial", 15)).grid(row = 2,column = 1)
tk.Label(top,text='Kx',height = 0,font=("Arial", 15)).grid(row = 2,column = 2)
tk.Label(top,text='Ky',height = 0,font=("Arial", 15)).grid(row = 2,column = 4)
tk.Label(top,text='Folding Coordinate:',height = 0,font=("Arial", 15)).grid(row = 0,column = 0)
p=tk.Label(top,text='%f %f'%(0,0),height = 0,font=("Arial", 15))
p.grid(row = 1,column = 0)

entryn=tk.StringVar()
tk.Entry(top,textvariable = entryn).grid(row = 3,column = 1)
entryx=tk.StringVar()
tk.Entry(top,textvariable = entryx).grid(row = 3,column = 2)
entryy=tk.StringVar()
tk.Entry(top,textvariable = entryy).grid(row = 3,column = 4)

tk.Button(top, text = "Calculate", height = 0,font=("Arial", 15),command = calculator).grid(row = 4,column = 5)
top.mainloop()
