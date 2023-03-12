from tkinter import *

root = Tk()
root.geometry("300x390")
root.title("Calculator Python")

bar = Entry(root,width=22,font=("Ubuntu",18,"normal"),fg="black",bg="gray85")
bar.place(x=5,y=3)

X = 75
Y = 75

# Menambahkan nomor yang diklik ke dalam bar
def insert(num):
    bar.insert(END, num)

# Menghapus karakter terakhir
def BackSpace():
    bar.delete(len(bar.get()) - 1)

# Menghapus semua karakter
def Delete():
    bar.delete(0, END)

# Mengambil teks yang ada di dalam bar, kemudian mengevaluasi ekspresi matematika yang ada di dalamnya menggunakan fungsi "eval()"
def Answer():
    text = str(bar.get())
    try:
        errors = ['**', '//', '-+', '---', '+--', '++']
        for eror in errors:
            if text.find(eror)>0:
                raise SyntaxError

        answer = eval(text)
        answer = round(answer,10)
        
        if float(answer).is_integer():
            answer = int(answer)
        
        Delete()
        bar.insert(0, answer)
        bar['fg'] = "black"
    except(SyntaxError):
        bar.delete(0, END)
        bar.insert(END, "Error")
        bar['fg'] = "red"

b1 = Button(root,text="1",font=("Poppins",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("1"))
b1.place(x=0,y=Y+20)

b2 = Button(root,text="2",font=("Poppins",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("2"))
b2.place(x=X,y=Y+20)

b3 = Button(root,text="3",font=("Poppins",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("3"))
b3.place(x=2*X,y=Y+20)

b4 = Button(root,text="4",font=("Poppins",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("4"))
b4.place(x=0,y=(2*Y)+20)

b5 = Button(root,text="5",font=("Poppins",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("5"))
b5.place(x=X,y=(2*Y)+20)

b6 = Button(root,text="6",font=("Poppins",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("6"))
b6.place(x=2*X,y=(2*Y)+20)

b7 = Button(root,text="7",font=("Poppins",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("7"))
b7.place(x=0,y=(3*Y)+20)

b8 = Button(root,text="8",font=("Poppins",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("8"))
b8.place(x=X,y=(3*Y)+20)

b9 = Button(root,text="9",font=("Poppins",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("9"))
b9.place(x=2*X,y=(3*Y)+20)

b0 = Button(root,text="0",font=("Poppins",16,"bold"),padx = 20,pady = 16,bd = 4,bg="white",command=lambda:insert("0"))
b0.place(x=X,y=(4*Y)+20)

# Decimal .
dot = Button(root,text=".",font=("Poppins",16,"bold"),padx = 23,pady = 16,bd = 4,bg="grey",command=lambda:insert("."))
dot.place(x=0,y=(4*Y)+20)

# Answer =
sama_dengan = Button(root,text="=",font=("Poppins",16,"bold"),padx = 20,pady = 16,bd = 4,bg="orange",command=Answer)
sama_dengan.place(x=2*X,y=(4*Y)+20)

# Insert * / + -
kali = Button(root,text="x",font=("Poppins",16,"bold"),padx = 22,pady = 16,bd = 4,bg="grey",command=lambda:insert("*"))
kali.place(x=3*X,y=Y+20)

bagi = Button(root,text="/",font=("Poppins",16,"bold"),padx = 25,pady = 16,bd = 4,bg="grey",command=lambda:insert("/"))
bagi.place(x=3*X,y=(2*Y)+20)

tambah = Button(root,text="+",font=("Poppins",16,"bold"),padx = 22,pady = 16,bd = 4,bg="grey",command=lambda:insert("+"))
tambah.place(x=3*X,y=(3*Y)+20)

kurang = Button(root,text="-",font=("Poppins",16,"bold"),padx = 25,pady = 16,bd = 4,bg="grey",command=lambda:insert("-"))
kurang.place(x=3*X,y=(4*Y)+20)

# Clear 
C = Button(root,text="C",font=("Poppins",16,"bold"),padx = 19,pady = 6,bd = 4,bg="orange",command=Delete)
C.place(x=0,y=Y-35)

CE = Button(root,text="CE",font=("Poppins",16,"bold"),padx = 12,pady = 6,bd = 4,bg="orange",command=BackSpace)
CE.place(x=X,y=Y-35)

root.mainloop()