import re
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title('Python GUI')

# 界面设置

# 因为在后面需要窗口居中效果，而一开始需要隐藏窗口，
# 这样后续才不会在屏幕上面出现闪影
# win.withdraw()

# 界面不能改变大小
# win.resizable(0,0)

# 常量
colors = ['Blue','Gold','Red']

scrolW = 30
scrolH = 3

# 相关函数

def click_me():
    button1.configure(text = 'Hello ' + name.get() + ' ' + num.get())
    print(check_button_flag_1.get(),type(check_button_flag_1.get()))
    print(check_button_flag_2.get(),type(check_button_flag_2.get()))
    print(check_button_flag_3.get(),type(check_button_flag_3.get()))

def rad_call():
    color_flag = rad_var.get()
    if color_flag == 0:
        win.configure(background = colors[0])
    elif color_flag == 1:
        win.configure(background = colors[1])
    elif color_flag == 2:
        win.configure(background = colors[2])

def center_window(master,width_flag = 0.382,height_flag = 0.382):
    """
    窗口先隐藏到大小设置完成以后才恢复，主要原因是如果不这么做，会发生闪影现象。
    width_flag 和 height_flag 值在 (0,1) ，是定位目标左上角的坐标的权重值。
    都设置为 0.5 的话，则窗口居中。默认是窗口放在黄金比例上。
    withdraw() 函数是隐藏窗口，deiconify() 函数是显示窗口。
    update() 函数是将前面原件摆放以后的窗口更新，以便获得摆放后窗口的自适配大小。
    """
    master.withdraw()
    master.update()
    current_window_width,current_window_height = [int(line) for line in re.findall(r'(\d*)x(\d*)', master.geometry())[0]]
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    suitable_width = int((screen_width - current_window_width)*width_flag)
    suitable_height = int((screen_height - current_window_height)*height_flag)
    master.geometry('{}x{}+{}+{}'.format(current_window_width,current_window_height,suitable_width,suitable_height))
    master.deiconify()

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

# 设置光标一开始就在输入框内
entry1.focus()

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

# 添加单选按钮
rad_var = tk.IntVar()
# 设置一个不存在的值，不然一开始就会选中第一个单选按钮
rad_var.set(99)
for col in range(3):
    cur_cad = 'rad' + str(col)
    cur_cad = tk.Radiobutton(win,text = colors[col],variable = rad_var,value = col,command = rad_call)
    cur_cad.grid(row = 5,column = col,sticky = tk.W)

# 添加下拉滚动条
# 在换行时，以单词为分界点，就是说在换行时不会分割单词
scr = scrolledtext.ScrolledText(win,width = scrolW,height = scrolH,wrap = tk.WORD)
scr.grid(column = 0,columnspan = 3,row = 6)

center_window(win)

win.mainloop()
