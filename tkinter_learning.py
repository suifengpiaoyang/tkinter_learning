import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python GUI')

# 界面不能改变大小
# win.resizable(0,0)

# 相关函数
def click_me():
    button1.configure(text = '** I have been Clicked! **')
    label1.configure(foreground = 'red')

# 添加标签
label1 = ttk.Label(win,text = 'A Label')
label1.grid(row = 0,column = 0)

# 添加按钮
button1 = ttk.Button(win,text = 'Click Me!',command = click_me)
button1.grid(row = 0,column = 1)

win.mainloop()
