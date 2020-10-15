import tkinter as tk
from tkinter import messagebox

def start_Login():
    global root
    root = tk.Tk()
    top = LoginWin(root)
    root.mainloop()

class LoginWin:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Courier New} -size 14"
        font11 = "-family {Segoe UI} -size 15 -weight bold"
        font9 = "-family {Segoe UI} -size 14 -weight bold"
        
        top.geometry("393x334+430+143")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Login Window")
        top.configure(background="#d9d9d9")
        
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.204, rely=0.06, height=28, width=227)
        self.Label1.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font11,foreground="#000000",
        text='''California Pizza POS''')
        
        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.28, rely=0.269,height=40, relwidth=0.57)
        self.Entry1.configure(background="white",disabledforeground="#a3a3a3",font=font10,
        foreground="#000000",insertbackground="black")
        
        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.285, rely=0.494,height=40, relwidth=0.57)
        self.Entry2.configure(background="white",disabledforeground="#a3a3a3",font=font10,foreground="#000000",
        highlightbackground="#f0f0f0f0f0f0",insertbackground="black",show="*")
        
        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.025, rely=0.323, height=21, width=59)
        self.Label2.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font9,foreground="#000000",text='''Name''')
        
        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.025, rely=0.536, height=21, width=81)
        self.Label3.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font9,foreground="#000000",text='''Password''')
        
        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.204, rely=0.698, height=44, width=90)
        self.Button1.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font9,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Confirm''',
        command=self.ConfirmLogin)
        
        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.534, rely=0.698, height=44, width=89)
        self.Button2.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font9,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Exit''',command=self.Exit)
    
    def Exit(self):
        root.destroy()

    def ConfirmLogin(self):
        infile = open("C:\\Users\\hp\\Desktop\\OOP mids\\Username.txt", "r")
        con1 = infile.read()
        con11 = con1.split()
        infile2 = open("C:\\Users\\hp\\Desktop\\OOP mids\\Password.txt", "r")
        con2 = infile2.read()
        con22 = con2.split()
        infile.close()
        if self.Entry1.get() == "" or self.Entry2.get() == "":
            messagebox.showerror("Error", "All fields are required for login")
        elif self.Entry1.get() == con11[0] and self.Entry2.get() == con22[0]:
            messagebox.showinfo("ATFS", "Login Successfull")
            root.destroy()
            import win2
            win2.start_Home()
        elif self.Entry1.get() == con11[1] and self.Entry2.get() == con22[1]:
            messagebox.showinfo("ATFS", "Login Successfull")
            root.destroy()
            import win2
            win2.start_Home()
        elif self.Entry1.get() == con11[2] and self.Entry2.get() == con22[2]:
            messagebox.showinfo("ATFS", "Login Successfull")
            root.destroy()
            import win2
            win2.start_Home()
        else:
            messagebox.showerror("Error", "Worng username or password")

if __name__ == '__main__':
    start_Login()