import subprocess
from tkinter import *

root = Tk()
root.title('New Processes Detector')
root.geometry('505x150+50+50')
root.resizable(width=0, height=0)

# Variables
ROTATE = True
processSet1 = set()
processSet2 = set()
extras = []


# Functions
def tprint(text):
    terminal['state'] = 'normal'
    terminal.insert('end', str(text) + '\n')
    terminal.see('end')
    root.update()
    terminal['state'] = 'disabled'


def color(variable, coloring):
    variable['fg'] = f'{coloring}'
    root.update()


def scan():
    global ROTATE

    if ROTATE:
        color(firstScanLabel, 'black')
        color(secondScanLabel, 'black')

        color(firstScanLabel, 'red')
        string = subprocess.check_output('tasklist /fo list').decode('Windows-1252').split('\n')
        for line in string:
            if 'Nombre de imagen' in line:
                processSet1.add(line.split(':')[1].strip())
        color(firstScanLabel, 'green')
        ROTATE = False

    else:
        color(secondScanLabel, 'red')
        string = subprocess.check_output('tasklist /fo list').decode('Windows-1252').split('\n')
        for line in string:
            if 'Nombre de imagen' in line:
                processSet2.add(line.split(':')[1].strip())
        color(secondScanLabel, 'green')
        ROTATE = True

        #       PRINTING
        for task in processSet2:
            if task not in processSet1:
                extras.append(task)
        if extras:
            tprint('New processes:')
            for task in extras:
                tprint(task)
            tprint(' ')
        if not extras:
            tprint('No new processes.')
            tprint(' ')
        processSet1.clear()
        processSet2.clear()
        extras.clear()


# BLOCKS
title = Label(root, text='Click once to scan processes, '
'click again to look for new processes running.', font=(0, 10, 'bold'), pady=10)
mainBlock = Frame(root)
leftHalf = LabelFrame(mainBlock, padx=10, pady=7)
rightHalf = Frame(mainBlock)
scanButton = Button(leftHalf, text='Scan', padx=10, pady=3, command=scan)
firstScanLabel = Label(leftHalf, text='First scan', pady=8)
secondScanLabel = Label(leftHalf, text='Second scan', pady=0)
terminal = Text(rightHalf, width=45, height=6, wrap='word', state='disabled')
terminalScrollbar = Scrollbar(rightHalf, command=terminal.yview)
terminal['yscrollcommand'] = terminalScrollbar.set
# POSITION
title.grid(row=0, column=0)
mainBlock.grid(row=1, column=0)
leftHalf.grid(row=1, column=0, padx=10)
rightHalf.grid(row=1, column=1)
scanButton.grid(row=0, column=0)
firstScanLabel.grid(row=1, column=0)
secondScanLabel.grid(row=2, column=0)
terminal.pack(side='left')
terminalScrollbar.pack(side='right', ipady=25)
root.mainloop()
