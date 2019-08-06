import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python GUI')

# 界面不能改变大小
# win.resizable(0,0)

# 相关函数
def click_me():
    button1.configure(text = 'Hello ' + name.get())

# 添加标签
label1 = ttk.Label(win,text = 'Enter a name:')
label1.grid(row = 0,column = 0)

# 添加按钮
button1 = ttk.Button(win,text = 'Click Me!',command = click_me)
button1.grid(row = 1,column = 1)

# 添加输入框
name = tk.StringVar()
entry1 = ttk.Entry(win,width = 12,textvariable = name)
entry1.grid(row = 1,column = 0)

# 设置光标一开始就在输入框内
entry1.focus()

win.mainloop()
