# -*- coding: utf-8 -*-
# Date: 2021/06/13

from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

from pymysql import connect
import datetime


def connect_mysql():
    """连接数据库"""
    host = "localhost"
    port = 3306
    user = "root"
    password = "yang,."
    database = "hotel"
    charset = "utf8"
    try:
        conn = connect(host=host, port=port, user=user, password=password,
                       database=database, charset=charset)
        cursor = conn.cursor()
        return cursor, conn
    except:
        messagebox.showwarning("警告", "连接数据库失败，请检查数据库连接！")
        return


class HMS(object):
    def __init__(self):
        self.root = Tk()
        self.root.geometry("980x680+275+60")
        self.root.title("酒店管理系统")
        self.root.configure(bg="white")
        self.root.iconbitmap("22.ico")
        self.logo = PhotoImage(file="logo.png")
        self.var = BooleanVar()
        self.user = StringVar()
        self.pwd = StringVar()

    def add_label(self):
        """添加界面标签"""
        label_logo = Label(self.root, bg="white", image=self.logo)
        label_logo.place(x=20, y=40, )

        label_text1 = Label(self.root, text='欢 迎 进 入',
                            bg="white",
                            font=("Source Code Pro", 30, "bold"))
        label_text1.place(x=430, y=60)

        label_text2 = Label(self.root, text="酒 店 管 理 系 统", bg="white",
                            font=("Source Code Pro", 30, "bold"))
        label_text2.place(x=520, y=128)

        label_english1 = Label(self.root, text='Welcome to the', bg="white",
                               font=("Source Code Pro", 20, "normal"))
        label_english1.place(x=430, y=190)

        label_english2 = Label(self.root, text='Hotel management system',
                               bg="white",
                               font=("Source Code Pro", 20, "normal"))
        label_english2.place(x=510, y=243)

    def add_rl_menu(self):
        """添加用户名，密码登陆界面"""
        # 框架
        frame1 = Frame(self.root, bg="white", width=600, height=120)
        frame1.place(x=310, y=350)

        # 登陆文本框
        user_l = Label(frame1, text="用户名:", bg="white",
                       font=("Source Code Pro", 16, "bold"))
        user_l.place(x=10, y=5)

        user_e = Entry(frame1, bd=3, font=10, textvariable=self.user)
        user_e.place(x=105, y=8, height=30, width=240)

        pwd_l = Label(frame1, text="密  码:", bg="white",
                      font=("Source Code Pro", 16, "bold"))
        pwd_l.place(x=7, y=65)

        pwd_e = Entry(frame1, bd=3, font=10, show="*", textvariable=self.pwd)
        pwd_e.place(x=105, y=70, height=30, width=240)

    def add_radiobutton(self):
        """添加选项按钮，用户/管理员模式"""
        frame2 = Frame(self.root, bg="white", width=600, height=50)
        frame2.place(x=310, y=465)

        user_bu = Radiobutton(frame2, bg="white", text="员工", variable=self.var, value=False,
                              font=("Source Code Pro", 14, "bold"))
        user_bu.place(x=55, y=7)

        manager_bu = Radiobutton(frame2, bg="white", text="管理员", variable=self.var, value=True,
                                 font=("Source Code Pro", 14, "bold"))
        manager_bu.place(x=240, y=7)

    def add_rl_button(self):
        """添加注册，登陆按钮"""
        frame3 = Frame(self.root, bg="white", width=600, height=50)
        frame3.place(x=310, y=540)

        # 添加按钮
        # 注册按钮
        register = Button(frame3, bg="white", text="注册",
                          font=("Source Code Pro", 14, "bold"),
                          command=self.register_menu)
        register.place(x=50, y=5, height=35, width=100)
        # 登陆按钮
        login = Button(frame3, bg="white", text="登陆",
                       font=("Source Code Pro", 14, "bold"),
                       command=self.login_examine)
        login.place(x=250, y=5, height=35, width=100)

    def login_examine(self):
        """登陆检查"""
        try:
            cursor, conn = connect_mysql()

            user = self.user.get()
            pwd = self.pwd.get()
            # print(var.get())
            # print(user.get(), pwd.get())
            if len(self.user.get()) == 0:
                if len(self.pwd.get()) == 0:
                    messagebox.showwarning("提示", "请输入用户名和密码！")
                    cursor.close()
                    conn.close()
                    return
                else:
                    messagebox.showwarning("提示", "请输入用户名！")
                    cursor.close()
                    conn.close()
                    return
            else:
                if len(self.pwd.get()) == 0:
                    messagebox.showwarning("提示", "请输入密码！")
                    cursor.close()
                    conn.close()
                    return
            administrator = self.var.get()  # 选项按钮的值
            # 管理员模式
            if administrator:

                cursor.execute("select * from administrator")
                ad_info = cursor.fetchall()

                for ad in ad_info:
                    if ad[0] == user:
                        if ad[1] == pwd:
                            messagebox.showinfo("提示", "登陆成功！")
                            self.administrator_opereate_menu()
                            break
                        else:
                            messagebox.showwarning("提示", "密码错误!")
                            break
                else:
                    messagebox.showwarning("提示", "用户不存在！")
            # 用户模式
            else:

                cursor.execute("select * from user")
                ad_info = cursor.fetchall()
                for ad in ad_info:
                    if ad[0] == user:
                        if ad[1] == pwd:
                            messagebox.showinfo("提示", "登陆成功！")
                            self.user_operate_menu()
                            break
                        else:
                            messagebox.showwarning("提示", "密码错误！")
                            break
                else:
                    messagebox.showwarning("提示", "用户不存在！")
            cursor.close()
            conn.close()
        except:
            return

    def register_examine(self, register_container, *args):
        """注册检查"""
        try:
            cursor, conn = connect_mysql()
            sno = args[0].get()
            sname = args[1].get()
            sid = args[2].get()
            user = args[3].get()
            pwd = args[4].get()
            pwd2 = args[5].get()

            if len(sno) == 0 or len(sname) == 0 or len(sid) == 0 \
                    or len(user) == 0 or len(pwd) == 0 or len(pwd2) == 0:
                messagebox.showwarning("提示", "请输入完整信息!")
                cursor.close()
                conn.close()
                return

            cursor.execute("select sno,sname,sid from staff")
            staff_info = cursor.fetchall()
            for staff in staff_info:
                if sno == staff[0]:
                    if sname == staff[1] and sid == staff[2]:
                        break
                    else:
                        messagebox.showwarning("提示", "员工信息有误!")
                        cursor.close()
                        conn.close()
                        return

            else:
                messagebox.showwarning("提示", "该员工信息不存在!")
                cursor.close()
                conn.close()
                return
            cursor.execute("select user_name from user")
            user_info = cursor.fetchall()
            # print(user_info)
            for info in user_info:
                if user == info[0]:
                    messagebox.showwarning("提示", "该用户名已存在, 请重试！")
                    cursor.close()
                    conn.close()
                    return

            if len(user) > 10:
                messagebox.showwarning("提示", "用户名过长，请输入长度为10以内的字符！")
                cursor.close()
                conn.close()
                return
            if pwd != pwd2:
                messagebox.showwarning("提示", "两次密码输入不一致, 请仔细检查！")
                cursor.close()
                conn.close()
                return
            else:
                try:
                    remarks = f"该用户由员工{sname}({sno})创建"
                    cursor.execute("insert into user(user_name, pwd, rtime, remarks) values('%s', '%s', '%s', '%s')"
                                   % (user, pwd, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), remarks))
                    conn.commit()
                    messagebox.showinfo("提示", "注册成功，请返回主界面登陆！")
                    cursor.close()
                    conn.close()
                    register_container.destroy()
                    self.root.deiconify()
                    return
                except:
                    messagebox.showerror("错误", "注册失败，请重试！")
                    cursor.close()
                    conn.close()
                    return
        except:
            return

    def register_menu(self):
        """注册界面"""
        # self.root.withdraw()
        if self.var.get():
            messagebox.showwarning("警告", "管理员只能由管理员添加, 不允许注册！")
            return
        self.root.iconify()
        register_container = Toplevel()
        # Popup = Toplevel(root)
        # register_container.attributes("-toolwindow", 1)
        # register_container.wm_attributes("-topmost", 2)
        register_container.title("员工注册界面")
        register_container.geometry("450x560+390+100")
        register_container.iconbitmap("22.ico")
        sno = StringVar()
        sname = StringVar()
        sid = StringVar()
        user = StringVar()
        pwd = StringVar()
        pwd2 = StringVar()
        param = [sno, sname, sid, user, pwd, pwd2]

        sno_l = Label(register_container, text="员 工 号:",
                      font=("Source Code Pro", 16, "bold"))
        sno_l.place(x=60, y=30)

        sno_e = Entry(register_container, font=10, textvariable=sno)
        sno_e.place(x=175, y=30, height=30, width=200)

        sname_l = Label(register_container, text="姓    名:",
                        font=("Source Code Pro", 16, "bold"))
        sname_l.place(x=60, y=100)

        sname_e = Entry(register_container, font=10, textvariable=sname)
        sname_e.place(x=175, y=100, height=30, width=200)

        sid_l = Label(register_container, text="身份证号:",
                      font=("Source Code Pro", 17, "bold"))
        sid_l.place(x=60, y=160)

        sid_e = Entry(register_container, font=10, textvariable=sid)
        sid_e.place(x=175, y=160, height=30, width=200)

        user_l = Label(register_container, text="用 户 名:",
                       font=("Source Code Pro", 16, "bold"))
        user_l.place(x=60, y=230)

        user_e = Entry(register_container, font=10, textvariable=user)
        user_e.place(x=175, y=230, height=30, width=200)

        pwd_l = Label(register_container, text="密    码:",
                      font=("Source Code Pro", 16, "bold"))
        pwd_l.place(x=60, y=300)

        pwd_e = Entry(register_container, font=10, show="*", textvariable=pwd)
        pwd_e.place(x=175, y=300, height=30, width=200)

        pwd_l2 = Label(register_container, text="再次输入:",
                       font=("Source Code Pro", 17, "bold"))
        pwd_l2.place(x=60, y=360)

        pwd_e2 = Entry(register_container, font=10, show="*", textvariable=pwd2)
        pwd_e2.place(x=175, y=360, height=30, width=200)

        register = Button(register_container, text="注册",
                          command=lambda: self.register_examine(register_container, *param),
                          font=("Source Code Pro", 14, "bold"))
        register.place(x=120, y=450, height=35, width=100)

        quitbu = Button(register_container, text="退出",
                        command=lambda: self.register_closing(register_container),
                        font=("Source Code Pro", 14, "bold"))
        quitbu.place(x=280, y=450, height=35, width=100)

        register_container.protocol('WM_DELETE_WINDOW', lambda: self.register_closing(register_container))
        register_container.mainloop()

    def user_operate_menu(self):
        """员工操作界面"""
        self.root.iconify()
        operation_container = Toplevel()
        operation_container.title("员工操作界面")
        operation_container.geometry("500x510+390+25")
        operation_container.iconbitmap("22.ico")
        menubar = Menu(operation_container)
        # 建立最上层菜单

        # 建立菜单类别对象,并将此莱单类别命名为File
        filemenu = Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)  # 在File菜单内建立菜单列表
        filemenu.add_command(label="New File", )
        filemenu.add_command(label="Exit! ",
                             command=lambda: self.user_operation_closing(operation_container))
        # 设置菜单
        editmenu = Menu(menubar)
        menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="settings")

        # 帮助菜单
        helpmenu = Menu(menubar)
        menubar.add_cascade(label="help", menu=helpmenu)
        helpmenu.add_command(label="About me", command=self.help_munu)

        operation_container.config(menu=menubar)
        # 显示菜单对象
        operation_container.protocol('WM_DELETE_WINDOW', lambda: self.register_closing(operation_container))

        # 查询界面
        select_frame = LabelFrame(operation_container, text="查询",
                                  font=("Source Code Pro", 16, "normal"))
        customer = Button(select_frame, text="查询所有客户的信息",
                          font=("Source Code Pro", 16, "normal"),
                          command=self.customer)
        customer.place(x=70, y=30, height=40, width=260)

        room_empty = Button(select_frame, text="查询所有空房间的信息",
                            font=("Source Code Pro", 16, "normal"),
                            command=self.room)
        room_empty.place(x=70, y=100, height=40, width=260)

        record_name = Button(select_frame, text="按姓名查询入住记录",
                             font=("Source Code Pro", 16, "normal"),
                             command=self.record_menu)
        record_name.place(x=70, y=170, height=40, width=260)

        price_sn = Button(select_frame, text="计算用户住房费用",
                          font=("Source Code Pro", 16, "normal"),
                          command=self.room_menu)
        price_sn.place(x=70, y=240, height=40, width=260)

        department = Button(select_frame, text="查询所有部门的信息",
                            font=("Source Code Pro", 16, "normal"),
                            command=self.department)
        department.place(x=70, y=310, height=40, width=260)

        # 查询的框框架显示
        select_frame.place(x=35, y=50, height=410, width=400)

    def administrator_opereate_menu(self):
        self.root.iconify()
        operation_container = Toplevel()
        operation_container.title("管理员操作界面")
        operation_container.geometry("500x710+390+25")
        operation_container.iconbitmap("22.ico")
        menubar = Menu(operation_container)
        # 建立最上层菜单

        # 建立菜单类别对象,并将此莱单类别命名为File
        filemenu = Menu(menubar)
        menubar.add_cascade(label="File", menu=filemenu)  # 在File菜单内建立菜单列表
        filemenu.add_command(label="New File", )
        filemenu.add_command(label="Exit! ",
                             command=lambda: self.administrator_operation_closing(operation_container))
        # 设置菜单
        editmenu = Menu(menubar)
        menubar.add_cascade(label="Edit", menu=editmenu)
        editmenu.add_command(label="settings")

        # 帮助菜单
        helpmenu = Menu(menubar)
        menubar.add_cascade(label="help", menu=helpmenu)
        helpmenu.add_command(label="About me", command=self.help_munu)

        operation_container.config(menu=menubar)
        # 显示菜单对象
        operation_container.protocol('WM_DELETE_WINDOW', lambda: self.register_closing(operation_container))

        # 查询界面
        select_frame = LabelFrame(operation_container, text="查询",
                                  font=("Source Code Pro", 16, "normal"))
        customer = Button(select_frame, text="查询所有客户的信息",
                          font=("Source Code Pro", 16, "normal"),
                          command=self.customer)
        customer.place(x=70, y=30, height=40, width=260)

        room_empty = Button(select_frame, text="查询所有空房间的信息",
                            font=("Source Code Pro", 16, "normal"),
                            command=self.room)
        room_empty.place(x=70, y=100, height=40, width=260)

        record_name = Button(select_frame, text="按姓名查询入住记录",
                             font=("Source Code Pro", 16, "normal"),
                             command=self.record_menu)
        record_name.place(x=70, y=170, height=40, width=260)

        price_sn = Button(select_frame, text="计算用户住房费用",
                          font=("Source Code Pro", 16, "normal"),
                          command=self.room_menu)
        price_sn.place(x=70, y=240, height=40, width=260)

        department = Button(select_frame, text="查询所有部门的信息",
                            font=("Source Code Pro", 16, "normal"),
                            command=self.department)
        department.place(x=70, y=310, height=40, width=260)

        # 查询的框框架显示
        select_frame.place(x=35, y=50, height=410, width=400)

        ad_frame = LabelFrame(operation_container, text="管理员操作",
                              font=("Source Code Pro", 16, "normal"))
        user_m = Button(ad_frame, text="删除用户",
                        font=("Source Code Pro", 16, "normal"),
                        command=lambda: self.delete_user(operation_container))
        user_m.place(x=70, y=30, height=40, width=260)
        add_ad = Button(ad_frame, text="添加管理员",
                        font=("Source Code Pro", 16, "normal"),
                        command=lambda: self.add_administrator(operation_container))
        add_ad.place(x=70, y=100, height=40, width=260)
        ad_frame.place(x=35, y=480, height=200, width=400)

    def add_administrator(self, operation_container):
        temp = Toplevel(operation_container)
        temp.title("添加管理员")
        temp.iconbitmap("22.ico")
        user = StringVar()
        pwd = StringVar()
        accountL = Label(temp, text="用户名",
                         font=("Source Code Pro", 16, "normal"))
        accountL.grid(row=0)
        pwdL = Label(temp, text="密码",
                     font=("Source Code Pro", 16, "normal"))
        pwdL.grid(row=1)

        accountE = Entry(temp, textvariable=user, font=10)
        pwdE = Entry(temp, textvariable=pwd, show="*", font=10)
        accountE.grid(row=0, column=1)
        pwdE.grid(row=1, column=1)
        loginbtn = Button(temp, text="添加",
                          font=("Source Code Pro", 16, "normal"),
                          command=lambda: self.add_examine(temp, user, pwd))
        quitbtn = Button(temp, text="退出", command=temp.destroy,
                         font=("Source Code Pro", 16, "normal"))
        loginbtn.grid(row=2, column=0, sticky=E, pady=5)
        quitbtn.grid(row=2, column=1, sticky=E, pady=5)

    def add_examine(self, temp, user, pwd):
        try:
            user = user.get()
            pwd = pwd.get()
            if len(user) == 0 or len(pwd) == 0:
                messagebox.showwarning("提示", "请输入完整信息!")
                return
            cursor, conn = connect_mysql()
            cursor.execute("select user_name from administrator")
            ad_info = cursor.fetchall()
            for ad in ad_info:
                if user == ad[0]:
                    messagebox.showwarning("提示", "该用户名已存在, 请重试！")
                    cursor.close()
                    conn.close()
                    return
            if len(user) > 10:
                messagebox.showwarning("提示", "用户名过长，请输入长度为10以内的字符！")
                cursor.close()
                conn.close()
                return
            try:

                cursor.execute("insert into administrator(user_name, pwd, rtime) values('%s', '%s', '%s')"
                               % (user, pwd, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                conn.commit()
                messagebox.showinfo("提示", "注册成功，请返回主界面登陆！")
                cursor.close()
                conn.close()
                temp.destroy()
                return
            except:
                messagebox.showerror("错误", "注册失败，请重试！")
                cursor.close()
                conn.close()
                return
        except:
            return

    def delete_user(self, operation_container):
        temp = Toplevel(operation_container)
        temp.title("添加管理员")
        temp.iconbitmap("22.ico")
        label = Label(temp, text="请输入要删除的用户名：",
                      font=("Source Code Pro", 16, "normal"))
        label.grid(row=0)
        user = StringVar()
        entry = Entry(temp,textvariable=user, font=10)
        entry.grid(row=0, column=1)

        ok = Button(temp, text="确定",font=("Source Code Pro", 16, "normal"),
                    command=lambda :self.deleteuser(user, temp))
        ok.grid(row=1, column=1)

    def deleteuser(self, user, temp):
        user = user.get()
        if len(user) == 0:
            messagebox.showwarning("提示", "请输入用户名！")
            return
        try:
            cursor, conn = connect_mysql()
            cursor.execute("select user_name from user")
            ad_info = cursor.fetchall()
            # print(ad_info)
            for ad in ad_info:
                if user == ad[0]:
                    cursor.execute("delete from user where user_name='%s'" % user)
                    conn.commit()
                    messagebox.showinfo("提示", "删除成功!")
                    cursor.close()
                    conn.close()
                    temp.destroy()
                    return
            messagebox.showwarning("提示", "找不到该用户！")
            cursor.close()
            conn.close()
            return
        except:
            return
    def customer(self):
        """查客户信息"""
        try:
            cursor, conn = connect_mysql()
            cursor.execute("select * from custermer")
            customer_info = cursor.fetchall()
            # print(customer_info)

            temp = Toplevel()
            temp.title("用户信息")
            temp.iconbitmap("22.ico")
            # 建立Treeview
            tree = Treeview(temp, show="headings",
                            columns=("sno", "cname", "csex", "cage", "isVip", "ccid", "cphone"))  # 建立栏标题
            tree.heading("#0", text="Sno")
            # 图标栏
            tree.heading("#1", text="Sno")
            tree.heading("#2", text="Cname")
            tree.heading("#3", text="Csex")  # 格式化栏位
            tree.heading("#4", text="Cage")
            tree.heading("#5", text="isVip")
            tree.heading("#6", text="Ccid")
            tree.heading("#7", text="Cphone")
            tree.column("#1", anchor=CENTER, width=150)
            tree.column("#2", anchor=CENTER, width=150)  # 建立内容
            tree.column("#3", anchor=CENTER, width=150)  # 建立内容
            tree.column("#4", anchor=CENTER, width=150)  # 建立内容
            tree.column("#5", anchor=CENTER, width=150)  # 建立内容
            tree.column("#6", anchor=CENTER, width=150)  # 建立内容
            tree.column("#7", anchor=CENTER, width=150)  # 建立内容
            tree.tag_configure("color", background="lightblue")
            for customer in customer_info:

                if customer[4] == 1:
                    tree.insert("", index=END, text=1, tags=("color"),
                                values=(customer[0], customer[1], customer[2],
                                        customer[3], customer[4], customer[5], customer[6]))
                else:
                    tree.insert("", index=END,
                                values=(customer[0], customer[1], customer[2],
                                        customer[3], customer[4], customer[5], customer[6]))
            # tree.insert("", index=END, text="加州", values=("洛杉矶”, "1000"))
            # tree.insert("", index=END, text="江苏", values=("南京", "900"))
            cursor.close()
            conn.close()
            tree.pack()
            # 显示菜单对象
            temp.mainloop()
        except:
            return

    def room(self):
        """查房间信息"""
        try:
            cursor, conn = connect_mysql()
            cursor.execute("select * from room where rstate='F'")
            customer_info = cursor.fetchall()

            temp = Toplevel()
            temp.title("空房信息")
            temp.iconbitmap("22.ico")
            # 建立Treeview
            tree = Treeview(temp, show="headings",
                            columns=("rnum", "rtype", "rprice", "rstate", "sno"))  # 建立栏标题

            # 图标栏
            tree.heading("#1", text="rnum")
            tree.heading("#2", text="rtype")
            tree.heading("#3", text="rprice")  # 格式化栏位
            tree.heading("#4", text="rstate")
            tree.heading("#5", text="sno")
            # tree.heading("#6", text="Ccid")
            # tree.heading("#7", text="Cphone")

            tree.column("#1", anchor=CENTER, width=150)
            tree.column("#2", anchor=CENTER, width=150)  # 建立内容
            tree.column("#3", anchor=CENTER, width=150)  # 建立内容
            tree.column("#4", anchor=CENTER, width=150)  # 建立内容
            tree.column("#5", anchor=CENTER, width=150)  # 建立内容
            # tree.column("#6", anchor=CENTER, width=150)  # 建立内容
            # tree.column("#7", anchor=CENTER, width=150)  # 建立内容
            for customer in customer_info:
                tree.insert("", index=END, text=1,
                            values=(customer[0], customer[1], customer[2],
                                    customer[3], customer[4]))

            # tree.insert("", index=END, text="加州", values=("洛杉矶”, "1000"))
            # tree.insert("", index=END, text="江苏", values=("南京", "900"))
            cursor.close()
            conn.close()
            tree.pack()
            # 显示菜单对象
            temp.mainloop()
        except:
            return

    def record_menu(self):
        """入住记录查询页面"""
        temp = Toplevel()
        temp.title("入住记录")
        temp.iconbitmap("22.ico")
        temp.geometry("900x300")
        # 建立Treeview
        var = StringVar()
        sname = Label(temp, text="Sname:", font=10)
        sname.place(x=290, y=10)
        sname_e = Entry(temp, textvariable=var, font=10)
        sname_e.place(x=345, y=10)

        find = Button(temp, text="search", command=lambda: self.record(var, temp))
        find.place(x=530, y=8)

    def record(self, var, temp):
        """入住记录操作"""
        cursor, conn = connect_mysql()
        ret = cursor.execute("select cname, record.cno, rnum,"
                             "rin, rout, rockpost"
                             " from record,custermer where cname='%s'"
                             "and record.cno=custermer.cno" % var.get())
        if ret == 0:
            messagebox.showwarning("提示", "没有该客户入住记录！")
            cursor.close()
            conn.close()
            return
        customer_info = cursor.fetchall()

        frame = Frame(temp)
        frame.place(x=0, y=40)
        tree = Treeview(frame, show="headings",
                        columns=("cname", "cno", "rnum", "rin", "rout", "post"))  # 建立栏标题

        # 图标栏

        tree.heading("#1", text="Cname")
        tree.heading("#2", text="Cno")
        tree.heading("#3", text="Rnum")
        tree.heading("#4", text="Rin")  # 格式化栏位
        tree.heading("#5", text="Rout")
        tree.heading("#6", text="post")
        # tree.heading("#6", text="Ccid")
        # tree.heading("#7", text="Cphone")

        tree.column("#1", anchor=CENTER, width=150)
        tree.column("#2", anchor=CENTER, width=150)  # 建立内容
        tree.column("#3", anchor=CENTER, width=150)  # 建立内容
        tree.column("#4", anchor=CENTER, width=150)  # 建立内容
        tree.column("#5", anchor=CENTER, width=150)  # 建立内容
        tree.column("#6", anchor=CENTER, width=150)  # 建立内容
        # tree.column("#6", anchor=CENTER, width=150)  # 建立内容
        # tree.column("#7", anchor=CENTER, width=150)  # 建立内容
        for customer in customer_info:
            tree.insert("", index=END, text=1,
                        values=(customer[0], customer[1], customer[2],
                                customer[3], customer[4], customer[5]))

        # tree.insert("", index=END, text="加州", values=("洛杉矶”, "1000"))
        # tree.insert("", index=END, text="江苏", values=("南京", "900"))
        cursor.close()
        conn.close()
        tree.pack()

        temp.mainloop()

    def room_menu(self):
        """价格计算界面"""
        temp = Toplevel()
        temp.title("房间价格")
        temp.iconbitmap("22.ico")
        temp.geometry("600x300")
        # 建立Treeview
        var = StringVar()
        sname = Label(temp, text="Cno:", font=10)
        sname.place(x=150, y=10)
        sname_e = Entry(temp, textvariable=var, font=10)
        sname_e.place(x=190, y=10)

        find = Button(temp, text="search", command=lambda: self.price(var, temp))
        find.place(x=365, y=7)

    def price(self, var, temp):
        """价格计算操作"""
        try:
            cursor, conn = connect_mysql()
            try:
                ret = cursor.execute("select priceview.cno, cname, priceview.rnum, round(hour / 24) * rprice as price" \
                                     " from priceview, romview, custermerview " \
                                     "where custermerview.cno = priceview.cno and " \
                                     "priceview.rnum = romview.rnum and priceview.cno = %d" % int(var.get()))
                if ret == 0:
                    messagebox.showwarning("提示", "没有该客户入住记录！")
                    cursor.close()
                    conn.close()
                    return
                customer_info = cursor.fetchall()

                frame = Frame(temp)
                frame.place(x=0, y=40)
                tree = Treeview(frame, show="headings",
                                columns=("cno", "cname", "rnum", "price"))  # 建立栏标题

                # 图标栏
                tree.heading("#1", text="Cno")
                tree.heading("#2", text="Cname")
                tree.heading("#3", text="Rnum")
                tree.heading("#4", text="Price")

                # tree.heading("#6", text="Ccid")
                # tree.heading("#7", text="Cphone")

                tree.column("#1", anchor=CENTER, width=150)
                tree.column("#2", anchor=CENTER, width=150)  # 建立内容
                tree.column("#3", anchor=CENTER, width=150)  # 建立内容
                tree.column("#4", anchor=CENTER, width=150)  # 建立内容
                # tree.column("#6", anchor=CENTER, width=150)  # 建立内容
                # tree.column("#7", anchor=CENTER, width=150)  # 建立内容
                for customer in customer_info:
                    tree.insert("", index=END, text=1,
                                values=(customer[0], customer[1], customer[2],
                                        customer[3]))

                # tree.insert("", index=END, text="加州", values=("洛杉矶”, "1000"))
                # tree.insert("", index=END, text="江苏", values=("南京", "900"))
                cursor.close()
                conn.close()
                tree.pack()
            except:
                messagebox.showwarning("提示", "请输入正确编号！")
        except:
            return

    def department(self):
        """查询部门信息"""
        cursor, conn = connect_mysql()
        cursor.execute("select * from dpartment")
        customer_info = cursor.fetchall()

        temp = Toplevel()
        temp.title("部门信息")
        temp.iconbitmap("22.ico")
        # 建立Treeview
        tree = Treeview(temp, show="headings",
                        columns=("dno", "dname", "dmanager"))  # 建立栏标题

        # 图标栏
        tree.heading("#1", text="Dno")
        tree.heading("#2", text="Dname")
        tree.heading("#3", text="Dmanager")  # 格式化栏位

        # tree.heading("#6", text="Ccid")
        # tree.heading("#7", text="Cphone")

        tree.column("#1", anchor=CENTER, width=150)
        tree.column("#2", anchor=CENTER, width=150)  # 建立内容
        tree.column("#3", anchor=CENTER, width=150)  # 建立内容
        # 建立内容
        # tree.column("#6", anchor=CENTER, width=150)  # 建立内容
        # tree.column("#7", anchor=CENTER, width=150)  # 建立内容

        for customer in customer_info:
            tree.insert("", index=END, text=1, tags="color",
                        values=(customer[0], customer[1], customer[2]))

        # tree.insert("", index=END, text="加州", values=("洛杉矶”, "1000"))
        # tree.insert("", index=END, text="江苏", values=("南京", "900"))
        tree.pack()
        # 显示菜单对象
        temp.mainloop()

    def help_munu(self):
        """帮助界面"""
        messagebox.showinfo("help", "具体使用帮助请查看用户手册！\n\n                --version=0.0.0")

    def root_closing(self):
        """关闭root"""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def register_closing(self, register_container):
        """关闭注册界面"""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.wm_state("normal")
            self.root.deiconify()  # 和iconify配合可以
            self.user.set('')
            self.pwd.set('')
            register_container.destroy()

    def user_operation_closing(self, operation_container):
        """关闭员工操作界面"""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.deiconify()  # 和iconify配合可以
            self.user.set('')
            self.pwd.set('')
            operation_container.destroy()

    def administrator_operation_closing(self, operation_container):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.deiconify()  # 和iconify配合可以
            self.user.set('')
            self.pwd.set('')
            operation_container.destroy()

    def root_mainloop(self):
        self.root.protocol('WM_DELETE_WINDOW', self.root_closing)
        self.root.mainloop()


if __name__ == '__main__':
    hotel_manage_system = HMS()
    hotel_manage_system.add_label()
    hotel_manage_system.add_rl_menu()
    hotel_manage_system.add_radiobutton()
    hotel_manage_system.add_rl_button()
    hotel_manage_system.root_mainloop()
