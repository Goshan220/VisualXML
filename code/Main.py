from tkinter import *
from tkinter import filedialog
from Parser import Pars


class App():
    def __init__(self):
        self.test = []
        self.startGUI()

#TODO: написать хелпу
    def Help(self, ev):
        self.test1(self.test)
        # global root
        # root.quit()

    def test1(self, test):
        listbox_item = ["ein", "zwei", "drei", "3", "1", "20", "34", "53", "777", "666"]
        for item in listbox_item:
            self.listbox.insert(END, item)

    def LoadFile(self, ev):
        fn = filedialog.Open(self.root, filetypes=[('*.xml files', '.xml')]).show()
        if fn == '':
            return
        text = open(fn)
        f = Pars()
        f.start(text)

        self.textbox.delete('1.0', 'end')
        self.textbox.insert('1.0', open("~temp.txt", 'rt', encoding='utf-8').read())

    #TODO: удалить следующую функцию т.к. сейва у меня нет
    def SaveFile(self, ev):
        fn =  filedialog.SaveAs(self.root, filetypes=[('*.txt files', '.txt')]).show()
        if fn == '':
            return
        if not fn.endswith(".txt"):
            fn += ".txt"
        open(fn, 'wt').write(self.textbox.get('1.0', 'end'))

    def startGUI(self):

        self.root = Tk()
        self.root.title("VisualXML")
        self.root.geometry("550x500")
        self.root.wm_minsize(540, 300)

        self.panelFrame = Frame(self.root, bg='gray', height = 100)
        self.textFrame = Frame(self.root)

        self.panelFrame.pack(side='top', fill='x')
        self.textFrame.pack(side='bottom', fill = 'both' , expand=1)

        self.textbox = Text(self.textFrame, font='Fristyle 8', wrap='word')
        self.scrollbar = Scrollbar(self.textFrame)
        # scrollbar = Scrollbar(panelFrame)

        self.scrollbar['command'] = self.textbox.yview
        self.textbox['yscrollcommand'] = self.scrollbar.set

        self.textbox.pack(side='left', fill='both', expand = 1)
        self.scrollbar.pack(side='right', fill='y')

        loadBtn = Button(self.panelFrame, text='Load XML File')
        # saveBtn = Button(panelFrame, text='Save')
        quitBtn = Button(self.panelFrame, text='Help')
        #===========
        #===========
        listbox_item = self.test
        def select_item(event):
            value = (self.listbox.get(self.listbox.curselection()))
            print(value)
        self.listbox = Listbox(self.panelFrame, width = 30, height = 4, font = ('times', 13))
        self.listbox.bind('<<ListboxSelect>>', select_item)

        for item in listbox_item:
            self.listbox.insert(END, item)
        self.listbox.place(x = 230, y = 10)
        #===========
        #===========

        loadBtn.bind("<Button-1>", self.LoadFile)
        # saveBtn.bind("<Button-1>", SaveFile)
        quitBtn.bind("<Button-1>", self.Help)

        loadBtn.place(x = 10,  y = 10, width = 100, height = 35)
        quitBtn.place(x = 120, y = 10, width = 100, height = 35)
        # saveBtn.place(x=110, y=10, width=40, height=40)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.mainloop()

app = App()
