import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

# create the window window
window = tk.Tk()
window.title('Watermarker Tkinter Dialog')
window.resizable(False, False)
window.geometry('320x240')

inputfilebox=tk.Text(window, height=1, width=40)

inputfilebox.pack()

def select_file():
    filetypes = (
        ('text files', '*.png'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    inputfilebox.delete("1.0","end")
    inputfilebox.insert("1.0", filename)
    # showinfo(
    #     title='Selected File',
    #     message=filename
    # )


# open button
open_button = ttk.Button(
    window,
    text='Select a PNG File',
    command=select_file
)

open_button.pack(expand=True)


outdirectorybox=tk.Text(window, height=1, width=40)

outdirectorybox.pack()


def select_directory():
    directoryname=fd.askdirectory()

    outdirectorybox.delete("1.0","end")
    outdirectorybox.insert("1.0", directoryname)

    # showinfo(
    #     title='Selected Direcory',
    #     message=directoryname
    # )


# open button
open_button_d = ttk.Button(
    window,
    text='Set Output Direcory',
    command=select_directory
)

open_button_d.pack(expand=True)


markermessagebox=tk.Text(window, height=1, width=40)

markermessagebox.pack()

markermessagebox.insert("1.0", "maker message")

import marker

def maker_it():
    #mytest.main(["-x","7","-y","6"])
    filename = inputfilebox.get("1.0",'end-1c')
    print(filename)
    outdir = outdirectorybox.get("1.0",'end-1c')
    print(outdir)
    msg = markermessagebox.get("1.0",'end-1c')
    print(msg)
    res = marker.main(["-f", filename, "-o", outdir, "-m", msg])
    # res = marker.main(["-f", ".\\input\\test.png", "-m", "test from tk"])
    # res = marker.main(["--help"])
    print(res)


open_button_m = ttk.Button(
    window,
    text='Maker it',
    command=maker_it
)

open_button_m.pack(expand=True)

# run the application
window.mainloop()