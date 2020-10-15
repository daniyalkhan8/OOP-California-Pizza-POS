import tkinter as tk
from tkinter import *
from win5 import CartWin
from tkinter import messagebox
import datetime

def start_Order():
    global root
    root = tk.Tk()
    top = OrderWin(root)
    root.mainloop()

class OrderWin(CartWin):
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 11 -weight bold"
        font9 = "-family {Segoe UI} -size 14 -weight bold"

        top.geometry("661x445+338+157")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Order Window")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.076, rely=0.292, height=31, width=80)
        self.Label1.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font9,foreground="#000000",text='''Flavour''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.076, rely=0.494, height=31, width=86)
        self.Label2.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font9,foreground="#000000",text='''Quantity''')

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.256, rely=0.267,height=40, relwidth=0.324)
        self.Entry1.configure(background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.257, rely=0.472,height=40, relwidth=0.324)
        self.Entry2.configure(background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.076, rely=0.652, height=44, width=97)
        self.Button1.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Add to Cart''',
        command=self.Add)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.272, rely=0.652, height=44, width=97)
        self.Button2.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''View Cart''',command=self.View)

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.378, rely=0.831, height=44, width=97)
        self.Button3.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Home''',command=self.Home)

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.182, rely=0.831, height=44, width=97)
        self.Button4.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Reset''',command=self.Reset)

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.469, rely=0.652, height=44, width=97)
        self.Button5.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Generate Slip''',
        command=self.Generate)

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.655, rely=0.124, relheight=0.849, relwidth=0.31)
        self.Text1.configure(background="white",font="TkTextFont",foreground="black",highlightbackground="#d9d9d9",highlightcolor="black",
        insertbackground="black",selectbackground="blue",selectforeground="white",wrap="word")

        scrollbar = tk.Scrollbar(top)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.Text1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.Text1.yview)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.696, rely=0.045, height=21, width=153)
        self.Label3.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font9,foreground="#000000",text='''Customer's Slip''')

    def Home(self):
        from pathlib import Path
        f_path = Path("C:\\Users\\hp\\Desktop\\OOP mids\\Cart.txt")
        if (f_path.stat().st_size == 0) == True:
            root.destroy()
            import win2
            win2.start_Home()
        else:
            permit=messagebox.askyesno("Note", "Do you want to cancle the order?")
            if permit > 0:
                open("C:\\Users\\hp\\Desktop\\OOP mids\\Cart.txt", "w").close()
                root.destroy()
                import win2
                win2.start_Home()
            else:
                root.destroy()
                import win2
                win2.start_Home()

    def View(self):
        root.destroy()
        import win5
        win5.start_Cart()

    def Add(self):
        super().Add()
    
    def Reset(self):
        super().Reset()

    def Generate(self):
        from pathlib import Path
        f_path = Path("C:\\Users\\hp\\Desktop\\OOP mids\\Cart.txt")
        if (f_path.stat().st_size == 0) == True:
            messagebox.showinfo("Info", "Cart is empty. Add some items to cart.")
        else:
            cart_set = set()
            import random
            rand = random.randint(3000, 12000)
            self.Text1.delete("1.0", "end")
            infile = open("C:\\Users\\hp\\Desktop\\OOP mids\\PizzaStock.txt", "r")
            con = infile.read().split("\n")
            infile.close()
            infile2 = open("C:\\Users\\hp\\Desktop\\OOP mids\\Cart.txt", "r")
            con2 = infile2.read().split("\n")
            infile2.close()
            con.pop(), con2.pop()
            for j in con2:
                con.remove(j)
                cart_set.add(j)
            outfile = open("C:\\Users\\hp\\Desktop\\OOP mids\\PizzaStock.txt", "w")
            for k in con:
                outfile.write(k+"\n")
            outfile.close()
            open("C:\\Users\\hp\\Desktop\\OOP mids\\Cart.txt", "w").close()
            self.Text1.insert(END,"________________________________________\n")
            self.Text1.insert(END,"                 CALIFORNIA PIZZA\n")
            self.Text1.insert(END,"________________________________________\n")
            self.Text1.insert(END,"                     ORDER RECEIPT\n")
            self.Text1.insert(END,"________________________________________\n")
            now = datetime.datetime.now()
            clock= now.strftime("%Y-%m-%d                                %H:%M:%S")        
            self.Text1.insert(END,"Date:                                               Time: \n{}".format(clock))
            self.Text1.insert(END, "\n                       BillNo:{}".format(rand))
            self.Text1.insert(END,"\n\nPIZZA                                      AMOUNT\n")
            for l in cart_set:
                self.Text1.insert(END, "{}\t\t|\t{}\n".format(l, con2.count(l)))
            ask=messagebox.askyesno("Note", "Do you want to save the bill in file?")
            if ask > 0:
                rec_file = open("C:\\Users\\hp\\Desktop\\OOP mids\\ReciptHistory\\Bill"+str(rand)+".txt", "w")
                rec_file.write(self.Text1.get(1.0, END))
                rec_file.close()
            else:
                pass

if __name__ == '__main__':
    start_Order()