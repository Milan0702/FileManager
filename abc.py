from tkinter import *
from PIL import ImageTk, Image
import shutil       
import os
import easygui
from tkinter import filedialog
from tkinter import messagebox as mb

# Major functions of file manager

# open a file box window 
# when we want to select a file
def open_window():
    read=easygui.fileopenbox()
    return read

# open file function
def open_file():
    string = open_window()
    try:
        os.startfile(string)
    except:
        mb.showinfo('confirmation', "File not found!")

# copy file function
def copy_file():
    source1 = open_window()
    destination1=filedialog.askdirectory()
    shutil.copy(source1,destination1)
    mb.showinfo('confirmation', "File Copied !")

# delete file function
def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)             
    else:
        mb.showinfo('confirmation', "File not found !")

# rename file function
def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension=os.path.splitext(chosenFile)[1]
    print("Enter new name for the chosen file")
    newName=input()
    path = os.path.join(path1, newName+extension)
    print(path)
    os.rename(chosenFile,path) 
    mb.showinfo('confirmation', "File Renamed !")

# move file function
def move_file():
    source = open_window()
    destination =filedialog.askdirectory()
    if(source==destination):
        mb.showinfo('confirmation', "Source and destination are same")
    else:
        shutil.move(source, destination)  
        mb.showinfo('confirmation', "File Moved !")

# function to make a new folder
def make_folder():
    newFolderPath = filedialog.askdirectory()
    print("Enter name of new folder")
    newFolder=input()
    path = os.path.join(newFolderPath, newFolder)  
    os.mkdir(path)
    mb.showinfo('confirmation', "Folder created !")

# function to remove a folder
def remove_folder():
    delFolder = filedialog.askdirectory()
    os.rmdir(delFolder)
    mb.showinfo('confirmation', "Folder Deleted !")

# function to list all the files in folder
def list_files():
    folderList = filedialog.askdirectory()
    sortlist=sorted(os.listdir(folderList))       
    mb.showinfo('Files Found',"\n".join(sortlist))
    

#Creating the UI of our file manager

root = Tk()
root.state("zoomed")

# creating label and buttons to perform operations
Label(root, text="Simple File Manager", font=("Helvetica", 50),bg='Black', fg="orange" ,padx=40).place(x=375,y=20)

Button(root, text = "Open a File",font='"Comic Sans M" 25 bold',fg='Black', bg="orange" ,width=20, command = open_file).place(x=300,y=200)

Button(root, text = "Copy a File",font='"Comic Sans M" 25 bold',fg='Black', bg="orange" ,width=20, command = copy_file).place(x=300,y=350)

Button(root, text = "Delete a File",font='"Comic Sans M" 25 bold',fg='Black', bg="orange" ,width=20, command = delete_file).place(x=300,y=500)

Button(root, text = "Rename a File",font='"Comic Sans M" 25 bold',fg='Black', bg="orange" ,width=20, command = rename_file).place(x=300,y=650)

Button(root, text = "Move a File",font='"Comic Sans M" 25 bold',fg='Black', bg="orange" ,width=20, command = move_file).place(x=800,y=200)

Button(root, text = "Make a Folder",font='"Comic Sans M" 25 bold',fg='Black', bg="orange" ,width=20, command = make_folder).place(x=800,y=350)

Button(root, text = "Remove a Folder",font='"Comic Sans M" 25 bold',fg='Black', bg="orange" ,width=20, command = remove_folder).place(x=800,y=500)

Button(root, text = "List all Files in Directory",font='"Comic Sans M" 25 bold',fg='Black', bg="orange" ,width=20, command = list_files).place(x=800,y=650)



root.mainloop()

