"""
@author Jinal Shah

"""


from tkinter import *
from tkinter import messagebox,filedialog
import tkinter.scrolledtext as ScrolledText
import tkinter.simpledialog

root = Tk(className='Text Editor')
textArea = ScrolledText.ScrolledText(master=root,width=100,height=80)

"""

Functions 

"""

# For opening File
def openFile():
    file = filedialog.askopenfile(parent=root,title='Select a text file',filetypes = (("txt files","*.txt"),("all files","*.*")))

    if file != None:
        contents = file.read()
        textArea.insert("1.0",contents)
        file.close()

# For saving files
def saveFile(event):
    file = filedialog.asksaveasfile(mode='w',filetypes=(("txt files","*.txt"),("all files","*.*")))

    if file != None:
        data = textArea.get("1.0",END+'-1c')
        file.write(data)
        file.close()

def saveFile2():
    file = filedialog.asksaveasfile(mode='w',filetypes=(("txt files","*.txt"),("all files","*.*")))

    if file != None:
        data = textArea.get("1.0",END+'-1c')
        file.write(data)
        file.close()

# For Exiting
def exitFile():
    if messagebox.askyesno("Quit?","Are you sure you would like to exit?"):
        root.destroy()

# For new Files
def newFile(event):
    if len(textArea.get(1.0,END+"-1c")) > 0:
        if messagebox.askyesno("Save?","Do you wish to save?"):
            saveFile()
        else:
            textArea.delete("1.0",END)

def newFile2():
    if len(textArea.get(1.0,END+"-1c")) > 0:
        if messagebox.askyesno("Save?","Do you wish to save?"):
            saveFile()
        else:
            textArea.delete("1.0",END)

# Create the Menu

menu = Menu(master=root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label="File",menu=fileMenu)

fileMenu.add_command(label='New',command=newFile2)
fileMenu.add_command(label='Open',command=openFile)
fileMenu.add_command(label='Save',command=saveFile2)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=exitFile)

# Binding
textArea.bind("<Control-Key-s>",saveFile)   # Control-s for saving
textArea.bind("<Control-Key-n>",newFile)    # Control-n for new file



# Pack everything

textArea.pack()


#Keeps Application Running
root.mainloop()
