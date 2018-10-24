import os
from Tkinter import *
import tkFileDialog
class GUI():
    def __init__(self):
        self.root = Tk()
        self.root.title("PDB File Processor")
        
        self.qFlag = False  #Flag to quit
        self.m = Menu(self.root)  # Cascade menu for several functions
        self.root.config(menu = self.m)
        self.filemenu = Menu(self.m)
        self.m.add_cascade(label="File", menu = self.filemenu)
        self.filemenu.add_command(label="Open...", command=self.selectPath)  #Choose to open a file 
        self.filemenu.add_command(label="Exit", command=self.__close)  #Quit the program
        self.helpmenu = Menu(self.m)
        self.m.add_cascade(label="Help", menu = self.helpmenu)
        self.helpmenu.add_command(label="About...", command=self.__help)  #Open the instruction
        
        self.fp = StringVar()  #Read the name of the file
        Label(self.root, text="File Path", height=1, width=10).grid(row=0, column=0, sticky=N+W+S)
        Entry(self.root, textvariable=self.fp, width=34).grid(row=1, column=0, columnspan=3, sticky=W+E)
        Button(self.root, text="Browse", width=15, height=1, command=self.selectPath).grid(row=1, column=3, sticky=E)  #Choose to open a file
        Button(self.root, text="Open", width=15, height=1, command=self.openfile).grid(row=0, column=3, sticky=E)   #Comfirm the file to open
        self.warning = StringVar()
        self.warning.set("")
        self.seg = Label(self.root, textvariable=self.warning, height=1)
        self.seg.grid(row=2, column=0, sticky=N+S+W+E)  #For segmentation
        
        self.func = Frame(self.root, width=400, height=500, bd=3, relief="groove")  #The frame is the function zone
        self.func.grid(row=3, column=0, rowspan=3, columnspan=4, sticky=N+S+W+E)
        
        self.aaFlag = 0  #Flag to search or count an excat amino acid
        Label(self.func, text="Amino acid", width=10).grid(row=0, column=0,sticky=N+S+W+E)
        self.aa = StringVar()  #The choice of the amino acid
        self.b1 = Button(self.func, text="Search", width=10, command=self.aaSearch, state="disabled")  #For search to comfirm the location
        self.b1.grid(row=0, column=2)
        self.b2 = Button(self.func, text="Count", width=10, command=self.aaCount, state="disabled")   #For count to comfirm the amount
        self.b2.grid(row=0, column=3)
        Radiobutton(self.func, text="GLY", variable=self.aa, width=10, value="GLY").grid(row=1, column=0, sticky=W)
        Radiobutton(self.func, text="ALA", variable=self.aa, width=10, value="ALA").grid(row=1, column=1, sticky=W)
        Radiobutton(self.func, text="PRO", variable=self.aa, width=10, value="PRO").grid(row=1, column=2, sticky=W)
        Radiobutton(self.func, text="VAL", variable=self.aa, width=10, value="VAL").grid(row=1, column=3, sticky=W)
        Radiobutton(self.func, text="LEU", variable=self.aa, width=10, value="LEU").grid(row=2, column=0, sticky=W)
        Radiobutton(self.func, text="ILE", variable=self.aa, width=10, value="ILE").grid(row=2, column=1, sticky=W)
        Radiobutton(self.func, text="PHE", variable=self.aa, width=10, value="PHE").grid(row=2, column=2, sticky=W)
        Radiobutton(self.func, text="TRP", variable=self.aa, width=10, value="TRP").grid(row=2, column=3, sticky=W)
        Radiobutton(self.func, text="MET", variable=self.aa, width=10, value="MET").grid(row=3, column=0, sticky=W)
        Radiobutton(self.func, text="SER", variable=self.aa, width=10, value="SER").grid(row=3, column=1, sticky=W)
        Radiobutton(self.func, text="THR", variable=self.aa, width=10, value="THR").grid(row=3, column=2, sticky=W)
        Radiobutton(self.func, text="TYR", variable=self.aa, width=10, value="TYR").grid(row=3, column=3, sticky=W)
        Radiobutton(self.func, text="CYS", variable=self.aa, width=10, value="CYS").grid(row=4, column=0, sticky=W)
        Radiobutton(self.func, text="ASN", variable=self.aa, width=10, value="ASN").grid(row=4, column=1, sticky=W)
        Radiobutton(self.func, text="GLN", variable=self.aa, width=10, value="GLN").grid(row=4, column=2, sticky=W)
        Radiobutton(self.func, text="LYS", variable=self.aa, width=10, value="LYS").grid(row=4, column=3, sticky=W)
        Radiobutton(self.func, text="ARG", variable=self.aa, width=10, value="ARG").grid(row=5, column=0, sticky=W)
        Radiobutton(self.func, text="HIS", variable=self.aa, width=10, value="HIS").grid(row=5, column=1, sticky=W)
        Radiobutton(self.func, text="ASP", variable=self.aa, width=10, value="ASP").grid(row=5, column=2, sticky=W)
        Radiobutton(self.func, text="GLU", variable=self.aa, width=10, value="GLU").grid(row=5, column=3, sticky=W)
        self.num = StringVar()
        self.num.set("Numbers are shown here...")  
        self.n = Label(self.func, textvariable=self.num, fg="gray", height=5, wraplength = 270)  #There shows the number
        self.n.grid(row=6, column=0, columnspan=4)
        
        self.seqFlag = False   #Flag to show the sequence of the peptide
        Label(self.func, text="Sequence", width=10).grid(row=7, column=0)
        self.b3 = Button(self.func, text="Produce", width=10, command=self.seqProduce, state="disabled")  #For producing the sequence
        self.b3.grid(row=7, column=3, sticky=E)
        self.s = Text(self.func, height=7, fg="gray", width=53)  #Show the sequence
        self.s.grid(row=8, column=0, columnspan=4, rowspan=2, sticky=W)
        self.scroll = Scrollbar(self.func)  #Scroll of the text
        self.scroll.grid(row=8, column=3, rowspan=2, sticky=N+S+E)
        self.scroll.config(command=self.s.yview)
        self.s.config(yscrollcommand=self.scroll.set)
        self.s.insert(0.0, "The peptide sequence is shown here...")  #Initialize the text
        
        #Call out some commands of text 
        self.call = Menu(self.root,tearoff=0)
        self.call.add_command(label="Cut",command=self.cut)
        self.call.add_command(label="Copy",command=self.copy)
        self.call.add_command(label="Paste",command=self.paste)
        self.call.add_separator()
        self.call.add_command(label="Select All", command=self.selectAll)
        self.s.bind("<Button-3>",self.popupmenu)
        self.root.bind("<Control-Key-a>", self.selectAll)

    #Three functions when click the right button        
    def cut(self, event=None):
        self.s.event_generate("<<Cut>>")
        
    def copy(self, event=None):
        self.s.event_generate("<<Copy>>")
        
    def paste(self, event=None):
        self.s.event_generate("<<Paste>>")
        
    def selectAll(self, event=None):
        self.s.tag_add('sel','1.0',END)
    
    def popupmenu(self, event):
        self.call.post(event.x_root,event.y_root)
        
    def __help(self):
    #Help function: show the instruction
        f = open("help.txt", "r")
        root = Tk()
        root.title("Help")
        helpfile = f.read()
        help = Text(root,height=50, width=80)
        help.grid(row=0, column=0, sticky=NW)
        help.insert(0.0, helpfile)
        f.close()
        self.root.quit()
        
    def __file(self):
    #Open the file that should be operate on
        root = Tk()
        self.fp=""
        Label(root, text="File Path", height=1, width=10).grid(row=0, column=0, sticky=N+S+W+E)
        Entry(root, textvariable=self.fp, width=30).grid(row=0, column=1, columnspan=2,sticky=N+S+W+E)
        Button(root, text="Browse", width=10, height=1, command=self.openfile).grid(row=0, column=3, sticky=N+S)
        Button(root, text="Open", width=10, height=1, command=self.openfile).grid(row=0, column=4, sticky=N+S)
        self.root.quit()
        
    def getInfo(self):
    #Get the flag from GUI and execute the function
        self.root.mainloop()
        return self.fp.get(), self.qFlag, self.aa.get()
        
    def showInfo(self, AA, aac, seq):
    #Show the informantion the program has read
        if self.aa.get() != "":
            if self.aaFlag == 1:
                self.num.set(aac)
            elif self.aaFlag == -1:
                self.num.set(AA.get(self.aa.get(), 0))
        
        if self.seqFlag == True:
            self.s.delete(0.0, END)
            self.s.insert(0.0, seq)
        
        self.root.quit()
        self.aaFlag = 0
        self.seqFlag = False
        
    def __close(self):
    #Quit the program
        self.qFlag = True
        self.root.quit()
        self.root.destroy()
    
    def selectPath(self):
    #Open the window to choose the file
        path_ = tkFileDialog.askopenfilename(filetypes=[("pdb_file".decode('gbk'),".pdb")])
        self.fp.set(str(path_))
        
    def openfile(self):
    #If the file exists, the button will be activated
        fp = self.fp.get()
        if os.path.exists(fp):
            self.b1.config(state="active")
            self.b2.config(state="active")
            self.b3.config(state="active")
            self.warning.set("")
        else:
            self.b1.config(state="disabled")
            self.b2.config(state="disabled")
            self.b3.config(state="disabled")
            self.n.config(fg="gray")
            self.s.config(fg="gray")
            self.warning.set("The file does't exist.")
            self.seg.config(fg="red")
        self.root.quit()
        
    def aaSearch(self):
    #Modify the flag to search the location of the amino acid
        self.aaFlag = 1
        self.n.config(fg="black")
        self.num.set("Please choose a amino acid.")
        self.root.quit()
        
    def aaCount(self):
    #Modify the flag to search the amount of the amino acid
        self.aaFlag = -1
        self.n.config(fg="black")
        self.num.set("Please choose a amino acid.")
        self.root.quit()
        
    def seqProduce(self):
    #Modify the flag to show the sequence of the amino acid
        self.seqFlag = True
        self.s.config(fg="black")
        self.root.quit()

