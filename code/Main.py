from tkinter import *
from tkinter import filedialog
from Parser  import Pars


class App:
    def __init__(self):
        self.listbox_item = {}
        self.start_GUI()

    def help(self, ev):
        self.textbox.delete('1.0', 'end')
        self.textbox.insert('1.0', open("~help.txt", 'rt', encoding='utf-8').read())

    def load_file(self, ev):
        self.listbox.delete(0, END)

        fn = filedialog.Open(self.root, filetypes=[('*.xml files', '.xml')]).show()
        if fn == '':
            return
        text = open(fn)
        pars = Pars()
        pars.start(text)
        self.listbox_item = pars.get_tag_dict()
        # self.listbox_item = pars.getTextDict()

        self.textbox.delete('1.0', 'end')
        self.textbox.insert('1.0', open("~temp.txt", 'rt', encoding='utf-8').read())
        for item in self.listbox_item:
            self.listbox.insert(END, item)

    def show_file(self, ev):
        self.listbox.delete(0, END)
        self.textbox.delete('1.0', 'end')
        self.textbox.insert('1.0', open("~temp.txt", 'rt', encoding='utf-8').read())

        for item in self.listbox_item:
            self.listbox.insert(END, item)

    def save_tag(self, ev):
        fn = filedialog.SaveAs(self.root, filetypes=[('*.txt files', '.txt')]).show()
        if fn == '':
            return
        if not fn.endswith(".txt"):
            fn += ".txt"
        open(fn, 'wt').write(self.textbox.get('1.0', 'end'))

    def start_GUI(self):
        self.root = Tk()
        self.root.title("VisualXML")
        self.root.geometry("550x500")
        self.root.wm_minsize(540, 300)

        self.panelFrame = Frame(self.root, bg='gray', height=105)
        self.textFrame = Frame(self.root)
        self.panelFrame.pack(side='top', fill='x')
        self.textFrame.pack(side='bottom', fill='both', expand=1)

        self.textbox = Text(self.textFrame, font='Fristyle 10', wrap='word')
        self.scrollbar = Scrollbar(self.textFrame)
        self.scrollbar['command'] = self.textbox.yview
        self.textbox['yscrollcommand'] = self.scrollbar.set

        self.textbox.pack(side='left', fill='both', expand=1)
        self.scrollbar.pack(side='right', fill='y')

        def select_item(event):
            value = (self.listbox.get(self.listbox.curselection()))
            tempchar = str(self.listbox_item.get(value)).split(" ::: ")
            text = ''
            for char in tempchar:
                char = char[1:len(char)-1].replace(":", " =")
                text = text + str(char) + '\n'
            self.textbox.delete('1.0', 'end')
            self.textbox.insert('1.0', text)

        self.listbox = Listbox(self.panelFrame, width=40, height=5, font=('Fristyle', 10))
        self.listbox.bind('<<ListboxSelect>>', select_item)

        self.listbox.place(x=230, y=10)

        load_btn = Button(self.panelFrame, text='Load XML File')
        help_btn = Button(self.panelFrame, text='Help')
        show_file = Button(self.panelFrame, text='Show file')
        save_file = Button(self.panelFrame, text='Save tag into file')
        load_btn.bind("<Button-1>", self.load_file)
        help_btn.bind("<Button-1>", self.help)
        show_file.bind("<Button-1>", self.show_file)
        save_file.bind("<Button-1>", self.save_tag)
        load_btn.place(x=10,  y=10, width=100, height=35)
        help_btn.place(x=120, y=10, width=100, height=35)
        show_file.place(x=10, y=55, width=100, height=35)
        save_file.place(x=120, y=55, width=100, height=35)

        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.mainloop()

app = App()
