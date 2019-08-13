import time
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import scrolledtext
from tkinter import messagebox as mBox
from threading import Thread
from queue import Queue

# 常量
colors = ['Blue','Gold','Red']
scrolW = 40
scrolH = 10

class GUI:

    def __init__(self):
        self.win = tk.Tk()
        self.win.title('Python GUI')
        self.win.resizable(0,0)         # 设置界面手动不能改变大小
        self.gui_queue = Queue()
        self.create_widgets()
        self.center_window(self.win)
        self.win.iconbitmap('./icon/hallow.ico') # 添加图标，最好在居中之后添加，不然可能会产生闪影，原因不明。
        self.win.mainloop()

    # 相关函数

    def use_queue(self):
        gui_queue = Queue()
        print(gui_queue)
        for i in range(10):
            gui_queue.put('Message from a queue: '+ str(i))
        while not gui_queue.empty():
            print(gui_queue.get())

    def test_thread(self,num_of_loops = 10):
        print('Hi, how are you?')
        for i in range(num_of_loops):
            time.sleep(1)
            self.scr.insert(tk.INSERT, str(i) + '\n')
            self.scr.see(tk.END)
        time.sleep(1)
        print('method in a thread():',self.run_thread.isAlive())

    def create_thread(self,**kwargs):
        self.run_thread = Thread(**kwargs)
        self.run_thread.setDaemon(True)
        self.run_thread.start()
        print(self.run_thread)
        print('method in a thread():',self.run_thread.isAlive())

        write_t = Thread(target = self.use_queue,daemon = True)
        write_t.start()

    def click_me(self):
        self.button1.configure(text = 'Hello ' + self.name.get() + ' ' + self.num.get())
        print(self.check_button_flag_1.get(),type(self.check_button_flag_1.get()))
        print(self.check_button_flag_2.get(),type(self.check_button_flag_2.get()))
        print(self.check_button_flag_3.get(),type(self.check_button_flag_3.get()))
        self.create_thread()
        # self.create_thread(target = self.test_thread,args = [8])
        # self.create_thread(target = self.use_queue)

    def rad_call(self):
        color_flag = self.rad_var.get()
        if color_flag == 0:
            self.tab2.configure(background = colors[0])
        elif color_flag == 1:
            self.tab2.configure(background = colors[1])
        elif color_flag == 2:
            self.tab2.configure(background = colors[2])

    def center_window(self,master,width_flag = 0.382,height_flag = 0.382):
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

    def __quit(self,master):
        master.quit()
        master.destroy()
        exit()

    def change_bg_color(self,color_index):
        self.tab2.configure(background = colors[color_index])

    def __msgbox(self):
        # mBox.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nThe year is 2015.')
        # mBox.showwarning('Python Message Warning Box', 'A Python GUI created using tkinter:\nWarning: There might be a bug in this code.')    
        # mBox.showerror('Python Message Error Box', 'A Python GUI created using tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')
        flag = mBox.askyesno("Python Message Dual Choice Box", "Are you sure you really wish to do this?")
        if flag:
            print('You choose Yes')
        else:
            print('You choose No')

    def _spin(self,spin_name):
        value = spin_name.get()
        print(value)
        self.scr.insert(tk.INSERT,value + '\n')
        # 一直将滚动条自动滚动到末端
        self.scr.see(tk.END)

    def create_widgets(self):

        # 增加菜单栏
        menubar = Menu(self.win)
        self.win.config(menu = menubar)

        file_menu = Menu(menubar,tearoff = 0)
        file_menu.add_command(label = 'New')
        file_menu.add_separator()
        file_menu.add_command(label = 'Exit',command = lambda:__quit(self.win))
        menubar.add_cascade(label = 'File',menu = file_menu)

        # add color menu
        color_menu = Menu(menubar,tearoff = 0)
        color_menu.add_command(label = colors[0],command = lambda:change_bg_color(0))
        color_menu.add_command(label = colors[1],command = lambda:change_bg_color(1))
        color_menu.add_command(label = colors[2],command = lambda:change_bg_color(2))
        menubar.add_cascade(label = 'Color',menu = color_menu)

        # add help menu
        help_menu = Menu(menubar,tearoff = 0)
        help_menu.add_command(label = 'About',command = self.__msgbox)
        menubar.add_cascade(label = 'Help',menu = help_menu)

        # add tab
        tab_control = ttk.Notebook(self.win)
        tab_control.grid(row = 0,column = 0)

        tab1 = tk.Frame(tab_control)
        tab1.grid(row = 0,column = 0)
        tab_control.add(tab1,text = 'Tab1')

        self.tab2 = tk.Frame(tab_control)
        self.tab2.grid(row = 0,column = 0,sticky = 'WE')
        tab_control.add(self.tab2,text = 'Tab2')

        tab3 = tk.Frame(tab_control,bg = 'blue')
        tab3.grid(row = 0,column = 0)
        tab_control.add(tab3,text = 'tab3')

        # 增加 canvas
        for orange_color in range(2):
            canvas = tk.Canvas(tab3,width = 206,height = 131,highlightthickness = 0,bg = 'orange')
            canvas.grid(row = orange_color,column = orange_color)

        # 增加 levelFrame

        monty = ttk.LabelFrame(tab1,text = ' Monty Python ')
        monty.grid(row = 0,column = 0,padx = 10,pady = 5)

        label_frame = ttk.LabelFrame(self.tab2,text = 'The Snake')
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
        self.button1 = ttk.Button(monty,text = 'Click Me!',command = self.click_me)
        self.button1.grid(row = 1,column = 2)

        # 添加输入框
        self.name = tk.StringVar()
        entry1 = ttk.Entry(monty,width = 24,textvariable = self.name)
        entry1.grid(row = 1,column = 0,sticky = tk.W)

        # 设置光标一开始就在输入框内
        entry1.focus()

        # 添加下拉列表框
        self.num = tk.StringVar()
        combobox1 = ttk.Combobox(monty,width = 14,textvariable = self.num)
        combobox1['values'] = (1,2,4,42,100)
        combobox1.grid(row = 1,column = 1)
        combobox1.current(0)

        # 添加复选按钮
        self.check_button_flag_1 = tk.IntVar()
        check1 = tk.Checkbutton(label_frame,text = 'Disabled',variable = self.check_button_flag_1,state = 'disabled')
        check1.select()
        check1.grid(row = 2,column = 0,sticky = 'W')

        self.check_button_flag_2 = tk.IntVar()
        check2 = tk.Checkbutton(label_frame,text = 'UnChecked',variable = self.check_button_flag_2)
        check2.deselect()
        check2.grid(row = 2,column = 1,sticky = 'W')

        self.check_button_flag_3 = tk.IntVar()
        check3 = tk.Checkbutton(label_frame,text = 'Enabled',variable = self.check_button_flag_3)
        check3.select()
        check3.grid(row = 2,column = 2,sticky = 'W')

        # 添加单选按钮
        self.rad_var = tk.IntVar()
        # 设置一个不存在的值，不然一开始就会选中第一个单选按钮
        self.rad_var.set(99)
        for col in range(3):
            cur_cad = 'rad' + str(col)
            cur_cad = tk.Radiobutton(label_frame,text = colors[col],variable = self.rad_var,value = col,command = self.rad_call)
            cur_cad.grid(row = 5,column = col,sticky = tk.W)

        # 添加下拉滚动条
        # 在换行时，以单词为分界点，就是说在换行时不会分割单词
        self.scr = scrolledtext.ScrolledText(monty,width = scrolW,height = scrolH,wrap = tk.WORD)
        self.scr.grid(column = 0,columnspan = 3,row = 4,sticky = 'WE')

        # adding a spinbox widget
        self.spin = tk.Spinbox(monty,values = (1,2,4,42,100),width = 5,bd = 8,command = lambda:self._spin(self.spin))
        self.spin.grid(row = 2,column = 0,sticky = 'w')

        '''
        the relief param have four values to choose:
        default is tk.SUNKEN
        except is tk.RAISED,tk.FLAT,tk.GROOVE,tk.RIDGE
        '''
        # spin2 = tk.Spinbox(monty,values = (0,50,100),width = 5,bd = 8,command = lambda:self._spin(spin2),relief = tk.RIDGE)
        # spin2.grid(row = 2,column = 1)

        # labelFrame 中所有部件设置

        for child in monty.winfo_children():
            child.grid_configure(padx = 5,pady = 2)

        for child in label_frame2.winfo_children():
            child.grid_configure(padx = 5,pady = 4)

if __name__ == '__main__':
    gui = GUI()
