import tkinter as tk

def start_Home():
    global root
    root = tk.Tk()
    top = HomeWin(root)
    root.mainloop()

class HomeWin:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 14 -weight bold"
        font11 = "-family {Segoe UI} -size 11 -weight bold"

        top.geometry("253x234+501+223")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Home Page")
        top.configure(background="#d9d9d9")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.237, rely=0.256, height=44, width=137)
        self.Button1.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font11,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Order Window''',
        command=self.Order)

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.237, rely=0.513, height=44, width=137)
        self.Button3.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font11,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Inventory Window''',
        command=self.Inventory)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.233, rely=0.043, height=40, width=143)
        self.Label3.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font10,foreground="#000000",text='''Home Page''')

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.237, rely=0.769, height=44, width=133)
        self.Button2.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font11,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Logout''',
        command=self.Logout)

    def Order(self):
        root.destroy()
        import win3
        win3.start_Order()

    def Inventory(self):
        root.destroy()
        import win4
        win4.start_Inventory()
    
    def Logout(self):
        root.destroy()
        import win1
        win1.start_Login()

if __name__ == '__main__':
    start_Home()