import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox

def start_Cart():
    global root
    root = tk.Tk()
    top = CartWin(root)
    root.mainloop()

class CartWin:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 11 -weight bold"
        font9 = "-family {Segoe UI} -size 14 -weight bold"

        top.geometry("561x431+407+128")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Cart Window")
        top.configure(background="#d9d9d9")

        self.Entry1 = tk.Entry(top)
        self.Entry1.place(relx=0.221, rely=0.241,height=40, relwidth=0.31)
        self.Entry1.configure(background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.221, rely=0.371,height=40, relwidth=0.31)
        self.Entry2.configure(background="white",disabledforeground="#a3a3a3",font="TkFixedFont",foreground="#000000",insertbackground="black")

        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.59, rely=0.139, relheight=0.805, relwidth=0.328)
        self.Text1.configure(background="white",font="TkTextFont",foreground="black",highlightbackground="#d9d9d9",highlightcolor="black",
        insertbackground="black",selectbackground="blue",selectforeground="white",wrap="word")

        scrollbar = tk.Scrollbar(top)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.Text1.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.Text1.yview)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.053, rely=0.255, height=34, width=71)
        self.Label1.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font9,foreground="#000000",text='''Flavour''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.046, rely=0.394, height=23, width=81)
        self.Label2.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font9,foreground="#000000",text='''Quantity''')

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.171, rely=0.831, height=44, width=133)
        self.Button1.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Back''',command=self.Back)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=0.321, rely=0.673, height=44, width=133)
        self.Button2.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",cursor="fleur",
        disabledforeground="#a3a3a3",font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",
        text='''Reset''',command=self.Reset)

        self.Button3 = tk.Button(top)
        self.Button3.place(relx=0.046, rely=0.517, height=44, width=137)
        self.Button3.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Add Items''',command=self.Add)

        self.Button4 = tk.Button(top)
        self.Button4.place(relx=0.321, rely=0.51, height=44, width=135)
        self.Button4.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''Remove Items''',
        command=self.Remove)

        self.Button5 = tk.Button(top)
        self.Button5.place(relx=0.053, rely=0.673, height=44, width=133)
        self.Button5.configure(activebackground="#ececec",activeforeground="#000000",background="#d9d9d9",disabledforeground="#a3a3a3",
        font=font10,foreground="#000000",highlightbackground="#d9d9d9",highlightcolor="black",pady="0",text='''View Cart Items''',
        command=self.View)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.677, rely=0.07, height=21, width=96)
        self.Label3.configure(background="#d9d9d9",disabledforeground="#a3a3a3",font=font9,foreground="#000000",text='''Cart Items''')

    def Back(self):
        root.destroy()
        import win3
        win3.start_Order()

    def Reset(self):
        self.Entry1.delete(0, "end")
        self.Entry2.delete(0, "end")
        self.Text1.delete("1.0", "end")

    def Add(self):
        try:
            if self.Entry1.get()=="" or self.Entry2.get()=="":
                messagebox.showerror("Error", "Flavour and Quantity both are required.")
            else:
                infile = open("C:\\Users\\hp\\Desktop\\OOP mids\\PizzaStock.txt", "r")
                con = infile.read().split("\n")
                infile.close()
                con.pop()
                cart_file = open("C:\\Users\\hp\\Desktop\\OOP mids\\Cart.txt", "r")
                con2 = cart_file.read().split("\n")
                cart_file.close()
                con2.pop()
                cart_file1 = open("C:\\Users\\hp\\Desktop\\OOP mids\\Cart.txt", "a")
                if self.Entry1.get().strip() not in con:
                    messagebox.showinfo("Info", "Flavour not available in stock.")
                elif int(self.Entry2.get()) > con.count(self.Entry1.get()):
                    messagebox.showinfo("ATFS", "The quantity entered is greater than the available stock")
                # elif self.Entry1.get().strip() not in con:
                #     messagebox.showinfo("ATFS", "Flavour not available in stock.")
                elif (con2.count(self.Entry1.get().strip()) + int(self.Entry2.get())) > con.count(self.Entry1.get().strip()):
                    messagebox.showinfo("ATFS","Some quantity of this flavour is already in the cart. You must enter the quantity in the range of the stock.")
                else:
                    for i in range(int(self.Entry2.get())):
                        cart_file1.write(self.Entry1.get().strip()+"\n")
                    messagebox.showinfo("Info", "Added to Cart.") 
                cart_file1.close()
        except Exception:
            messagebox.showerror("Invalid input", "Quantity should be an integer in quantity entry.")
        

    def View(self):
        self.Text1.delete("1.0", "end")
        cset = set()
        c_list = []
        cart_file = open("C:\\Users\\hp\\Desktop\\OOP mids\\Cart.txt", "r")
        con = cart_file.read().split("\n")
        con.pop()
        for i in con:
            cset.add(i)
            c_list.append(i)
        self.Text1.insert(tk.END,"Flavours\t\t           Quantity\n")
        for j in cset:
            self.Text1.insert(tk.END, "{}\t\t|\t{}\n".format(j,c_list.count(j)))

    def Remove(self):
        try:
            if self.Entry1.get() == "" or self.Entry2.get() == "":
                messagebox.showerror("Error", "Flavour and quantity both are required.")
            else:
                infile = open("C:\\Users\\hp\\Desktop\\OOP mids\\Cart.txt", "r")
                con = infile.read().split("\n")
                con.pop()
                infile.close()
                for i in range(int(self.Entry2.get())):
                    if self.Entry1.get() not in con:
                        messagebox.showinfo("ATFS", "Flavour not added in cart.")
                        break
                    else:
                        con.remove(self.Entry1.get().strip())
                outfile = open("C:\\Users\\hp\\Desktop\\OOP mids\\Cart.txt", "w")
                for i in con:
                    outfile.write(i+"\n")
                outfile.close()
        except Exception:
            messagebox.showerror("Invalid input", "Quantity should be an integer in quantity entry.")

if __name__ == '__main__':
    start_Cart()