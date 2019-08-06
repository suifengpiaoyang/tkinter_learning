import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Python GUI')

# 界面不能改变大小
# win.resizable(0,0)

# 相关函数
def click_me():
    button1.configure(text = 'Hello ' + name.get() + ' ' + num.get())
    print(check_button_flag_1.get(),type(check_button_flag_1.get()))
    print(check_button_flag_2.get(),type(check_button_flag_2.get()))
    print(check_button_flag_3.get(),type(check_button_flag_3.get()))

# 添加标签
label1 = ttk.Label(win,text = 'Enter a name:')
label1.grid(row = 0,column = 0)
label2 = ttk.Label(win,text = 'Choose a number:')
label2.grid(row = 0,column = 1)

# 添加按钮
button1 = ttk.Button(win,text = 'Click Me!',command = click_me)
button1.grid(row = 1,column = 2)

# 添加输入框
name = tk.StringVar()
entry1 = ttk.Entry(win,width = 12,textvariable = name)
entry1.grid(row = 1,column = 0)

# 添加下拉列表框
num = tk.StringVar()
combobox1 = ttk.Combobox(win,width = 12,textvariable = num)
combobox1['values'] = (1,2,4,42,100)
combobox1.grid(row = 1,column = 1)
combobox1.current(0)

# 添加复选按钮
check_button_flag_1 = tk.IntVar()
check1 = tk.Checkbutton(win,text = 'Disabled',variable = check_button_flag_1,state = 'disabled')
check1.select()
check1.grid(row = 2,column = 0)

check_button_flag_2 = tk.IntVar()
check2 = tk.Checkbutton(win,text = 'UnChecked',variable = check_button_flag_2)
check2.deselect()
check2.grid(row = 2,column = 1)

check_button_flag_3 = tk.IntVar()
check3 = tk.Checkbutton(win,text = 'Enabled',variable = check_button_flag_3)
check3.select()
check3.grid(row = 2,column = 2)

# 设置光标一开始就在输入框内
entry1.focus()

win.mainloop()
