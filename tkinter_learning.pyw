import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as mBox

win = tk.Tk()
win.title('Python GUI')

# 界面设置

# 界面不能改变大小
win.resizable(0,0)

# 常量
colors = ['Blue','Gold','Red']

scrolW = 30
scrolH = 7

# 相关函数

def click_me():
    button1.configure(text = 'Hello ' + name.get() + ' ' + num.get())
    print(check_button_flag_1.get(),type(check_button_flag_1.get()))
    print(check_button_flag_2.get(),type(check_button_flag_2.get()))
    print(check_button_flag_3.get(),type(check_button_flag_3.get()))

def rad_call():
    color_flag = rad_var.get()
    if color_flag == 0:
        tab2.configure(background = colors[0])
    elif color_flag == 1:
        tab2.configure(background = colors[1])
    elif color_flag == 2:
        tab2.configure(background = colors[2])

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
    current_window_width = master.winfo_width()
    current_window_height = master.winfo_height()
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()
    suitable_location_x = int((screen_width - current_window_width)*width_flag)
    suitable_location_y = int((screen_height - current_window_height)*height_flag)
    master.geometry('+{}+{}'.format(suitable_location_x,suitable_location_y))
    master.deiconify()

def __quit(master):
    master.quit()
    master.destroy()
    exit()

def change_bg_color(color_index):
    tab2.configure(background = colors[color_index])

def __msgbox():
    # mBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2015.')
    # mBox.showwarning('Python Message Warning Box', 'A Python GUI created using tkinter:\nWarning: There might be a bug in this code.')    
    # mBox.showerror('Python Message Error Box', 'A Python GUI created using tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
    flag = mBox.askyesno("Python Message Dual Choice Box", "Are you sure you really wish to do this?")
    if flag:
        print('You choose Yes')
    else:
        print('You choose No')

def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT,value + '\n')
    scr.see(tk.END)

# 增加菜单栏
menubar = Menu(win)
win.config(menu = menubar)

file_menu = Menu(menubar,tearoff = 0)
file_menu.add_command(label = 'New')
file_menu.add_separator()
file_menu.add_command(label = 'Exit',command = lambda:__quit(win))
menubar.add_cascade(label = 'File',menu = file_menu)

# add color menu
color_menu = Menu(menubar,tearoff = 0)
color_menu.add_command(label = colors[0],command = lambda:change_bg_color(0))
color_menu.add_command(label = colors[1],command = lambda:change_bg_color(1))
color_menu.add_command(label = colors[2],command = lambda:change_bg_color(2))
menubar.add_cascade(label = 'Color',menu = color_menu)

# add help menu
help_menu = Menu(menubar,tearoff = 0)
help_menu.add_command(label = 'About',command = __msgbox)
menubar.add_cascade(label = 'Help',menu = help_menu)

# add tab
tab_control = ttk.Notebook(win)
tab_control.grid(row = 0,column = 0)

tab1 = tk.Frame(tab_control)
tab1.grid(row = 0,column = 0)
tab_control.add(tab1,text = 'Tab1')

tab2 = tk.Frame(tab_control)
tab2.grid(row = 0,column = 0,sticky = 'WE')
tab_control.add(tab2,text = 'Tab2')

# 增加 levelFrame

monty = ttk.LabelFrame(tab1,text = ' Monty Python ')
monty.grid(row = 0,column = 0,padx = 10,pady = 5)

label_frame = ttk.LabelFrame(tab2,text = 'The Snake')
label_frame.grid(row = 0,column = 0,padx = 20,pady = 31)

label_frame2 = ttk.LabelFrame(label_frame,text = 'Levels in a Frame ')
label_frame2.grid(row = 7,column = 0)

# 在 levelFrame 上添加标签
for i in range(2):
    ttk.Label(label_frame2,text = 'Label{}'.format(i + 1)).grid(row = i,column = 0)

# 添加标签
label1 = ttk.Label(monty,text = 'Enter a name:')
label1.grid(row = 0,column = 0,sticky = 'W')
label2 = ttk.Label(monty,text = 'Choose a number:')
label2.grid(row = 0,column = 1)

# 添加按钮
button1 = ttk.Button(monty,text = 'Click Me!',command = click_me)
button1.grid(row = 1,column = 2)

# 添加输入框
name = tk.StringVar()
entry1 = ttk.Entry(monty,width = 12,textvariable = name)
entry1.grid(row = 1,column = 0,sticky = tk.W)

# 设置光标一开始就在输入框内
entry1.focus()

# 添加下拉列表框
num = tk.StringVar()
combobox1 = ttk.Combobox(monty,width = 12,textvariable = num)
combobox1['values'] = (1,2,4,42,100)
combobox1.grid(row = 1,column = 1)
combobox1.current(0)

# 添加复选按钮
check_button_flag_1 = tk.IntVar()
check1 = tk.Checkbutton(label_frame,text = 'Disabled',variable = check_button_flag_1,state = 'disabled')
check1.select()
check1.grid(row = 2,column = 0,sticky = 'W')

check_button_flag_2 = tk.IntVar()
check2 = tk.Checkbutton(label_frame,text = 'UnChecked',variable = check_button_flag_2)
check2.deselect()
check2.grid(row = 2,column = 1,sticky = 'W')

check_button_flag_3 = tk.IntVar()
check3 = tk.Checkbutton(label_frame,text = 'Enabled',variable = check_button_flag_3)
check3.select()
check3.grid(row = 2,column = 2,sticky = 'W')

# 添加单选按钮
rad_var = tk.IntVar()
# 设置一个不存在的值，不然一开始就会选中第一个单选按钮
rad_var.set(99)
for col in range(3):
    cur_cad = 'rad' + str(col)
    cur_cad = tk.Radiobutton(label_frame,text = colors[col],variable = rad_var,value = col,command = rad_call)
    cur_cad.grid(row = 5,column = col,sticky = tk.W)

# 添加下拉滚动条
# 在换行时，以单词为分界点，就是说在换行时不会分割单词
scr = scrolledtext.ScrolledText(monty,width = scrolW,height = scrolH,wrap = tk.WORD)
scr.grid(column = 0,columnspan = 3,row = 4,sticky = 'WE')

# adding a spinbox widget
spin = tk.Spinbox(monty,values = (1,2,4,42,100),width = 5,bd = 8,command = _spin)
spin .grid(row = 2,column = 0)

# labelFrame 中所有部件设置

for child in monty.winfo_children():
    child.grid_configure(padx = 5,pady = 2)

for child in label_frame2.winfo_children():
    child.grid_configure(padx = 5,pady = 4)

center_window(win)
# 添加图标
# 图标放在 窗口居中以后添加会减少很多问题
# 比如闪影，原因善不可知
win.iconbitmap('./icon/hallow.ico')
win.mainloop()
