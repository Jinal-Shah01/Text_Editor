"""

@author Jinal Shah

"""

from tkinter import *
import tkinter.scrolledtext as ScrolledTxt
import tkinter.simpledialog as simpleDialog
from tkinter import messagebox,filedialog

root = Tk(className=' Text Editor')
textArea = ScrolledTxt.ScrolledText(master=root, width=100, height=80)


# Text Editor Class
class Text_Editor:

    def __init__(self):
        pass

    # For opening Files
    def openFile(self):
        file = filedialog.askopenfile(parent=root, title='Select a text file',
                                      filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

        if file != None:
            contents = file.read()
            textArea.insert("1.0", contents)
            file.close()

    def openFile2(self,event):
        file = filedialog.askopenfile(parent=root, title='Select a text file',
                                      filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

        if file != None:
            contents = file.read()
            textArea.insert("1.0", contents)
            file.close()

    # For saving files:
    def saveFile(self):
        file = filedialog.asksaveasfile(mode='w', filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

        if file != None:
            data = textArea.get("1.0", END + '-1c')
            file.write(data)
            file.close()

    def saveFile2(self,event):
        file = filedialog.asksaveasfile(mode='w', filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

        if file != None:
            data = textArea.get("1.0", END + '-1c')
            file.write(data)
            file.close()

    # For exiting the file:
    def exitFile(self):
        if messagebox.askyesno("Quit?", "Are you sure you would like to exit?"):
            root.destroy()

    # For new files:
    def newFile(self):
        if len(textArea.get(1.0, END + "-1c")) > 0:
            if messagebox.askyesno("Save?", "Do you wish to save?"):
                self.saveFile()
            else:
                textArea.delete("1.0", END)

    def newFile2(self,event):
        if len(textArea.get(1.0, END + "-1c")) > 0:
            if messagebox.askyesno("Save?", "Do you wish to save?"):
                self.saveFile()
            else:
                textArea.delete("1.0", END)

    def copyFile(self,event):
        messagebox.showinfo("Copied","File has been copied")

    def pasteFile(self,event):
        txt = textArea.get(1.0,END + "-1c")
        textArea.insert(INSERT,txt)

    def selectAll(self,event):
        textArea.configure(background="light blue")

    def normalArea(self,event):
        textArea.configure(background='white')

    def cut(self,event):
        textArea.delete(index1=1.0,index2=END)

    def replaceString(self,event):
        find = simpleDialog.askstring("Find","Enter text")
        replace = simpleDialog.askstring("Replace", "Enter text")
        text = textArea.get(1.0,END + "-1c")
        text_Array = text.split(" ")

        try:
            index = text_Array.index(find)
            text_Array[index] = replace
        except:
            messagebox.showerror("Error","Word not found!!")
        data = ''

        for x in text_Array:
            data += x + " "

        textArea.delete(1.0,END + "-1c")
        textArea.insert(INSERT,data)

    # Creating the menu:
    def createMenu(self):
        menu = Menu(master=root)
        root.config(menu=menu)

        fileMenu = Menu(menu)
        menu.add_cascade(label="File", menu=fileMenu)

        fileMenu.add_command(label='New', command=self.newFile)
        fileMenu.add_command(label='Open', command=self.openFile)
        fileMenu.add_command(label='Save', command=self.saveFile)
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=self.exitFile)


txt_editor = Text_Editor()
txt_editor.createMenu()

# Binding
textArea.bind("<Control-Key-s>",txt_editor.saveFile2)       # Binding control-s to saveFile()
textArea.bind("<Control-Key-n>",txt_editor.newFile2)        # Binding control-n to newFile()
textArea.bind("<Control-Key-o>",txt_editor.openFile2)       # Binding control-o to openFile()
textArea.bind("<Control-Key-c>",txt_editor.copyFile)        # Binding control-c to copyFile()
textArea.bind("<Control-Key-v>",txt_editor.pasteFile)       # Binding control-v to pasteFile()
textArea.bind("<Control-Key-a>",txt_editor.selectAll)       # Binding control-a to selectAll()
textArea.bind("<Button-1>",txt_editor.normalArea)
textArea.bind("<Button-2>",txt_editor.normalArea)
textArea.bind("<Button-3>",txt_editor.normalArea)
textArea.bind("<Control-Key-x>",txt_editor.cut)
textArea.bind("<Control-Key-f>",txt_editor.replaceString)
# Packing everything
textArea.pack()

# Keeps the app running
root.mainloop()
