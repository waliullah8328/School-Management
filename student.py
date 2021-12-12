

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # =========================Variable ===============================
        self.var_class = StringVar()
        self.var_year = StringVar()
        self.var_std_id = StringVar()
        self.var__std_name = StringVar()
        self.var_div = StringVar()
        self.var_rel = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_father = StringVar()
        self.var_mother = StringVar()
        self.var_address = StringVar()
        self.var_parent = StringVar()



        img = Image.open(r"C:\Users\Admin\Desktop\face_recogn_system\colleges_images\Student.jpg")
        img =img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl =Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        img1 = Image.open(r"C:\Users\Admin\Desktop\face_recogn_system\colleges_images\Student1.jpg")
        img1 =img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl =Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        img2 = Image.open(r"C:\Users\Admin\Desktop\face_recogn_system\colleges_images\Student2.jpg")
        img2 =img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl =Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)


        img3 = Image.open(r"C:\Users\Admin\Desktop\face_recogn_system\colleges_images\Studen.png")
        img3 =img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img =Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl = Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg ="red",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        main_frame = Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1480,height=600)

        #left label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=740,height=580)

        img_left = Image.open(r"C:\Users\Admin\Desktop\face_recogn_system\colleges_images\Student_hand_rising.jpg")
        img_left =img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl =Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=720,height=130)

        #Current course
        Current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_course_frame.place(x=10,y=135,width=720,height=115)
        
        Class_label = Label(Current_course_frame,text="Class",font=("times new roman",12,"bold"),bg="white")
        Class_label.grid(row=0,column=0,padx=10)

        Class_combo = ttk.Combobox(Current_course_frame,textvariable=self.var_class,font=("times new roman",12,"bold"),state="read only",width=17)
        Class_combo["values"]= ("Select Class","Six")
        Class_combo.current(0)
        Class_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Year
       
        course_label = Label(Current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo = ttk.Combobox(Current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="read only",width=17)
        course_combo["values"]= ("Select Year","2022","2023","2024","2025")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)



         #Class Student Information 
        Class_student_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information ",font=("times new roman",12,"bold"))
        Class_student_course_frame.place(x=10,y=250,width=720,height=300)

        # Student Roll

        student_Id_label = Label(Class_student_course_frame,text="Student Roll",font=("times new roman",12,"bold"),bg="white")
        student_Id_label.grid(row=0,column=0,padx=10,sticky=W)

        student_Id_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        student_Id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #Student Name

        student_name_label = Label(Class_student_course_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var__std_name,width=20,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

          
        #Student Division

        student_div_label = Label(Class_student_course_frame,text="Student Division",font=("times new roman",12,"bold"),bg="white")
        student_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo = ttk.Combobox(Class_student_course_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="read only",width=18)
        div_combo["values"]= ("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
         
        
     
        # Student Religion

        roll_no_label = Label(Class_student_course_frame,text="Religion",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_rel,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

         #Student Gender

        gender_label = Label(Class_student_course_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

       

        gender_combo = ttk.Combobox(Class_student_course_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="read only",width=18)
        gender_combo["values"]= ("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

           
        #Student DOB

        dob_label = Label(Class_student_course_frame,text="Date of Birth",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

         #Father's name

        father_name_label = Label(Class_student_course_frame,text="Father Name",font=("times new roman",12,"bold"),bg="white")
        father_name_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        father_name_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_father,width=20,font=("times new roman",12,"bold"))
        father_name_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

           
        # Mother Name

        mother_name_label = Label(Class_student_course_frame,text="Mother Name",font=("times new roman",12,"bold"),bg="white")
        mother_name_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        mother_name_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_mother,width=20,font=("times new roman",12,"bold"))
        mother_name_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

         #Student Address

        address_label = Label(Class_student_course_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

           
        #Parent Number

        parent_no_label = Label(Class_student_course_frame,text="Parent Number",font=("times new roman",12,"bold"),bg="white")
        parent_no_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        parent_no_entry = ttk.Entry(Class_student_course_frame,textvariable=self.var_parent,width=20,font=("times new roman",12,"bold"))
        parent_no_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)



        #button Frame
        btn_frame = Frame(Class_student_course_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn =Button(btn_frame,text= "Save",command=self.add_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn =Button(btn_frame,text= "Update",command=self.update_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn =Button(btn_frame,text= "Delete",command=self.delete_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn =Button(btn_frame,text= "Reset",command=self.reset_data,width=19,font=("times new roman",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1 = Frame(Class_student_course_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)




        #Right label frame
        Right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=780,y=10,width=660,height=580)

        img_right = Image.open(r"C:\Users\Admin\Desktop\face_recogn_system\colleges_images\Student3.jpg")
        img_right =img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(Right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=720,height=130)

        # +===============Search System==============
        Search_frame = LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        Search_frame.place(x=10,y=135,width=710,height=70)

        search_label = Label(Search_frame,text="Search By",font=("times new roman",15,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo = ttk.Combobox(Search_frame,font=("times new roman",12,"bold"),state="read only",width=15)
        search_combo["values"]= ("Select","Roll Number","Phone Number","")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry = ttk.Entry(Search_frame,width=15,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn =Button(Search_frame,text= "Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn =Button(Search_frame,text= "Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        # ====================table frame==================
        table_frame =Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=210,width=710,height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,columns=("class","year","rel","name","div","rele","gender","dob","father","mother","address","parent"),xscrollcommand = scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)  
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)



        self.student_table.heading("class",text="Class")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("rel",text="Roll No")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("rele",text="Religion")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Date of Birth")
        self.student_table.heading("father",text="Father Name")
        self.student_table.heading("mother",text="Mother Name")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("parent", text="Parent Number")
        self.student_table["show"]="headings"

        self.student_table.column("class",width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("rel",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("rele",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("father",width=100)
        self.student_table.column("mother",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("parent", width=100)


        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
    # ==================Function Declaration ====================
    def add_data(self):
        if self.var_class.get()=="Select Class" or self.var__std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fileds are required",parent = self.root)
        else:
            try:
                conn =mysql.connector.connect(
                    host="localhost",
                    user="root",password = "",
                    database= "face_recognition"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_class.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_std_id.get(),
                                                                                                                self.var__std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_rel.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_father.get(),
                                                                                                                self.var_mother.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_parent.get(),

                    



                                                                                                                       ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student Details has been added Successfully",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent = self.root)


    # =================fetchdata=============
    def fetch_data(self):
        conn =mysql.connector.connect(
                    host="localhost",
                    user="root",password = "",
                    database= "face_recognition"
                )
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #=====================getcursor==============
    def get_cursor(self,event=""):
        cursor_focus =self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_class.set(data[0]),
        self.var_year.set(data[1]),
        self.var_std_id.set(data[2]),
        self.var__std_name.set(data[3]),
        self.var_div.set(data[4]),
        self.var_rel.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_dob.set(data[7]),
        self.var_father.set(data[8]),
        self.var_mother.set(data[9]),
        self.var_address.set(data[10]),
        self.var_parent.set(data[11]),


    # ==================Update Function=============
    def update_data(self):
        if self.var_class.get()=="Select Class" or self.var__std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fileds are required",parent = self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update student details",parent= self.root)
                if Update>0:
                    conn =mysql.connector.connect(
                    host="localhost",
                    user="root",password = "",
                    database= "face_recognition"
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Class_Name =%s,Year=%s,Student_Name=%s,Division=%s,Religion=%s,Gender=%s,Date_Of_Birth=%s,Father_name=%s,Mother_Name=%s,Address=%s,Parent_Number=%s where Student_Id=%s",(
                                                                                                                self.var_class.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var__std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_rel.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_father.get(),
                                                                                                                self.var_mother.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_parent.get(),
                                                                                                                self.var_std_id.get()
                                                                                                                

                                                                                                                        ))
                else:
                    if not Update:
                        return 
                messagebox.showinfo("Success","Student details successfully updated",parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent= self.root)

     # delete function ================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent = self.root)   
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn =mysql.connector.connect(
                    host="localhost",
                    user="root",password = "",
                    database= "face_recognition"
                    )
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_Id=%s"
                    val =(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent = self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent= self.root)  

    # ================================reset function===============================  
    def reset_data(self):
        self.var_class.set("Select Class")
        self.var_year.set("Select Year"),
        self.var_std_id.set(""),
        self.var__std_name.set(""),
        self.var_div.set("Select Division"),
        self.var_rel.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_father.set(""),
        self.var_mother.set(""),
        self.var_address.set(""),
        self.var_parent.set("")

    # ===================Generate data set take photo sample=====================
    def generate_dataset(self):
        if self.var_class.get()=="Select Class" or self.var__std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All fileds are required",parent = self.root)
        else:
            try:
                
                conn =mysql.connector.connect(
                host="localhost",
                user="root",password = "",
                database= "face_recognition"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult= my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Class_Name =%s,Year=%s,Student_Name=%s,Division=%s,Religion=%s,Gender=%s,Date_Of_Birth=%s,Father_Name=%s,Mother_Name=%s,Address=%s,Parent_Number=%s where Student_Id=%s",(
                                                                                                                self.var_class.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var__std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_rel.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_father.get(),
                                                                                                                self.var_mother.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_parent.get(),
                                                                                                                self.var_std_id.get()==id+1
                                                                                                                

                                                                                                                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()  
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent= self.root)







                                                                                                                      




        



if __name__ == "__main__":

    root = Tk()
    obj =Student(root)
    root.mainloop()