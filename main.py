#from tkinter import Tk, Label, Button,Frame,LabelFrame,Menu,Toplevel
from tkinter import*

class HackApp:
    def __init__(self, master):
        self.master = master
        master.title("Hacker-APP")
        master.geometry("900x500")
        master.configure(bg="black")

        #full window row configure
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)

        #full window column configure
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)
        

        self.menu_section = Menu(master)          # menu started
        
        # file menu option
        self.menu_section_file = Menu(self.menu_section,tearoff = 0)        
        self.menu_section_file.add_command(label="About")
        self.menu_section_file.add_command(label="close")
        self.menu_section_file.add_separator()                                   #menu option seperator
        self.menu_section_file.add_command(label="Exit")
        master.config(menu = self.menu_section)                             # file menu configure with the menu_section
        self.menu_section.add_cascade(label="File", menu = self. menu_section_file)   #menu label
        
        #labelled frames
        self.frame_left          =  LabelFrame(master,text="SELECT CHARECTERS",labelanchor="n")
        self.frame_center     =  LabelFrame(master,text="LENGTH OF WORDS",labelanchor="n")
        self.frame_right        =  LabelFrame(master,text="GENERATE",labelanchor="n")

        self.frame_left2          =  LabelFrame(master,text="PROGRESS BAR",labelanchor="n")
        self.frame_center2     =  LabelFrame(master,text="EXPORT AS FILES",labelanchor="n")
        self.frame_right2        =  LabelFrame(master,text="METADAT",labelanchor="n")

        #frame grids
        self.frame_left.grid(row=0,column=0,sticky="nsew")
        self.frame_center.grid(row=0,column=1,sticky="nsew")
        self.frame_right.grid(row=0,column=2,sticky="nsew")

        self.frame_left2.grid(row=1,column=0,sticky="nsew")
        self.frame_center2.grid(row=1,column=1,sticky="nsew")
        self.frame_right2.grid(row=1,column=2,sticky="nsew")
        
        #componants row configure
        self.frame_left.grid_rowconfigure(0, weight=1)
        self.frame_left.grid_rowconfigure(1, weight=1)
        self.frame_left.grid_rowconfigure(2, weight=1)

        #componants column configure
        self.frame_left.columnconfigure(0, weight=1)
        self.frame_left.columnconfigure(1, weight=1)
        
        

        
        #componants for frame 1
        self.check_btn1 = Checkbutton(self.frame_left,text="button")
        self.check_btn2 = Checkbutton(self.frame_left,text="button")
        self.check_btn3 = Checkbutton(self.frame_left,text="button")
        self.check_btn4 = Checkbutton(self.frame_left,text="button")
        self.frame1_btn = Button(self.frame_left,text="Continue",height = 2, width = 8)

        #componants grid
        self.check_btn1.grid(row=0,column=0,sticky="nsew")
        self.check_btn2.grid(row=0,column=1,sticky="nsew")
        self.check_btn3.grid(row=1,column=0,sticky="nsew")
        self.check_btn4.grid(row=1,column=1,sticky="nsew")
        self.frame1_btn.grid(row=2,column=0, columnspan=2)
 
        

root = Tk()
hack_gui = HackApp(root)
root.mainloop()
