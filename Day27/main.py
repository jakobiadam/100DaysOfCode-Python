from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        miles = float(input.get())
        km = round(miles * 1.609, 2)
        res.set(str(km))
    except ValueError:
        print("Not a number!")

root = Tk()
root.minsize(width=300, height=200)
root.title("Mile to Km Converter")

mainframe = ttk.Frame(root)
mainframe.grid(row=0, column=0)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

input = ttk.Entry(mainframe ,width=10)
input.grid(row=0, column=1)

label1 = ttk.Label(mainframe ,text="Miles")
label1.grid(row=0, column=2)

label2 = ttk.Label(mainframe ,text="is equal to")
label2.grid(row=1, column=0)

label3 = ttk.Label(mainframe ,text="Km")
label3.grid(row=1, column=2)

res = StringVar()
res.set("0")
result = ttk.Label(mainframe, textvariable=res)
result.grid(row=1, column=1)

button = ttk.Button(mainframe ,text="Calculate", command=calculate)
button.grid(row=2, column=1)

input.bind("<Return>", calculate)
input.focus()

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()