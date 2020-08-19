#from tkinter import Tk, Label, Button,Frame,LabelFrame,Menu,Toplevel
from tkinter import*

class HackApp:
    def __init__(self, master):
        self.master = master
        master.title("Hacker-APP")
        master.geometry("900x500")
        master.configure(bg="red")

        #full window row configure
        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)

        #full window column configure
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.columnconfigure(2, weight=1)
        
        # MENU SECTION STARTED #####################################################
        self.menu_section = Menu(master)          # menu started
        self.menu_section_file = Menu(self.menu_section,tearoff = 0)        # file menu option
        self.menu_section_file.add_command(label="About")
        self.menu_section_file.add_command(label="close")
        self.menu_section_file.add_separator()                                   #menu option seperator
        self.menu_section_file.add_command(label="Exit")
        master.config(menu = self.menu_section)                             # file menu configure with the menu_section
        self.menu_section.add_cascade(label="File", menu = self. menu_section_file)   #menu label

        #END MENU #####################################################################


        #MAIN FRAMES 6 ##################################################################
        #labelled frames
        self.frame_left          =  LabelFrame(master,text="SELECT CHARECTERS",labelanchor="n",bg="black",bd=10)
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

        #MAIN FRAMES 6 ENDS   ##################################################################


        
       #Frame 1 Configuration for first labelled frame ######################################################
        #frame for componants for fisrt labeled frame  row configure
        self.frame_left.grid_rowconfigure(0, weight=1)
        self.frame_left.grid_rowconfigure(1, weight=1)
        self.frame_left.grid_rowconfigure(2, weight=1)
        #frame for componants for fisrt labeled frame column configure
        self.frame_left.columnconfigure(0, weight=1)
        #END#####################################################################################
        
        #Componants for frame 1 #######################################################################
         #componants 1 frame
        self.frame_comp_1 = Frame(self.frame_left,bg="#232526")
        #componants 1 frame row config
        self.frame_comp_1.grid_rowconfigure(0, weight=1)
        self.frame_comp_1.grid_rowconfigure(1, weight=1)
        self.frame_comp_1.grid_rowconfigure(2, weight=1)
        self.frame_comp_1.grid_rowconfigure(3, weight=1)
        #componants 1 frame column config
        self.frame_comp_1.columnconfigure(0, weight=1)
        #componants 1 frame grid
        self.frame_comp_1.grid(row=0,column=0,sticky="nsew")
        
        
        
        #componants for frame 1
        self.check_btn1 = Checkbutton(self.frame_comp_1,text="Numbers",padx=50,pady=30,bg="#232526",fg="white",selectcolor="#0F2027",activebackground="#232526")
        self.check_btn2 = Checkbutton(self.frame_comp_1,text="Alphabets (A)",padx=50,pady=20,bg="#232526",fg="white",selectcolor="#0F2027",activebackground="#232526")
        self.check_btn3 = Checkbutton(self.frame_comp_1,text="Alphabets (a)",padx=50,pady=20,bg="#232526",fg="white",selectcolor="#0F2027",activebackground="#232526")
        self.check_btn4 = Checkbutton(self.frame_comp_1,text="Special Characters",padx=50,pady=20,bg="#232526",fg="white",selectcolor="#0F2027",activebackground="#232526")
        self.frame1_btn = Button(self.frame_left,text="Continue",height = 2, width = 8,bg="#232526",fg="white")

        #componants grid
        self.check_btn1.grid(row=0,column=0,sticky="w")
        self.check_btn2.grid(row=1,column=0,sticky="w")
        self.check_btn3.grid(row=2,column=0,sticky="w")
        self.check_btn4.grid(row=3,column=0,sticky="w")
        self.frame1_btn.grid(row=2,column=0)

         #END ########################################################################################
        

root = Tk()
hack_gui = HackApp(root)
root.mainloop()
