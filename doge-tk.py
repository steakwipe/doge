import tkinter as tk
from tkinter import messagebox as mb

def in1():
    mb.showinfo("cate", "the cate liked that :D")
def in2():
    mb.showinfo("cate", "the cate is mad D:")
def in3():
    mb.showerror("cate", "you killed the cate you monster")
    mb.showerror("cate", "how could you..")
    mb.showerror("cate", "don't come near me or my cates")
    exit("you killed the cate you monster how do you feel about yourself?")

tk.Button(text='pet cate', command=in1).pack(fill=tk.X)
tk.Button(text='feed cate', command=in1).pack(fill=tk.X)
tk.Button(text='good boy', command=in1).pack(fill=tk.X)
tk.Button(text='play with he cate', command=in1).pack(fill=tk.X)
tk.Button(text='take the ball form the cate', command=in2).pack(fill=tk.X)
tk.Button(text='give the cate the ball', command=in1).pack(fill=tk.X)
tk.Button(text='kill the cate..', command=in3).pack(fill=tk.X)
tk.mainloop()
