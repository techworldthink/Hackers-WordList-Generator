#from tkinter import Tk, Label, Button,Frame,LabelFrame,Menu,Toplevel
from tkinter.ttk import *
from tkinter import*
from tkinter import font

class HackApp:
    def __init__(self, master):
        self.master = master
        master.title("Hacker-APP")
        master.geometry("900x500")
        master.configure(bg="red")
        #Fonts
        self.label_frame_font = font.Font(family="Helvetica",size=10,weight="bold")
        self.frame2_font = font.Font(family="Franklin Gothic Medium",size=10)

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
        self.frame_left          =  LabelFrame(master,text="SELECT CHARECTERS",labelanchor="n",bg="black",bd=10,fg="white",font=self.label_frame_font)
        self.frame_center     =  LabelFrame(master,text="LENGTH OF WORDS",labelanchor="n",bg="black",bd=10,fg="white",font=self.label_frame_font)
        self.frame_right        =  LabelFrame(master,text="STATUS & GENERATE",labelanchor="n",bg="black",bd=10,fg="white",font=self.label_frame_font)

        self.frame_left2          =  LabelFrame(master,text="PROGRESS BAR",labelanchor="n",bg="black",bd=10,fg="white",font=self.label_frame_font)
        self.frame_center2     =  LabelFrame(master,text="EXPORT AS FILES",labelanchor="n",bg="black",bd=10,fg="white",font=self.label_frame_font)
        self.frame_right2        =  LabelFrame(master,text="METADAT",labelanchor="n",bg="black",bd=10,fg="white",font=self.label_frame_font)

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


         #Frame 2 Configuration for second labelled frame ######################################################
        #frame for componants for fisrt labeled frame  row configure
        self.frame_center.grid_rowconfigure(0, weight=1)
        self.frame_center.grid_rowconfigure(1, weight=1)
        self.frame_center.grid_rowconfigure(2, weight=1)
        #frame for componants for fisrt labeled frame column configure
        self.frame_center.columnconfigure(0, weight=1)
        #END#####################################################################################


        #Componants for frame 1 #######################################################################
         #componants 1 frame
        self.frame_comp_2 = Frame(self.frame_center,bg="#232526")
        #componants 1 frame row config
        self.frame_comp_2.grid_rowconfigure(0, weight=1)
        self.frame_comp_2.grid_rowconfigure(1, weight=1)
        self.frame_comp_2.grid_rowconfigure(2, weight=1)
        self.frame_comp_2.grid_rowconfigure(3, weight=1)
        #componants 1 frame column config
        self.frame_comp_2.columnconfigure(0, weight=1)
        #componants 1 frame grid
        self.frame_comp_2.grid(row=0,column=0,sticky="nsew")
        
        
        
        #componants for frame 1
        self.label_frame_2 = Label(self.frame_comp_2,text="MINIMUM WORD LENGTH",padx=50,pady=30,bg="#232526",fg="white",font=self.frame2_font)
        self.label2_frame_2 = Label(self.frame_comp_2,text="MAXIMUM WORD LENGTH",padx=50,pady=25,bg="#232526",fg="white",font=self.frame2_font)
        self.entry_frame_2 = Entry(self.frame_comp_2,bg="#0F2027",fg="white")
        self.entry2_frame_2 = Entry(self.frame_comp_2,bg="#0F2027",fg="white")
       
        self.frame2_btn = Button(self.frame_center,text="Continue",height = 2, width = 8,bg="#232526",fg="white")

        #componants grid
        self.label_frame_2.grid(row=0,column=0,sticky="w")
        self.entry_frame_2.grid(row=1,column=0,sticky="w",padx=50,pady=20)
        self.label2_frame_2.grid(row=2,column=0,sticky="w")
        self.entry2_frame_2.grid(row=3,column=0,sticky="w",padx=50,pady=20)
        self.frame2_btn.grid(row=2,column=0)

         #END ########################################################################################

        #Frame 3 Configuration for second labelled frame ######################################################
        #frame for componants for fisrt labeled frame  row configure
        self.frame_right.grid_rowconfigure(0, weight=1)
        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(2, weight=1)
        #frame for componants for fisrt labeled frame column configure
        self.frame_right.columnconfigure(0, weight=1)
        #END#####################################################################################


        #Componants for frame 1 #######################################################################
         #componants 1 frame
        self.frame_comp_3 = Frame(self.frame_right,bg="#232526")
        #componants 1 frame row config
        self.frame_comp_3.grid_rowconfigure(0, weight=1)
        self.frame_comp_3.grid_rowconfigure(1, weight=1)
        self.frame_comp_3.grid_rowconfigure(2, weight=1)
        self.frame_comp_3.grid_rowconfigure(3, weight=1)
        #componants 1 frame column config
        self.frame_comp_3.columnconfigure(0, weight=1)
        #componants 1 frame grid
        self.frame_comp_3.grid(row=0,column=0,sticky="nsew")
        
        
        
        #componants for frame 1
        self.label_frame_3 = Label(self.frame_comp_3,text="STATUS",padx=50,pady=30,bg="#232526",fg="white",font=self.frame2_font)
        self.frame3_progress1 = Progressbar(self.frame_comp_3, orient = HORIZONTAL, length = 200, mode = 'determinate')
        self.frame3_progress2 = Progressbar(self.frame_comp_3, orient = HORIZONTAL, length = 200, mode = 'determinate')
        self.frame3_progress3 = Progressbar(self.frame_comp_3, orient = HORIZONTAL, length = 200, mode = 'determinate')
        self.frame3_btn = Button(self.frame_right,text="Continue",height = 2, width = 8,bg="#232526",fg="white")
        self.frame3_progress1['value']=25
        self.frame3_progress2['value']=50
        self.frame3_progress3['value']=75
        

        #componants grid
        self.label_frame_3.grid(row=0,column=0,sticky="w")
        self.frame3_progress1.grid(row=1,column=0,sticky="w",padx=50,pady=20)
        self.frame3_progress2.grid(row=2,column=0,sticky="w",padx=50,pady=20)
        self.frame3_progress3.grid(row=3,column=0,sticky="w",padx=50,pady=20)
        self.frame3_btn.grid(row=2,column=0)

         #END ########################################################################################


        #frame 4#####################################################################################
        self.frame_left2.grid_rowconfigure(0, weight=1)
        self.frame_left2.columnconfigure(0, weight=1)
        
        self.frame_comp_4 = Frame(self.frame_left2,bg="#232526")
        self.frame_comp_4.grid(row=0,column=0,sticky="nsew")
        
        self.frame_comp_4.grid_rowconfigure(0,weight=1)
        self.frame_comp_4.grid_columnconfigure(0,weight=1)
        
        
        self.frame4_progress = Progressbar(self.frame_comp_4, orient = HORIZONTAL, length = 200, mode = 'determinate')
        self.frame4_progress.grid(row=0,column=0)
        #END

        
        #frame 5#####################################################################################
        self.frame_center2.grid_rowconfigure(0, weight=1)
        self.frame_center2.columnconfigure(0, weight=1)
        self.frame5_button = Button(self.frame_center2,text="Export",height = 2, width = 8,bg="#232526",fg="white")
        self.frame5_button.grid(row=0,column=0,sticky="nsew")
        #END
        
        #frame 6#####################################################################################
        self.frame_right2.grid_rowconfigure(0, weight=1)
        self.frame_right2.columnconfigure(0, weight=1)
        
        self.frame_comp_6 = Frame(self.frame_right2,bg="#232526")
        self.frame_comp_6.grid(row=0,column=0,sticky="nsew")
        #END

        
        

root = Tk()
hack_gui = HackApp(root)
root.mainloop()
