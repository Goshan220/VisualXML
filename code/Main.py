from tkinter import *
from tkinter import filedialog
import MyParser

def Quit(ev):
    global root
    root.destroy()

def LoadFile(ev):
    fn =  filedialog.Open(root, filetypes=[('*.xml files', '.xml')]).show()
    if fn == '':
        return
    text = open(fn)
    MyParser.start(text)

    textbox.delete('1.0', 'end')
    textbox.insert('1.0', open("~temp.txt", 'rt', encoding='utf-8').read())

#TODO: удалить следующую функцию т.к. сейва у меня нет
def SaveFile(ev):
    fn =  filedialog.SaveAs(root, filetypes=[('*.txt files', '.txt')]).show()
    if fn == '':
        return
    if not fn.endswith(".txt"):
        fn += ".txt"
    open(fn, 'wt').write(textbox.get('1.0', 'end'))


root = Tk()
root.title("VisualXML")
panelFrame = Frame(root, height=60, bg='gray')
textFrame = Frame(root, height=340, width=600)

panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill='both', expand=1)

textbox = Text(textFrame, font='Fristyle 14', wrap='word')
scrollbar = Scrollbar(textFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

loadBtn = Button(panelFrame, text='Load XML File')
# saveBtn = Button(panelFrame, text='Save')
quitBtn = Button(panelFrame, text='Quit')

loadBtn.bind("<Button-1>", LoadFile)
# saveBtn.bind("<Button-1>", SaveFile)
quitBtn.bind("<Button-1>", Quit)

loadBtn.place(x=10, y=10, width=100, height=40)
# saveBtn.place(x=110, y=10, width=40, height=40)
quitBtn.place(x=120, y=10, width=100, height=40)

root.mainloop()