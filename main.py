from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry("280x303")
root.resizable(False, False)
root.title("PyCalc by Donio3d")

style = ttk.Style()
style.configure("TButton",
                font="Roboto 18",
                padding="5",
                width='4')

style.configure("TLabel",
                font="Roboto 20",
                padding=(10, 0, 10, 10),
                )

style.configure("M.TLabel",
                font="Roboto 12",
                padding=(10, 10, 10, 0),
                foreground="gray"
                )

display = StringVar(root, value="")
display.set("0")

memory = StringVar(root, value="")
memory.set("")

reset = False


def negate():
    if display.get()[0] is "0":
        pass
    elif display.get()[0] is "-":
        display.set(display.get()[1:])
    else:
        display.set("-"+display.get())


def clearall():
    display.set("0")
    memory.set("")


def clear():
    display.set("0")


def delete():
    global reset

    if reset:
        pass
    else:
        display.set(display.get()[0:-1])

        if display.get() is "":
            display.set("0")


def result():
    global reset

    if memory.get() is "":
        reset = True
        pass
    else:
        display.set(eval(memory.get() + display.get()))
        memory.set("")
        reset = True


def num(value):
    global reset

    if len(display.get()) is 17:
        if reset:
            display.set(value)
        pass
    elif display.get() is "0" or reset:
        display.set(value)
        reset = False
    else:
        display.set(display.get() + value)


def op(value):
    global reset

    if reset and memory.get() is "":
        memory.set(display.get() + value)
    elif reset:
        memory.set(memory.get()[0:-1] + value)
    else:
        memory.set(memory.get() + display.get() + value)
        reset = True

    if memory.get() is not "":
        display.set(eval(memory.get()[0:-1]))


def dot():
    global reset

    if '.' in display.get():
        pass
    elif reset:
        display.set("0.")
        reset = False
    elif display.get()[-1] is ".":
        pass
    else:
        display.set(display.get() + ".")


# Row 0 ----------------
ttk.Label(root, textvariable=memory, style="M.TLabel").grid(row=0, columnspan=4, sticky='e')

# Row 1 ----------------
ttk.Label(root, textvariable=display).grid(row=1, columnspan=4, sticky='e')

# Row 2 ----------------
ttk.Button(root, text="CE", command=lambda: clear()).grid(row=2, column=0)
ttk.Button(root, text="C", command=lambda: clearall()).grid(row=2, column=1)
ttk.Button(root, text="Del", command=lambda: delete()).grid(row=2, column=2)
ttk.Button(root, text=chr(247), command=lambda: op('/')).grid(row=2, column=3)

# Row 3 ----------------
ttk.Button(root, text="7", command=lambda: num('7')).grid(row=3, column=0)
ttk.Button(root, text="8", command=lambda: num('8')).grid(row=3, column=1)
ttk.Button(root, text="9", command=lambda: num('9')).grid(row=3, column=2)
ttk.Button(root, text="*", command=lambda: op('*')).grid(row=3, column=3)

# Row 4 ----------------
ttk.Button(root, text="4", command=lambda: num('4')).grid(row=4, column=0)
ttk.Button(root, text="5", command=lambda: num('5')).grid(row=4, column=1)
ttk.Button(root, text="6", command=lambda: num('6')).grid(row=4, column=2)
ttk.Button(root, text="-", command=lambda: op('-')).grid(row=4, column=3)

# Row 5 ----------------
ttk.Button(root, text="1", command=lambda: num('1')).grid(row=5, column=0)
ttk.Button(root, text="2", command=lambda: num('2')).grid(row=5, column=1)
ttk.Button(root, text="3", command=lambda: num('3')).grid(row=5, column=2)
ttk.Button(root, text="+", command=lambda: op('+')).grid(row=5, column=3)

# Row 6 ----------------
ttk.Button(root, text="+/-", command=lambda: negate()).grid(row=6, column=0)
ttk.Button(root, text="0", command=lambda: num('0')).grid(row=6, column=1)
ttk.Button(root, text=".", command=lambda: dot()).grid(row=6, column=2)
ttk.Button(root, text="=", command=lambda: result()).grid(row=6, column=3)

root.grid_columnconfigure(0, weight=1)
root.mainloop()
