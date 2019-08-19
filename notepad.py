#from tkinter import *
from tkinter import Menu
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


root = Tk()

root.title("Untitled - Notepad")
root.wm_iconbitmap("notepad.ico")

TextArea= Text(root,)
TextArea.pack()

menu = Menu(root)
root.config(menu=menu)


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<>"))

def copy():
    TextArea.event_generate(("<>"))

def paste():
    TextArea.event_generate(("<>"))

def about():
    showinfo("Notepad", "Notepad by Code With Gideon")






filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New          Ctrl+N", command =newFile )
filemenu.add_command(label="Open...       Ctrl+O", command = openFile)
filemenu.add_command(label="Save          Ctrl+S", command = saveFile)
filemenu.add_command(label="Save As...", command = saveFile)
filemenu.add_separator()
filemenu.add_command(label="Print          Ctrl+P")
filemenu.add_command(label="Exit", command = quitApp)



editmenu = Menu(menu, tearoff=0)
menu.add_cascade(label= "Edit", menu=editmenu)
editmenu.add_command(label="Undo")
editmenu.add_command(label="Cut", command = cut)
editmenu.add_command(label="Copy", command = copy)
editmenu.add_separator()
editmenu.add_command(label="Paste",command = paste)
editmenu.add_command(label="Delete")


formatmenu = Menu(menu, tearoff= 0)
menu.add_cascade(label= "Format", menu=formatmenu)
formatmenu.add_command(label="Font")


viewmenu = Menu(menu, tearoff= 0)
menu.add_cascade(label= "View", menu=viewmenu)






helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label= "Help", menu=helpmenu)
helpmenu.add_command(label="View Help")

aboutmenu = Menu(menu, tearoff=0)
menu.add_cascade(label= "about", menu=aboutmenu)
aboutmenu.add_command(label="about", command= about)













root.mainloop()
