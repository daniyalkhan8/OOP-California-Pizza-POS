import tkinter as tk
from tkinter import messagebox

def start_Inventory():
    global root
    root = tk.Tk()
    top = InventoryWin(root)
    root.mainloop()

class InventoryWin:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 11 -weight bold"
        font9 = "-family {Segoe UI} -size 14 -weight bold"

        top.geometry("600x450+364+154")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Inventory Window")
        top.configure(background="#d9d9d9")

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.633, rely=0.089, relheight=0.742, relwidth=0.307)
        self.Text1.configure(background="white",font="TkTextFont",foreground="black",highlightbackground="#d9d9d9",highlightcolor="black",
        insertbackground="black",selectbackground="blue",selectforeground="white",wrap="word")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.033, rely=0.311, height=31, width=74)
        self.Label1.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font9,foreground="#000000",text='''Flavour''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.033, rely=0.533, height=31, width=84)
        self.Label2.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font9,foreground="#000000",text='''Quantity''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.2, rely=0.289,height=40, relwidth=0.307)
        self.Entry1.configure(background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",
        insertbackground="black")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.2, rely=0.511,height=40, relwidth=0.307)
        self.Entry2.configure(background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",
        insertbackground="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.017, rely=0.867, height=44, width=87)
        self.Button1.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Add''',command=self.Add)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.217, rely=0.867, height=44, width=87)
        self.Button2.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''View''',
        command=self.ViewStock)

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.417, rely=0.867, height=44, width=87)
        self.Button3.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Remove''',
        command=self.Remove)

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.617, rely=0.867, height=44, width=87)
        self.Button4.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",cursor="fleur",
        disabledforeground="#a3a3a3",font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",
        text='''Reset''',command=self.Reset)

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.817, rely=0.867, height=44, width=87)
        self.Button5.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Home''',command=self.Home)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.65, rely=0.022, height=21, width=173)
        self.Label3.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font9,foreground="#000000",text='''Stock Available''')

    def Home(self):
        root.destroy()
        import win2
        win2.start_Home()

    def Add(self):
        try:
            if self.Entry1.get()=="" or self.Entry2.get()=="":
                messagebox.showerror("Error", "Pizza name and quantity both are required.")
            else:
                infile = open("C:\\Users\\hp\\Desktop\\OOP mids\\PizzaStock.txt", "a")
                for i in range(int(self.Entry2.get().strip())):
                    infile.write(self.Entry1.get().strip()+"\n")
                infile.close()
        except Exception:
            messagebox.showerror("Invalid input", "Quantity should be an integer in quantity entry.")
        

    def Reset(self):
        self.Entry1.delete(0, "end")
        self.Entry2.delete(0, "end")
        self.Text1.delete("1.0", "end")    
    
    def ViewStock(self):
        self.Text1.delete("1.0", "end")
        conset = set()
        p_list = []
        infile = open("C:\\Users\\hp\\Desktop\\OOP mids\\PizzaStock.txt", "r")
        con = infile.read()
        infile.close()
        con2 = con.split("\n")
        con2.pop()
        self.Text1.insert(tk.END,"Flavours\t\t           Quantity\n")
        for i in con2:
            conset.add(i)
            p_list.append(i)
        for j in conset:
            self.Text1.insert(tk.END,"{}\t\t|           {}\n".format(j,p_list.count(j)))

    def Remove(self):
        try:
            if self.Entry1.get() == "" or self.Entry2.get() == "":
                messagebox.showerror("Error", "Flavour and quantity both are required.")
            else:
                infile = open("C:\\Users\\hp\\Desktop\\OOP mids\\PizzaStock.txt", "r")
                con = infile.read().split("\n")
                con.pop()
                infile.close()
                for i in range(int(self.Entry2.get())):
                    if self.Entry1.get() not in con:
                        messagebox.showinfo("ATFS", "Flavour not available in stock.")
                        break
                    else:
                        con.remove(self.Entry1.get().strip())
                outfile = open("C:\\Users\\hp\\Desktop\\OOP mids\\PizzaStock.txt", "w")
                for i in con:
                    outfile.write(i+"\n")
                outfile.close()
        except Exception:
            messagebox.showerror("Invalid input", "Quantity should be an integer in quantity entry.")   

if __name__ == '__main__':
    start_Inventory()