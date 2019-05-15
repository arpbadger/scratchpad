#!/usr/bin/python

# Import modules
from Tkinter import *
import ttk
import subprocess
import os
import sys

# Define Global Variable

def quit_command():
    sys.exit()
# Create New Project Folder and add associated txt files for scans,flags,compromat

############################################################################################################
############################################################################################################

# Gui Configuration

############################################################################################################
############################################################################################################

# Main Gui
main = Tk()
main.title('Tinkersec Scratchpad')
main.geometry('325x300')

# set style params
style = ttk.Style()
style.configure('My.TFrame', background='#535353')
style.configure('My.TButton', background='#212121',foreground='#1db954')
style.configure('My.TLabel',background='#535353',foreground='#1db954')

# create a toplevel menu
menubar = Menu(main)
shell_menu = Menu(menubar, tearoff=0)
shell_menu.add_command(label="Run")
shell_menu.add_command(label="Stop")
menubar.add_cascade(label='Shell',menu=shell_menu)
menubar.add_command(label='Quit',command=quit_command)
powershell_menu = Menu(menubar,tearoff=0)
powershell_menu.add_command(label='Run')
powershell_menu.add_command(label='Stop')
menubar.add_cascade(label='PowerShell',menu=powershell_menu)
menubar.add_command(label='Help')
main.config(menu=menubar)

# Main Gui Window

rows = 0
while rows < 50:
    main.rowconfigure(rows,weight=1)
    main.columnconfigure(rows,weight=1)
    rows += 1

# Configure the notebook Settings


frame= Frame(main,width=325,height=100)
frame.place(x=0,y=150)

output_text= Text(frame,bg='black')
output_text.insert(INSERT,END,'Hello')
output_text.place(x=0,y=0)

nb = ttk.Notebook(main, width=325,height=100)
nb.place(x=0,y=0)

# Page 1: Home Page
home= ttk.Frame(nb)#,style='My.TFrame')
nb.add(home, text='Home')


# Page 2: Shell Scripts
shell= ttk.Frame(nb)
nb.add(shell,text='shell')

# Page 3
powershell = ttk.Frame(nb)
nb.add(powershell,text='Powershell')

# Page 5: About
about= ttk.Frame(nb)
nb.add(about, text='About')

# Start Gui
main.mainloop()
