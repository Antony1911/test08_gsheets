# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.title('Treeview demo')
#         self.geometry('620x200')

#         self.tree = self.create_tree_widget()

#     def create_tree_widget(self):
#         columns = ('first_name', 'last_name', 'email')
#         tree = ttk.Treeview(self, columns=columns, show='headings')

#         # define headings
#         tree.heading('first_name', text='First Name')
#         tree.heading('last_name', text='Last Name')
#         tree.heading('email', text='Email')

#         tree.bind('<<TreeviewSelect>>', self.item_selected)
#         tree.grid(row=0, column=0, sticky=tk.NSEW)

#         # add a scrollbar
#         scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=tree.yview)
#         tree.configure(yscroll=scrollbar.set)
#         scrollbar.grid(row=0, column=1, sticky='ns')

#         # generate sample data
#         contacts = []
#         for n in range(1, 100):
#             contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

#         # add data to the treeview
#         for contact in contacts:
#             tree.insert('', tk.END, values=contact)

#         return tree

#     def item_selected(self, event):
#         for selected_item in self.tree.selection():
#             item = self.tree.item(selected_item)
#             record = item['values']
#             # show a message
#             showinfo(title='Information', message=','.join(record))


# if __name__ == '__main__':
#     app = App()
#     app.mainloop()



from tkinter import*
from tkinter import ttk # = for gender
import pymysql  #pymysql
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1500x760+0+0")
 
        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="#15181A",fg="gray")
        title.pack(side=TOP,fill=X)
        
        # ========All Variables ========
        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
            
        # ========== Manage Frame ====
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#1E2124")
        Manage_Frame.place(x=20,y=100,width=450,height=630)
 
        m_title=Label(Manage_Frame,text="Manage Students",bg="#1E2124",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
 
        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="#1E2124",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
 
        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")
 
        lbl_name = Label(Manage_Frame, text="Name", bg="#1E2124", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
 
        txt_name = Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")
 
        lbl_Email = Label(Manage_Frame, text="E-mail", bg="#1E2124", fg="white", font=("times new roman", 20, "bold"))
        lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
 
        txt_Email= Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")
 
        lbl_Gender = Label(Manage_Frame, text="Gender", bg="#1E2124", fg="white", font=("times new roman", 20, "bold"))
        lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")
         
        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",15,"bold"),state='readonly')
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)
 
        lbl_Contact = Label(Manage_Frame, text="Contact", bg="#1E2124", fg="white", font=("times new roman", 20, "bold"))
        lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
         
        txt_Contact = Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")
 
        lbl_Dob = Label(Manage_Frame, text="D.O.B", bg="#1E2124", fg="white",font=("times new roman", 20, "bold"))
        lbl_Dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
         
        txt_Dob = Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")
 
        lbl_Address = Label(Manage_Frame, text="Address", bg="#1E2124", fg="white", font=("times new roman", 20, "bold"))
        lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
         
        self.txt_Address=Text(Manage_Frame,width=20,height=4,font=("",10))
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")
 
        ##-----------------Button Frame
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#1E2124")
        btn_Frame.place(x=10,y=550,width=420)
 
        Addbtn=Button(btn_Frame,text="Add",width=8,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatedbtn = Button(btn_Frame, text="Update", width=8).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=8).grid(row=0, column=2, padx=10, pady=10)
        Clearbtn = Button(btn_Frame, text="Clear", width=8).grid(row=0, column=3, padx=10, pady=10)
 
        ##-----------------Detail Frame
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#1E2124")
        Detail_Frame.place(x=500,y=100,width=980,height=630)
 
        lbl_search = Label(Detail_Frame, text="Search By", bg="#15181A", fg="white", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")
 
        combo_search = ttk.Combobox(Detail_Frame, font=("times new roman", 15, "bold"), state='readonly')
        combo_search['values'] = ("Roll", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)
 
        txt_Search = Entry(Detail_Frame, font=("times new roman", 16, "bold"), bd=5, relief=GROOVE)
        txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")
 
        searchbtn = Button(Detail_Frame, text="Search", width=8).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show All", width=8).grid(row=0, column=4, padx=10, pady=10)
        # --------------Table Frame   farbe  rechts  ?
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="yellow")
        Table_Frame.place(x=10, y=80, width=950, height=530)
 
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame, columns=("roll","name","email","gender","contact","dob","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("Address", text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=30)  ####Breite ############
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=80)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("Address", width=100)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
    def add_students(self):
        con=pymysql.connect(host="localhost",user="root",password="N.....80#",database="stm")   #pymysql
        cur=con.cursor()
        cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_Address.get('1.0',END)
                                                                        ))
        con.commit()
        self.fetch_data()
        con.close()
 
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="N.....80#",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()
 
root=Tk()
ob=Student(root)
root.mainloop()