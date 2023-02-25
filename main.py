from tkinter import *
import cv2
import os 
import random
from PIL import Image, ImageTk
from datetime import datetime
from time import time
import time

class System:
    def __init__(self,root):
        self.root = root
        self.root.title("Automate Attendence System")
        self.root.geometry("700x600+300+50")
        self.root.resizable(False,False)
        

        ####################### BACKGROUND IMAGE ####################################################################################################

        Image_Location = "D:/Playground/Projects/Student Attendence/assets/back.jpg"
        image = Image.open(Image_Location)
        image = image.resize((700, 600), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(image)
        self.bg_image = Label(self.root, image = self.bg).place(x = 0 ,y =0, relwidth = 1,relheight =1)
        self.root.wm_iconbitmap("D:/Playground/Projects/Student Attendence/assets/ico.ico")
        ####################### LABEL ######################################################################################################
        
        lbl = Label(self.root, text = 'S T U D E N T  A T T E N D E N C E  S Y S T E M',bg = '#2e2e1f',fg = 'white',font = ("Elephant",13)).pack(fill = X)
        lbl_bottom = Label(self.root, text = 'Design By Koustav Dey',bg = 'black',fg = 'white',anchor = 'center',font = ("times new roman",10)).place(x=150,y=580,width = 340)
        self.lbl_id_down = Label(self.root,text = "None",fg = "white",bg = "black",font = ("times new roman",10))
        self.lbl_id_down.place(x = 490,y=580,relwidth = 0.3)


        ########################    CREATING FRAME ##################################################################
        
        frame1 = Frame(self.root,bd = 2 , relief = RIDGE,bg = "lightgrey")
        frame1.place(x= 30,y=35,width = 300, height = 200)
        frame2 = Frame(self.root,bd = 2 , relief = RIDGE,bg = "lightgrey")
        frame2.place(x= 370,y=35,width = 300, height = 200)

        lbl_reg = Label(frame1, text = 'REGESTRATION'  ,bg = '#2e2e1f',fg = 'white',font = ("times new roman",13)).pack(fill= X)
        lbl_att = Label(frame2, text = 'ATTENDENCE'  ,bg = '#2e2e1f',fg = 'white',font = ("times new roman",13)).pack(fill = X)

        #######################  FRAME1 ############################################################################################################

        frame1_lbl_id = Label(frame1, text = 'ID :',bg = 'lightgrey',fg = '#2e2e1f',font = ("times new roman",12,'bold')).place(x = 4, y = 50)
        self.frame1_lbl_id_data = Label(frame1, text = '',bg = 'lightyellow',fg = '#2e2e1f',font = ("times new roman",12), relief = RIDGE,anchor = 'w')
        self.frame1_lbl_id_data.place(x = 60, y = 50,width = 200)
         
        frame1_lbl_name = Label(frame1, text = 'Name :',bg = 'lightgrey',fg = '#2e2e1f',font = ("times new roman",12,'bold')).place(x = 4, y = 90)
        self.frame1_entry_val = StringVar()
        self.frame1_lbl_entry_name = Entry(frame1,textvariable = self.frame1_entry_val,bg = 'lightyellow',fg = '#2e2e1f',font = ("times new roman",12),bd = 2,relief = RIDGE)
        self.frame1_lbl_entry_name.place(x = 60, y = 90, width  = 200)
        self.frame1_lbl_entry_name.focus()
        
        self.frame1_lbl_btn = Button(frame1,text = 'Take Photo',state = NORMAL,cursor ="hand2",bg = '#3d3d29',fg = 'white',font = ("times new roman",12,'bold'),relief = GROOVE,command = self.fun)
        self.frame1_lbl_btn.place(x = 20, y = 150, width  = 150)
        self.frame1_lbl_btn_stop = Button(frame1,text = 'Stop',state = DISABLED,cursor ="hand2",bg = '#3d3d29',fg = 'white',font = ("times new roman",12,'bold'),relief = GROOVE,command = self.stop)
        self.frame1_lbl_btn_stop.place(x = 195, y = 150,width = 80)

        self.frame1_warnning = Label(frame1, text = '',bg = 'lightgrey',fg = '#2e2e1f',font = ("times new roman",9,'bold'))
        self.frame1_warnning.place(x = 90, y = 125)

        ################################      FRAME 2       #######################################################################################


        frame2_lbl_id_reg = Label(frame2, text = 'ID :',bg = 'lightgrey',fg = '#2e2e1f',font = ("times new roman",12,'bold')).place(x = 4, y = 90)
        self.frame2_lbl_id_data_reg = Label(frame2,text = '',bg = 'lightyellow',anchor='w',fg = '#2e2e1f',font = ("times new roman",12) , relief = RIDGE)
        self.frame2_lbl_id_data_reg.place(x = 60, y =  90, width  = 200)
         
        
        frame2_lbl_name_reg = Label(frame2, text = 'Name :',bg = 'lightgrey',fg = '#2e2e1f',font = ("times new roman",12,'bold')).place(x = 4, y = 50)
        self.frame2_entry_name_val = StringVar()
        self.frame2_lbl_entry_name_reg = Entry(frame2,textvariable=self.frame2_entry_name_val,bg = 'lightyellow',fg = '#2e2e1f',font = ("times new roman",12),bd = 2,relief = RIDGE)
        self.frame2_lbl_entry_name_reg.place(x = 60, y = 50, width  = 200)
        
        self.frame2_lbl_btn_reg = Button(frame2,text = 'Check',state = NORMAL,command = self.match,bg = '#3d3d29',fg = 'white',cursor ="hand2",font = ("times new roman",12,'bold'),relief = GROOVE)
        self.frame2_lbl_btn_reg.place(x = 20, y = 150, width  = 150)
        
        self.frame2_btn_clr = Button(frame2,text = 'Clear',state = DISABLED,command = self.clear,bg = '#3d3d29',fg = 'white',cursor ="hand2",font = ("times new roman",12,'bold'),relief = GROOVE)
        self.frame2_btn_clr.place(x = 195, y = 150, width  = 80)

        self.frame2_lbl = Label(frame2, text = '',anchor = CENTER,bg = 'lightgrey',fg = '#2e2e1f',font = ("times new roman",9,'bold'))
        self.frame2_lbl.place(x = 90, y = 125)

    #######################################  EXTRA  ##########################################################
        self.face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        self.panel = Label(self.root,relief = RIDGE)
        self.panel.place(x = 200,y=280 ,height = 290,width = 290)

        self.panel_lbl = Label(self.root,text = 'User Image',bg ="#ECF0F1",fg = "black",font = ("times new roman",10))
        self.panel_lbl.place(x = 260, y= 530,width = 150)
        self.no = Label(self.root,text = 'Number of Photos',bg ="black",fg = "white",font = ("times new roman",10))
        self.no.place(x = 0, y= 580,width = 150)


        ########################### SUBMIT  ########################################

        self.submit = Button(self.root,text = "Submit",state = DISABLED,cursor ="hand2",bg = '#3d3d29',command = self.submit,fg = 'white',font = ("times new roman",12,'bold'),relief = GROOVE,)
        self.submit.place(x = 30, y = 240,width = 20, relwidth=0.4, relheight=0.05)
        self.check = Button(self.root,text = "Take Attendence",state = DISABLED,command = self.attendence,cursor ="hand2",bg = '#3d3d29',fg = 'white',font = ("times new roman",12,'bold'),relief = GROOVE,)
        self.check.place(x = 370, y = 240,width = 20, relwidth=0.4, relheight=0.05)


    def set_imgpanel(self):
        path_new = "D:/Playground/Projects/Student Attendence/assets/user_path.jpg"
        image1 = Image.open(path_new)
        imgtk = ImageTk.PhotoImage(image = image1)
        self.panel.imgtk = imgtk

    def stop(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.panel_lbl.config(relief = FLAT)
        self.set_imgpanel()
        self.no.config(text = "Number of Photos")
        self.frame1_lbl_btn_stop.config(state = DISABLED)
        
    def face_extractor(self,img):
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = self.face_classifier.detectMultiScale(gray,1.3,5)
        if faces == ():
            return None
      
        for (x,y,w,h) in faces:
            cropped_face = img[y:y+h,x:x+w]
            cv2.rectangle(img,(x,y),(x+w,y+h),(224,224,224),2)
        return cropped_face

    # def gen_random_range(self,min, max):
    #     time_random = time() - float(str(time()).split('.')[0])
    #     return int(time_random * (max - min) + min)

    
    def id_name(self):
        # self.data = self.gen_random_range(500,10000)
        self.data = random.randint(188888,599999)
        self.frame1_lbl_id_data.config(text = self.data)
        print("\nID Genarated")

    def fun(self):
        self.cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.frame1_lbl_btn_stop.config(state = NORMAL)
        
        count = 0
        while True:
            try:
                ret, frame = self.cap.read()
                frame = cv2.flip(frame,1)
                self.panel_lbl.config(bd=2,relief = SOLID)
                if self.face_extractor(frame) is not None:
                    count+=1
                    face = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

                    file_path = 'D:/Playground/Projects/Student Attendence/Sample'
                    if os.path.exists(file_path)==False:
                        os.mkdir(file_path)

                    file_name_path = 'D:/Playground/Projects/Student Attendence/Sample/user' + str(count)+'.jpg' 
                    cv2.imwrite(file_name_path,face)


#####################################################################################################
                # ''' Below Comment Code Save user faces everytime in a unique new folder But Its give a Deprecation Warning ''' 
                # '''  DeprecationWarning: elementwise comparison failed; this will raise an error in the future. if faces == ():'''
                 
                    # a = str(self.data)
                    # file_name_path =os.path.join( 'C:/Users/Darknight/Desktop/Sample/',a)
                    # if os.path.exists(file_name_path)==False:
                    #     os.mkdir(file_name_path)
                    # file_path = file_name_path +'/user' + str(count)+'.jpg' 
                    # cv2.imwrite(file_path,face)

########################################################################################################
                    self.current_image = Image.fromarray(frame)
                    imgtk = ImageTk.PhotoImage(image = self.current_image)
                    self.panel.imgtk = imgtk
                    self.panel.config(image = imgtk)
                    self.no.config(text = f"PLEASE WAIT {count}")
                    self.root.update()
                    print(f'Taking User face Sample Number : {count}')
                else:
                    print("Face Not Found")    
                if cv2.waitKey(1) == 13 or count == 100:
                    self.lbl_id_down.config(text = "ID GENARETED !")
                    break

            except Exception as e:
                return

        self.cap.release()
        cv2.destroyAllWindows()
        self.set_imgpanel()
        self.id_name()
        self.panel_lbl.config(relief = FLAT)
        self.submit.config(state = NORMAL)
        self.no.config(text = "Number of Photos")
        print('\n!!!!!!!!Process Complete!!!!!!!!!!')
        print("\nFace Sample Collected !!!!")
        self.frame1_lbl_btn_stop.config(state = DISABLED)
        self.frame1_lbl_btn.config(state = DISABLED)


    def submit(self):
        if self.frame1_entry_val.get() == '':
            self.frame1_warnning.config(text = 'Name Path is Empty !!',fg = 'red',font = ("Elephant",8))
        else:
            a = self.frame1_entry_val.get()
            sml_wrd = a.lower()
            f = open("data.txt","a")
            f.write(str(self.data)+"  "+sml_wrd+"  ")
            f.close()
            self.frame1_warnning.config(text = '')
            self.frame1_lbl_btn.config(state = NORMAL)
            self.submit.config(state = DISABLED)
            self.frame1_lbl_id_data.config(text="")
            self.frame1_entry_val.set('')
            self.lbl_id_down.config(text = "Data Submitted !")
            print("Data Submitted !")
    

    def match(self):
        f = open("data.txt")
        read_data = f.read()
        split_data = read_data.split("  ")
        len_data = len(split_data)
        self.l1 = []
        self.l2 = []

        for i in range (len_data):
            if i%2==0:
                self.l1.append(split_data[i])
            if i%2!=0:
                self.l2.append(split_data[i])

        self.result_dict = dict(zip(self.l2,self.l1))
        self.val = self.frame2_entry_name_val.get()

        for key,value in self.result_dict.items():
            if self.val == key:
                self.frame2_lbl.config(text = "ID FOUND!",anchor = CENTER, fg = "#004d00", font = ("Elephant",9))
                time.sleep(3)
                print("ID FOUND!")
                self.frame2_lbl_id_data_reg.config(text = value)
                print(value)
                break
        else :
            print("ID NOT FOUND")
            self.frame2_lbl.config(text = "ID NOT FOUND!",anchor = CENTER, fg = "red", font = ("Elephant",9))
            self.frame2_lbl_id_data_reg.config(text = "")
        self.frame2_btn_clr.config(state = NORMAL)
        self.frame2_lbl_btn_reg.config(state = DISABLED)
        self.check.config(state = NORMAL)


    def clear(self):
        self.frame2_lbl_id_data_reg.config(text = "")
        self.frame2_entry_name_val.set('')
        self.frame2_lbl.config(text = '')
        self.frame2_btn_clr.config(state = DISABLED)
        self.frame2_lbl_btn_reg.config(state = NORMAL)


    def attendence(self):
        self.check.config(state = DISABLED)
        self.frame2_lbl_btn_reg.config(state = NORMAL)
        self.clear()
        now = datetime.now()
        date_time = now.strftime('%Y/%m/%d %I:%M:%S')
        f = open("time.txt","a")
        f.write(self.val+" : "+date_time+"\n")
        f.close()
        self.frame2_lbl.config(text = "Attendence Submitted!",anchor = CENTER, fg = "#004d00", font = ("Elephant",9))
        print("Attendence Submitted !")
        self.lbl_id_down.config(text = "Attendence Submitted !")

root = Tk()
obj = System(root)
root.mainloop()