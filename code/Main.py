from tkinter import *
from tkinter import filedialog
import MyParser

#TODO: написать хелпу
test = []
def Help(ev):
    test1(test)
    # global root
    # root.quit()

def test1(test):
    listbox_item = ["ein", "zwei", "drei", "3", "1", "20", "34", "53", "777", "666"]
    for item in listbox_item:
        listbox.insert(END, item)

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
root.geometry("550x500")
root.wm_minsize(540, 300)

panelFrame = Frame(root, bg='gray', height = 100)
textFrame = Frame(root)

panelFrame.pack(side='top', fill='x')
textFrame.pack(side='bottom', fill = 'both' , expand=1)

textbox = Text(textFrame, font='Fristyle 8', wrap='word')
scrollbar = Scrollbar(textFrame)
# scrollbar = Scrollbar(panelFrame)

scrollbar['command'] = textbox.yview
textbox['yscrollcommand'] = scrollbar.set

textbox.pack(side='left', fill='both', expand=1)
scrollbar.pack(side='right', fill='y')

loadBtn = Button(panelFrame, text='Load XML File')
# saveBtn = Button(panelFrame, text='Save')
quitBtn = Button(panelFrame, text='Help')
#===========
#===========


listbox_item = test
def select_item(event):
    value = (listbox.get(listbox.curselection()))
    print(value)
listbox = Listbox(panelFrame, width = 30, height = 4, font = ('times', 13))
listbox.bind('<<ListboxSelect>>', select_item)

for item in listbox_item:
    listbox.insert(END, item)
listbox.place(x = 230, y = 10)
#===========
#===========

loadBtn.bind("<Button-1>", LoadFile)
# saveBtn.bind("<Button-1>", SaveFile)
quitBtn.bind("<Button-1>", Help)

loadBtn.place(x = 10,  y = 10, width = 100, height = 35)
quitBtn.place(x = 120, y = 10, width = 100, height = 35)
# saveBtn.place(x=110, y=10, width=40, height=40)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()
