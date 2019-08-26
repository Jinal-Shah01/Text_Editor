"""

@author Jinal Shah

"""

from tkinter import *
import tkinter.scrolledtext as ScrolledTxt
import tkinter.simpledialog as simpleDialog
from tkinter import messagebox,filedialog


# Text Editor Class
class Text_Editor:

    def __init__(self):
        self.root = Tk(className=' Text Editor')
        self.textArea = ScrolledTxt.ScrolledText(master=self.root, width=100, height=80)

    # For opening Files
    def openFile(self):
        file = filedialog.askopenfile(parent=self.root, title='Select a text file',
                                      filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

        if file != None:
            contents = file.read()
            self.textArea.insert("1.0", contents)
            file.close()

    def openFile2(self,event):
        file = filedialog.askopenfile(parent=self.root, title='Select a text file',
                                      filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

        if file != None:
            contents = file.read()
            self.textArea.insert("1.0", contents)
            file.close()

    # For saving files:
    def saveFile(self):
        file = filedialog.asksaveasfile(mode='w', filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

        if file != None:
            data = self.textArea.get("1.0", END + '-1c')
            file.write(data)
            file.close()

    def saveFile2(self,event):
        file = filedialog.asksaveasfile(mode='w', filetypes=(("txt files", "*.txt"), ("all files", "*.*")))

        if file != None:
            data = self.textArea.get("1.0", END + '-1c')
            file.write(data)
            file.close()

    # For exiting the file:
    def exitFile(self):
        if messagebox.askyesno("Quit?", "Are you sure you would like to exit?"):
            self.root.destroy()

    # For new files:
    def newFile(self):
        if len(self.textArea.get(1.0, END + "-1c")) > 0:
            if messagebox.askyesno("Save?", "Do you wish to save?"):
                self.saveFile()
            else:
                self.textArea.delete("1.0", END)

    def newFile2(self,event):
        if len(self.textArea.get(1.0, END + "-1c")) > 0:
            if messagebox.askyesno("Save?", "Do you wish to save?"):
                self.saveFile()
            else:
                self.textArea.delete("1.0", END)

    def copyFile(self,event):
        messagebox.showinfo("Copied","File has been copied")

    def pasteFile(self,event):
        txt = self.textArea.get(1.0,END + "-1c")
        self.textArea.insert(INSERT,txt)

    def selectAll(self,event):
        self.textArea.configure(background="light blue")

    def normalArea(self,event):
        self.textArea.configure(background='white')

    def cut(self,event):
        self.textArea.delete(index1=1.0,index2=END)

    def replaceString(self,event):
        find = simpleDialog.askstring("Find","Enter text")
        replace = simpleDialog.askstring("Replace", "Enter text")
        text = self.textArea.get(1.0,END + "-1c")
        text_Array = text.split(" ")
        temp = []

        for x in range(0,len(text_Array)):
            if "\n" in text_Array[x]:
                temp = text_Array[x].split("\n")
                for y in range(0, len(temp)):
                    if temp[y] == '':
                        temp[y] = '123'             # Key for /n
                text_Array[x] = temp

        for y in range(0,len(text_Array)):
            if type(text_Array[y]) == list:
                for z in range(0,len(text_Array[y])):
                    if text_Array[y][z] == find:
                        text_Array[y][z] = replace
            else:
                if text_Array[y] == find:
                    text_Array[y] = replace

        data = ''

        for a in text_Array:
            if type(a) == list:
                for b in a:
                    if b == '123':
                        data += "\n"
                    else:
                        data += b + " "
            else:
                data += a + " "
        self.textArea.delete(1.0,END + "-1c")
        self.textArea.insert(INSERT,data)

    # Creating the menu:
    def createMenu(self):
        menu = Menu(master=self.root)
        self.root.config(menu=menu)

        fileMenu = Menu(menu)
        menu.add_cascade(label="File", menu=fileMenu)

        fileMenu.add_command(label='New', command=self.newFile)
        fileMenu.add_command(label='Open', command=self.openFile)
        fileMenu.add_command(label='Save', command=self.saveFile)
        fileMenu.add_separator()
        fileMenu.add_command(label='Exit', command=self.exitFile)


# Tester
txt_editor = Text_Editor()
txt_editor.createMenu()

# Binding
txt_editor.textArea.bind("<Control-Key-s>",txt_editor.saveFile2)       # Binding control-s to saveFile()
txt_editor.textArea.bind("<Control-Key-n>",txt_editor.newFile2)        # Binding control-n to newFile()
txt_editor.textArea.bind("<Control-Key-o>",txt_editor.openFile2)       # Binding control-o to openFile()
txt_editor.textArea.bind("<Control-Key-c>",txt_editor.copyFile)        # Binding control-c to copyFile()
txt_editor.textArea.bind("<Control-Key-v>",txt_editor.pasteFile)       # Binding control-v to pasteFile()
txt_editor.textArea.bind("<Control-Key-a>",txt_editor.selectAll)       # Binding control-a to selectAll()
txt_editor.textArea.bind("<Button-1>",txt_editor.normalArea)
txt_editor.textArea.bind("<Button-2>",txt_editor.normalArea)
txt_editor.textArea.bind("<Button-3>",txt_editor.normalArea)
txt_editor.textArea.bind("<Control-Key-x>",txt_editor.cut)
txt_editor.textArea.bind("<Control-Key-f>",txt_editor.replaceString)

# Packing everything
txt_editor.textArea.pack()

# Keeps the app running
txt_editor.root.mainloop()
