import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from tkinter.simpledialog import askstring
import tkinter.messagebox as MessageBox
import mysql.connector

class Table:
    total_rows = 0
    total_columns = 0
    lst = list()
    def __init__(self,root):

        # code for creating table
        for i in range(Table.total_rows):
            for j in range(Table.total_columns):
                if i == 0:
                    self.e = tk.Entry(root, width=18, fg='black', font=('Arial',10,'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(tk.END, Table.lst[i][j])
                    continue
                self.e = tk.Entry(root, width=18, fg='blue', font=('Arial',10))
                self.e.grid(row=i, column=j)
                self.e.insert(tk.END, Table.lst[i][j])

class MySQLDatabase:
    def __init__(self, host, username, password="00000000", database='Hospital'):
        self.connection = mysql.connector.connect(
            host=host,
            user=username,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, parameters=None):
        try:
            self.cursor.execute(query, parameters)
            return self.cursor.fetchall()
        except mysql.connector.Error as error:
            print(f"Error executing query: {error}")

    def insert_data(self, table, data):
        placeholders = ", ".join(["%s"] * len(data))
        columns = ", ".join(data.keys())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.execute_query(query, tuple(data.values()))

    def update_data(self, table, data, condition):
        set_clause = ", ".join([f"{column} = %s" for column in data.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE {condition}"
        self.execute_query(query, tuple(data.values()))

    def delete_data(self, table, condition):
        query = f"DELETE FROM {table} WHERE {condition}"
        self.execute_query(query)

    def __del__(self):
        self.connection.close()

class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # creating a container
        container = tk.Frame(self)
        self.geometry("600x600") 
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        # initializing frames to an empty dictionary
        self.frames = {} 
        for F in (StaffLogin, PatientLogin, PatientRegistration, AdminPage, PatientPage, DoctorPage, NursePage, NMSPage, forgotPID, forgotPassPat, forgotPassStf):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(PatientLogin)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StaffLogin(tk.Frame):
    ids = ""
    passw = ""
    def __init__(self, parent, controller):
        self.db = MySQLDatabase("localhost", "root")
        self.db.connection.autocommit = True
        tk.Frame.__init__(self, parent)
        def getdat():
            StaffLogin.ids = idtt.get()
            idtt.delete(0, tk.END)
            StaffLogin.passw = patt.get()
            patt.delete(0, tk.END)
            if StaffLogin.ids == "" or StaffLogin.passw == "":
                MessageBox.showwarning("Login Status", "All Field are Required!!!")
            else:
                if len(StaffLogin.ids) <=8:
                    passchk = self.db.execute_query(f"Select `password` from staff where s_id='{StaffLogin.ids}'")[0][0]
                    if passchk != StaffLogin.passw:
                        MessageBox.showerror("Login Error", "Wrong Password or Non-Existent user")
                        controller.show_frame(StaffLogin)
                        return
                    if StaffLogin.ids[0:3] == "DOC":
                        if StaffLogin.ids == "DOC0000":
                            controller.show_frame(AdminPage)
                        else:
                            controller.show_frame(DoctorPage)
                    elif StaffLogin.ids[0:3] == "NUR":
                        controller.show_frame(NursePage)
                    else:
                        controller.show_frame(NMSPage)

        titletext = tk.Label(master=self, text="Staff Login", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

        idss = tk.Label(master = logframe, text="Enter your ID")
        idss.grid(row = 0, column = 0, sticky=tk.W+tk.E)

        idtt = tk.Entry(master = logframe)
        idtt.grid(padx=20, row = 0, column = 1, sticky=tk.W+tk.E)

        passw = tk.Label(master = logframe, text="Password")
        passw.grid(row = 1, column = 0, sticky=tk.W+tk.E)

        patt = tk.Entry(master = logframe,show="*")
        patt.grid(padx=20, row = 1, column = 1, sticky=tk.W+tk.E)

        logframe.pack(pady = 20, fill='x')

        button = tk.Button(master=self, command=getdat, text="Login")
        button.pack(padx = 100,pady = 20)

        button1 = ttk.Button(self, text ="Patient Login", command = lambda : controller.show_frame(PatientLogin))
        # putting the button in its place by
        # using grid
        button1.pack(padx = 10, pady = 10)
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Patient Registration", command = lambda : controller.show_frame(PatientRegistration))
        # putting the button in its place by
        # using grid
        button2.pack(padx = 10, pady = 10)
        button3 = ttk.Button(self, text ="Forgot Password", command = lambda : controller.show_frame(forgotPassStf))
        # putting the button in its place by
        # using grid
        button3.pack(padx = 10, pady = 10)

class PatientLogin(tk.Frame):
    ids=""
    passw=""
    def __init__(self, parent, controller):
        self.db = MySQLDatabase("localhost", "root")
        self.db.connection.autocommit = True
        tk.Frame.__init__(self, parent)
        def getdat():
            PatientLogin.ids = idtt.get()
            idtt.delete(0, tk.END)
            PatientLogin.passw = patt.get()
            patt.delete(0, tk.END)
            if PatientLogin.ids == "" or PatientLogin.passw == "":
                MessageBox.showwarning("Login Status", "All Field are Required!!!")
            else:
                if len(PatientLogin.ids) <=8:
                    passchk = self.db.execute_query(f"Select `password` from patient where p_id='{PatientLogin.ids}'")[0][0]
                    if passchk != PatientLogin.passw:
                        MessageBox.showerror("Login Error", "Wrong Password or Non-Existent user")
                        controller.show_frame(PatientLogin)
                        return
                    else:
                        controller.show_frame(PatientPage)

        titletext = tk.Label(master=self, text="Patient Login", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

        idss = tk.Label(master = logframe, text="Enter your ID")
        idss.grid(row = 0, column = 0, sticky=tk.W+tk.E)

        idtt = tk.Entry(master = logframe)
        idtt.grid(padx=20, row = 0, column = 1, sticky=tk.W+tk.E)

        passw = tk.Label(master = logframe, text="Password")
        passw.grid(row = 1, column = 0, sticky=tk.W+tk.E)

        patt = tk.Entry(master = logframe, show="*")
        patt.grid(padx=20, row = 1, column = 1, sticky=tk.W+tk.E)

        logframe.pack(pady = 20, fill='x')

        button = tk.Button(master=self, command=getdat, text="Login")
        button.pack(padx = 100,pady = 20)

        button1 = ttk.Button(self, text ="Staff Login", command = lambda : controller.show_frame(StaffLogin))
        # putting the button in its place by
        # using grid
        button1.pack(padx = 10, pady = 10)
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Patient Registration", command = lambda : controller.show_frame(PatientRegistration))
        # putting the button in its place by
        # using grid
        button2.pack(padx = 10, pady = 10)
        button3 = ttk.Button(self, text ="Forgot Patient ID", command = lambda : controller.show_frame(forgotPID))
        # putting the button in its place by
        # using grid
        button3.pack(padx = 10, pady = 10)
        button4 = ttk.Button(self, text ="Forgot Password", command = lambda : controller.show_frame(forgotPassPat))
        # putting the button in its place by
        # using grid
        button4.pack(padx = 10, pady = 10)

class PatientRegistration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.db = MySQLDatabase("localhost", "root")
        self.db.connection.autocommit = True

        def getdat():
            name = nmtt.get()
            gndr = gntt.get(gntt.curselection())
            phnum = phtt.get()
            adr = adtt.get("1.0", tk.END)
            pwd1 = passwordtt.get()
            pwd2 = passrett.get()
            if name == "" or phnum == "" or adr=="" or pwd1=="" or pwd2=="":
                MessageBox.showwarning("Registration Status", "All Field are Required!!!")
            else:
                if not phnum.isdigit() or len(phnum)!=10:
                    MessageBox.showerror("Registration Status", "Enter Valid Phone No.")
                    phtt.delete(0,tk.END)
                    return
                elif pwd2!=pwd1:
                    MessageBox.showerror("Registration Status", "Passwords don't match")
                    passwordtt.delete(0, tk.END)
                    passrett.delete(0, tk.END)
                    return
                elif gndr == "None":
                    MessageBox.showerror("Registration Status", "Please Select Your Gender")
                    return
                elif gndr == "Others":
                    gndr = askstring("Gender", "What is your gender?")
                    MessageBox.showinfo("Patient Gender", "Gender {} registered succesfully".format(gndr))
                result = self.db.execute_query(f"insert into PATIENT (p_name,gender,address,`Ph.No.`,`password`) VALUES('{name}','{gndr}','{adr}','{phnum}','{pwd1}')")
                nmtt.delete(0, tk.END)
                gntt.select_set(0)
                phtt.delete(0, tk.END)
                passrett.delete(0, tk.END)
                passwordtt.delete(0, tk.END)
                adtt.delete("1.0",tk.END)
                id = self.db.execute_query(f"SELECT p_id from patient order by p_id desc limit 1")[0][0]
                MessageBox.showinfo("Registration Done", f"Remember: Your Patient ID is {id}")
                controller.show_frame(PatientLogin)

        titletext = tk.Label(master=self, text="Patient Registration", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)

        nm = tk.Label(master = logframe, text="Full Name").grid(row = 0, column = 0, sticky=tk.W+tk.E)
        nmtt = tk.Entry(master = logframe)
        nmtt.grid(pady=10, padx=10, row = 0, column = 1, sticky=tk.W+tk.E)

        phno = tk.Label(master = logframe, text="Phone No.").grid(row = 0, column =2, sticky=tk.W+tk.E)
        phtt = tk.Entry(master = logframe)
        phtt.grid(pady=10, padx=10, row = 0, column = 3, sticky=tk.W+tk.E)

        gnd = tk.Label(master=logframe, text="Gender").grid(row=1,column=0,sticky=tk.W+tk.E)

        gntt = tk.Listbox(master=logframe, height=8, exportselection=False)
        gntt.insert(1, "None")
        gntt.insert(2, "Male")
        gntt.insert(3, "Female")
        gntt.insert(4, "Transgender")
        gntt.insert(5, "Non-Binary")
        gntt.insert(6, "Intersex")
        gntt.insert(7, "Others")
        gntt.select_set(0)
        gntt.grid(pady=10, padx=10, row=1, column=1, sticky=tk.E+tk.W)

        add = tk.Label(master=logframe, text = "Address").grid(row = 1, column = 2, sticky=tk.W+tk.E)
        adtt = tk.Text(master = logframe, height=8, width=25)
        adtt.grid(pady=10, padx=10, row = 1, column = 3, sticky=tk.W+tk.E)

        password = tk.Label(master=logframe, text="Password").grid(padx=10, row= 4, column=0, sticky=tk.E+tk.W)
        passwordtt = tk.Entry(master=logframe, show="*")
        passwordtt.grid(pady=10, padx=10, row=4, column=1, sticky=tk.E+tk.W)

        passret = tk.Label(master=logframe, text="Re-Enter Password").grid(padx=10, row = 4, column=2, sticky= tk.E+tk.W)
        passrett = tk.Entry(master=logframe,show="*")
        passrett.grid(pady=10, padx=10, row=4, column=3, sticky=tk.E+tk.W)

        logframe.pack(pady = 20, fill='x')

        button = tk.Button(master=self, command=getdat, text="Register")
        button.pack(padx = 10,pady = 10)

        button1 = ttk.Button(self, text ="Staff Login", command = lambda : controller.show_frame(StaffLogin))
        # putting the button in its place by
        # using grid
        button1.pack(padx = 10, pady = 10)
        ## button to show frame 2 with text layout2
        button2 = ttk.Button(self, text ="Patient Login", command = lambda : controller.show_frame(PatientLogin))
        # putting the button in its place by
        # using grid
        button2.pack(padx = 10, pady = 10)

class AdminPage(tk.Frame):
    s_id = ""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.db = MySQLDatabase("localhost", "root")
        self.db.connection.autocommit = True

        def getDate():
            stafframe.pack_forget()
            retdat.pack(padx=10, pady=10)

        def retSet():
            id = idtt.get()
            date = cal.get_date()
            if id == "":
                MessageBox.showerror("Operation Failed", "No ID Entered")
                return
            self.db.execute_query(f"update staff set retirement='{date}' where s_id='{id}'")
            idtt.delete(0, tk.END)
            cal.selection_clear()
            retdat.pack_forget()
            if self.db.cursor.rowcount !=1:
                MessageBox.showerror("Operation Failed", "No such User Exists")
                return

        def changePass():
            newpass = askstring("Change Password", "Enter New Password Here")
            if newpass =="":
                return
            MessageBox.showinfo("New Password", f"Changed Password is {newpass}")
            self.db.execute_query(f"update staff set `password` = '{newpass}' where s_id='DOC0000'")
        
        def addStaff():
            retdat.pack_forget()
            stafframe.pack(padx=10,pady=0)

        def showStaff():
            Table.lst = self.db.execute_query(f"select s_id, s_name, joining, `Ph.No.`, Address, Gender, Salary from staff order by s_id")
            Table.lst.insert(0,("ID","Name", "Joining Date", "Ph.No.", "Address", "Gender", "Salary"))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showstff = tk.Tk()
            t = Table(showstff)
            showstff.geometry("1000x600")
            showstff.mainloop()

        def showPatient():
            Table.lst = self.db.execute_query(f"select p_id, p_name, `Ph.No.`, Address, Gender from patient")
            Table.lst.insert(0,("ID","Name", "Ph.No.", "Address", "Gender"))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showstff = tk.Tk()
            t = Table(showstff)
            showstff.geometry("1000x600")
            showstff.mainloop()

        def changeSalary():
            chanid = askstring("Change Salary", "Enter Staff ID")
            if len(chanid) >8:
                MessageBox.showerror("Operation Failed", "Invalid ID entered")
                return
            chansal = askstring("Change Salary", "Enter Value in Decimals")
            if not chansal.isdecimal():
                MessageBox.showerror("Operation Failed", "Enter valid salary, in decimal format")
                return
            result = self.db.execute_query(f"UPDATE STAFF SET SALARY={chansal} WHERE s_id='{chanid}'")
            if self.db.cursor.rowcount == 1:
                MessageBox.showinfo("Salary Change", f"Salary of {chanid} changed to {chansal}")
                return
            MessageBox.showerror("Operation Failed", "Unable to update salary")

        def changePhone():
            newPh = askstring("Change Phone No.", "Enter New Phone No.")
            if newPh=="" or not newPh.isdigit or len(newPh)!=10:
                MessageBox.showerror("Operation Failed", "Please Enter a valid No.")
                return
            MessageBox.showinfo("New Phone No.", f"Changed Number is {newPh}")
            self.db.execute_query(f"update staff set `Ph.No.` = '{newPh}' where s_id='{StaffLogin.ids}'")

        def addRoom():
            dept = askstring("Room Addition", "Write Room type between VIP,General,Children,Public")
            fee = askstring("Fee per day","Enter Room Fee per day")
            if dept=="" or dept not in ("VIP", "General", "Children", "Public"):
                MessageBox.showerror("Operation Fail", "Invalid name given")
                return
            elif not fee.isdigit():
                MessageBox.showerror("Operation Fail", "Invalid Fee value given")
                return
            self.db.execute_query(f"insert into room(r_type, room_fee_per_day) values('{dept}',{fee})")
            if self.db.cursor.rowcount != 1:
                MessageBox.showerror("Operation fail", f"Room {dept} could not be added")

        def addDep():
            dept = askstring("Department Addition", "Write Department name to be added")
            if dept=="":
                MessageBox.showerror("Operation Fail", "No Department name given")
            self.db.execute_query(f"insert into departments(dep_name) values('{dept}')")
            if self.db.cursor.rowcount != 1:
                MessageBox.showerror("Operation fail", f"Department {dept} could not be added")

        def getdat():
            name = nmtt.get()
            gndr = gntt.get(gntt.curselection())
            phnum = phtt.get()
            adr = adtt.get("1.0", tk.END)
            spec = speclist.curselection()
            spec = spec[0] + 1
            stftyp = typelist.get(typelist.curselection())
            senior = ""
            dutype = ""
            salary = saltt.get()
            pwd1 = passwordtt.get()
            pwd2 = passrett.get()
            if name == "" or phnum == "" or adr=="" or pwd1=="" or pwd2=="" or salary=="":
                MessageBox.showwarning("Registration Status", "All Field are Required!!!")
            else:
                if not phnum.isdigit() or len(phnum)!=10:
                    MessageBox.showerror("Registration Status", "Enter Valid Phone No.")
                    phtt.delete(0,tk.END)
                    return
                elif not salary.isdecimal():
                    MessageBox.showerror("Registration Status", "Enter Valid Salary Amount")
                    saltt.delete(0,tk.END)
                    return
                elif pwd2!=pwd1:
                    MessageBox.showerror("Registration Status", "Passwords don't match")
                    passwordtt.delete(0, tk.END)
                    passrett.delete(0, tk.END)
                    return
                elif gndr == "None":
                    MessageBox.showerror("Registration Status", "Please Select Your Gender")
                    return
                elif gndr == "Others":
                    gndr = askstring("Gender", "What is your gender?")
                    MessageBox.showinfo("Staff Gender", "Gender {} registered succesfully".format(gndr))
                elif stftyp == "Nurse":
                    senior = askstring("Seniority", "Choose between Junior, Experienced and Senior")
                    MessageBox.showinfo("Nurse Seniority",f'Nurse Seniority set to {senior}')
                elif stftyp == "Non-Medical Staff":
                    dutype = askstring("Duty", "Please enter staff duty")
                    MessageBox.showinfo("Non-Medical Duty", f'Staff duty set as {dutype}')
                
                stafframe.pack_forget()
                if stftyp == "Doctor":
                    s_id = self.db.execute_query(f"select convert(substring(s_id,4,4),unsigned) + 1 from doctor order by s_id desc limit 1")[0][0]

                    result = self.db.execute_query(f"INSERT INTO Doctor(s_id, dep_id) values (concat('DOC',LPAD({s_id},4,0)),{spec})")
                    result = self.db.execute_query(f"Insert into staff(s_id,s_name,salary,joining,`Ph.No.`,Address, `password`, gender) select s_id,'{name}', {salary}, current_date, '{phnum}', '{adr}', '{pwd1}', '{gndr}' from doctor order by s_id desc limit 1")
                elif stftyp == "Nurse":
                    s_id = self.db.execute_query(f"select convert(substring(s_id,4,4),unsigned) + 1 from nurse order by s_id desc limit 1")[0][0]

                    result = self.db.execute_query(f"INSERT INTO Nurse(s_id, dep_id, seniority) values (concat('NUR',LPAD({s_id},4,0)),{spec}, '{senior}')")
                    result = self.db.execute_query(f"Insert into staff(s_id,s_name,salary,joining,`Ph.No.`,Address, `password`, gender) select s_id,'{name}', {salary}, current_date, '{phnum}', '{adr}', '{pwd1}', '{gndr}' from nurse order by s_id desc limit 1")
                else:
                    s_id = self.db.execute_query(f"select convert(substring(s_id,4,4),unsigned) + 1 from `non-medical staff` order by s_id desc limit 1")[0][0]

                    result = self.db.execute_query(f"INSERT INTO `Non-Medical Staff`(s_id, duty_type) values (concat('NMS',LPAD({s_id},4,0)),'{dutype}')")
                    result = self.db.execute_query(f"Insert into staff(s_id,s_name,salary,joining,`Ph.No.`,Address, `password`, gender) select s_id,'{name}', '{salary}', current_date, '{phnum}', '{adr}', '{pwd1}', '{gndr}' from `Non-Medical Staff` order by s_id desc limit 1")
                nmtt.delete(0,tk.END)
                phtt.delete(0,tk.END)
                adtt.delete("1.0",tk.END)
                saltt.delete(0,tk.END)
                passrett.delete(0,tk.END)
                passwordtt.delete(0,tk.END)
                speclist.select_set(0)
                typelist.select_set(0)
                gntt.select_set(0)

        titletext = tk.Label(master=self, text="Welcome Admin", font=("Arial bold", 18)).pack(pady=10)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

        button1 = tk.Button(master=logframe, text="Change Password", command=changePass).grid(padx=10, pady=10, row=0, column=0)

        button10 = tk.Button(master=logframe, text="Change Phone No.", command=changePhone).grid(padx=10, pady=10, row=2, column=0)

        button2 = tk.Button(master=logframe, text="Add Staff", command=addStaff).grid(padx=10, pady=10, row=0, column=1)

        button3 = tk.Button(master=logframe, text="Observe Staff", command=showStaff).grid(padx=10, pady=10, row=0, column=2)

        button4 = tk.Button(master=logframe, text="Observe Patients", command=showPatient).grid(padx=10, pady=10, row=1, column=0)

        button5 = tk.Button(master=logframe, text="Change Salary", command=changeSalary).grid(padx=10, pady=10, row=1, column=1)

        button6 = tk.Button(master=logframe,text="Logout", command = lambda : controller.show_frame(StaffLogin)).grid(padx=10, pady=0, row=3, column=1)

        button8 = tk.Button(master=logframe, text="Retire Staff", command=getDate).grid(padx=10, pady=10, row=1,column=2)

        button11 = tk.Button(master=logframe, text="Add Room", command=addRoom).grid(padx=10, pady=10, row=2, column=1)

        button12 = tk.Button(master=logframe, text="Add Department", command=addDep).grid(padx=10, pady=10, row=2, column=2)

        logframe.pack(padx=20, pady=20)

        stafframe = tk.Frame(master=self)
        nm = tk.Label(master = stafframe, text="Full Name").grid(row = 0, column = 0, sticky=tk.W+tk.E)
        nmtt = tk.Entry(master = stafframe)
        nmtt.grid(pady=10, padx=20, row = 0, column = 1, sticky=tk.W+tk.E)

        gnd = tk.Label(master=stafframe, text="Gender").grid(row=1,column=0,sticky=tk.W+tk.E)

        gntt = tk.Listbox(master=stafframe, height=8, exportselection=False)
        gntt.insert(1, "None")
        gntt.insert(2, "Male")
        gntt.insert(3, "Female")
        gntt.insert(4, "Transgender")
        gntt.insert(5, "Non-Binary")
        gntt.insert(6, "Intersex")
        gntt.insert(7, "Others")
        gntt.select_set(0)
        gntt.grid(pady=10, padx=20, row=1, column=1, sticky=tk.E+tk.W)

        phno = tk.Label(master = stafframe, text="Phone No.").grid(row = 0, column = 2, sticky=tk.W+tk.E)
        phtt = tk.Entry(master = stafframe)
        phtt.grid(pady=10, padx=10, row = 0, column = 3, sticky=tk.W+tk.E)

        add = tk.Label(master=stafframe, text = "Address").grid(row = 1, column = 2, sticky=tk.W+tk.E)
        adtt = tk.Text(master = stafframe, height=8)
        adtt.grid(pady=10, padx=10, row = 1, column = 3, sticky=tk.W+tk.E)

        password = tk.Label(master=stafframe, text="Password").grid(padx=10, row= 2, column=0, sticky=tk.E+tk.W)
        passwordtt = tk.Entry(master=stafframe, show="*")
        passwordtt.grid(pady=10, padx=10, row=2, column=1, sticky=tk.E+tk.W)

        passret = tk.Label(master=stafframe, text="Re-Enter Password").grid(padx=10, row = 2, column=2, sticky= tk.E+tk.W)
        passrett = tk.Entry(master=stafframe,show="*")
        passrett.grid(pady=10, padx=10, row=2, column=3, sticky=tk.E+tk.W)

        typelab = tk.Label(master=stafframe, text="Staff Type").grid(padx=10, row=3, column=0)
        typelist = tk.Listbox(master=stafframe, height=4, exportselection=False)
        typelist.insert(1, "Doctor")
        typelist.insert(2, "Nurse")
        typelist.insert(3, "Non-Medical Staff")
        typelist.select_set(0)
        typelist.grid(padx=10, row=3, column=1, sticky=tk.E+tk.W)

        speclab = tk.Label(master=stafframe, text="Department").grid(padx=10, row=3, column=2)
        speclist = tk.Listbox(master=stafframe, height=4, exportselection=False)
        result = self.db.execute_query("Select dep_name from departments")
        result = list(result)
        for i in result:
            speclist.insert(tk.END, i)
        speclist.select_set(0)
        speclist.grid(padx=10, row=3, column=3, sticky=tk.E+tk.W)

        sallab = tk.Label(master=stafframe, text="Salary").grid(padx=10, row = 4, column=0)
        saltt = tk.Entry(master=stafframe)
        saltt.grid(padx=10,pady=10, row=4, column=1)

        button7 = tk.Button(master=stafframe, text="Add Staff", command=getdat).grid(pady=10, row=4, column=2)

        retdat= tk.Frame(master=self)

        labelret = tk.Label(master=retdat, text="Staff ID").pack(padx=10)
        idtt = tk.Entry(master=retdat)
        idtt.pack(padx=10, pady=10)
        cal = Calendar(master=retdat, selectmode = 'day', date_pattern='yyyy-mm-dd')
        cal.pack(pady=10, padx=10)
        button9 = tk.Button(master=retdat, text="Set Retirement", command=retSet).pack(padx=10, pady=10)

class PatientPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.db = MySQLDatabase("localhost", "root")
        self.db.connection.autocommit = True
        titletext = tk.Label(master=self, text="Welcome Back", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

        def showDetails():
            Table.lst = self.db.execute_query(f"select p.p_id,p.p_name,p.gender,p.address,p.`Ph.No.` from patient as p where p.p_id={PatientLogin.ids}")
            Table.lst.insert(0,('Patient ID','Patient Name','Gender','Address','Ph.No.'))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showApp = tk.Tk()
            t = Table(showApp)
            showApp.geometry("1000x600")
            showApp.mainloop()

        def changePhone():
            newPh = askstring("Change Phone No.", "Enter New Phone No.")
            if newPh=="" or not newPh.isdigit or len(newPh)!=10:
                MessageBox.showerror("Operation Failed", "Please Enter a valid No.")
                return
            MessageBox.showinfo("New Phone No.", f"Changed Number is {newPh}")
            self.db.execute_query(f"update patient set `Ph.No.` = '{newPh}' where s_id='{PatientLogin.ids}'")

        def changePass():
            s_id = PatientLogin.ids
            newpass = askstring("Change Password", "Enter New Password Here")
            if newpass =="":
                MessageBox.showerror("Operation Cancelled", "Operation wasn't completed")
                return
            MessageBox.showinfo("New Password", f"Changed Password is {newpass}")
            self.db.execute_query(f"update patient set `password` = '{newpass}' where s_id='{s_id}'")

        def showHistory():
            pass

        def makeAppointment():
            pass

        def delAppoint():
            pass

        def acceptProc():
            pass

        def showDiag():
            pass

        def showBill():
            pass

        button1 = tk.Button(master=logframe, text="Check Details", command=showDetails).grid(padx=10, pady=20, row=0, column=0)

        button2 = tk.Button(master=logframe, text="Change Password", command=changePass).grid(padx=10, pady=20, row=0, column=1)

        button3 = tk.Button(master=logframe, text="Check History", command=showHistory).grid(padx=10, pady=20, row=0, column=2)

        button4 = tk.Button(master=logframe, text="Make Appointment", command=makeAppointment).grid(padx=10, pady=20, row=1, column=0)

        button5 = tk.Button(master=logframe, text="Delete Appointment", command=delAppoint).grid(padx=10, pady=20, row=1, column=1)

        button6 = tk.Button(master=logframe, text="Accept Procedure", command=acceptProc).grid(padx=10, pady=20, row=1, column=2)

        button7 = tk.Button(master=logframe, text="Show Diagnosis", command=showDiag).grid(padx=10, pady=20, row=2, column=0)

        button8 = tk.Button(master=logframe, text="Show Bill", command=showBill).grid(padx=10, pady=20, row=2, column=1)

        button9 = tk.Button(master=logframe, text="Logout", command= lambda : controller.show_frame(PatientLogin)).grid(padx=10, pady=20, row=2, column=2)

        logframe.pack(padx=10, pady=20)

class DoctorPage(tk.Frame):
    txt = ""
    def __init__(self, parent, controller):
        self.db = MySQLDatabase("localhost", username="root")
        self.db.connection.autocommit = True
        tk.Frame.__init__(self, parent)

        def seeDetails():
            Table.lst = self.db.execute_query(f"select s.s_id,s.s_name,s.salary,s.joining,d.dep_name,s.address,s.`Ph.No.` from doctor join staff as s using(s_id) join departments as d using (dep_id) where  s_id = '{StaffLogin.ids}'")
            Table.lst.insert(0,('Staff ID','Staff Name','Salary','Date of Joining','Department', 'Address', 'Ph.No.'))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showApp = tk.Tk()
            t = Table(showApp)
            showApp.geometry("1000x600")
            showApp.mainloop()

        def changePhone():
            newPh = askstring("Change Phone No.", "Enter New Phone No.")
            if newPh=="" or not newPh.isdigit or len(newPh)!=10:
                MessageBox.showerror("Operation Failed", "Please Enter a valid No.")
                return
            MessageBox.showinfo("New Phone No.", f"Changed Number is {newPh}")
            self.db.execute_query(f"update staff set `Ph.No.` = '{newPh}' where s_id='{StaffLogin.ids}'")

        def changePass():
            s_id = StaffLogin.ids
            newpass = askstring("Change Password", "Enter New Password Here")
            if newpass =="":
                MessageBox.showerror("Operation Cancelled", "Operation wasn't completed")
                return
            MessageBox.showinfo("New Password", f"Changed Password is {newpass}")
            self.db.execute_query(f"update staff set `password` = '{newpass}' where s_id='{s_id}'")

        def upcomingAppoint():
            Table.lst = self.db.execute_query(f"select a_id,p_id,patient.p_name,date from appointment join patient using(p_id) where s_id = '{StaffLogin.ids}' and status ='diagnosis'")
            Table.lst.insert(0,('Appointment ID','Patient ID','Patient Name','Date of Appointment'))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showApp = tk.Tk()
            t = Table(showApp)
            showApp.geometry("1000x600")
            showApp.mainloop()

        def ongoingProcedure():
            Table.lst = self.db.execute_query(f"select a_id,p_id,patient.p_name,date,status from appointment join patient using(p_id) where s_id = '{StaffLogin.ids}' and (status ='procedure' or status='diagnosis')")
            Table.lst.insert(0,('Appointment ID','Patient ID','Patient Name','Date of Appointment','Status of Patient'))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showApp = tk.Tk()
            t = Table(showApp)
            showApp.geometry("1000x600")
            showApp.mainloop()

        def patientsByName():
            checkpat = askstring("Search by Name", "Enter Patient Name to be searched for")
            if checkpat=="":
                MessageBox.showerror("Operation Cancelled", "Operation wasn't completed")
                return
            Table.lst = self.db.execute_query(f"SELECT p_id, p_name, gender, address, `Ph.No.` from Patient where p_name LIKE '%{checkpat}%'")
            Table.lst.insert(0,('Patient ID','Patient Name','Gender', 'Address', 'Ph.No.'))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showApp = tk.Tk()
            t = Table(showApp)
            showApp.geometry("1000x600")
            showApp.mainloop()

        def patientByID():
            checkid = askstring("Search by Name", "Enter Patient ID to be searched for")
            if checkid=="":
                MessageBox.showerror("Operation Cancelled", "Operation wasn't completed")
                return
            Table.lst = self.db.execute_query(f"SELECT p_id, p_name, gender, address, `Ph.No.` from Patient where p_id = '{checkid}'")
            Table.lst.insert(0,('Patient ID','Patient Name','Gender', 'Address', 'Ph.No.'))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showApp = tk.Tk()
            t = Table(showApp)
            showApp.geometry("1000x600")
            showApp.mainloop()

        def setDiagnosis():
            procframe.pack_forget()
            diagframe.pack(padx=10,pady=10)

        def changeDiagnosis():
            aid = aidtt.get()
            diag = diatt.get("1.0",tk.END)
            med = meditt.get("1,0",tk.END)
            if aid=="":
                MessageBox.showerror("Update Fail", "Enter valid appointment id")
                return
            self.db.execute_query(f"update diagnosis join appointment using(a_id) set diagnosis = concat(diagnosis'\n',current_time, '{diag}'), medicine = concat(medicine'\n',current_time,'{med}') where a_id = {aid} and status='diagnosis'")
            aidtt.delete(0,tk.END)
            diatt.delete("1.0", tk.END)
            meditt.delete("1.0", tk.END)
            diagframe.pack_forget()
            if self.db.cursor.rowcount!=1:
                MessageBox.showerror("Update failed", "Enter appropriate appointment ID")

        def updateProc():
            diagframe.pack_forget()
            procframe.pack(padx=10,pady=10)

        def setProc():
            aid = aidtt1.get()
            if aid=="":
                MessageBox.showerror("Update Fail", "Enter valid appointment id")
                return
            det = dett.get("1.0", tk.END)
            self.db.execute_query(f"update procedure join appointment using(a_id) set details = concat(details,'\n',current_time, '{det}') where a_id = {aid} and status='procedure'")
            aidtt1.delete(0,tk.END)
            dett.delete("1.0", tk.END)
            procframe.pack_forget()
            if self.db.cursor.rowcount!=1:
                MessageBox.showerror("Update failed", "Enter appropriate appointment ID")

        def patientHistory():
            Table.lst = self.db.execute_query(f"select a.a_id,a.p_id,p.p_name,a.date from appointment as a join patient as p using(p_id) where s_id = '{StaffLogin.ids}'")
            Table.lst.insert(0,('Appointment ID','Patient ID','Patient Name','Appointment Date'))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showApp = tk.Tk()
            t = Table(showApp)
            showApp.geometry("1000x600")
            showApp.mainloop()

        DoctorPage.txt = f"Welcome Doctor {StaffLogin.ids}"
        titletext = tk.Label(master=self, text=DoctorPage.txt, font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

        button1 = tk.Button(master=logframe, text="Change Password", command=changePass).grid(padx=10, pady=10, row=0, column=0)
        button10 = tk.Button(master=logframe, text="Change Phone No.", command=changePhone).grid(padx=10, pady=10, row=0, column=1)
        button9 = tk.Button(master=logframe, text="Check Personal Details", command=seeDetails).grid(padx=10, pady=10, row = 0, column=2)

        button2 = tk.Button(master=logframe, text="Upcoming Appointment", command=upcomingAppoint).grid(padx=10, pady=10, row=1, column=0)
        button4 = tk.Button(master=logframe, text="Search Patients By Name", command=patientsByName).grid(padx=10, pady=10, row=1, column=1)
        button5 = tk.Button(master=logframe, text="Search Patients By ID", command=patientByID).grid(padx=10, pady=10, row=1, column=2)

        button3 = tk.Button(master=logframe, text="Ongoing Procedure", command=ongoingProcedure).grid(padx=10, pady=10, row=2, column=0)
        button8 = tk.Button(master=logframe, text="Update Diagnosis", command=setDiagnosis).grid(padx=10, pady=10, row=2, column=1)
        button12 = tk.Button(master=logframe, text="Update Procedure", command=updateProc).grid(padx=10,pady=10,row=2,column=2)

        button7 = tk.Button(master=logframe, text="Patient History", command=patientHistory).grid(padx=10, pady=10, row=3, column=0)
        button6 = tk.Button(master=logframe, text="Logout", command=lambda : controller.show_frame(StaffLogin)).grid(padx=10, pady=10, row=3, column=1)

        logframe.pack(padx=10, pady=20)

        diagframe = tk.Frame(self)

        lab1 = tk.Label(master=diagframe, text="Enter diagnosis").grid(padx=10,pady=10,row=0,column=0)
        lab2 = tk.Label(master=diagframe, text="Enter Medicine").grid(padx=10,pady=10,row=0,column=1)

        diatt = tk.Text(master=diagframe, height=8, width=10)
        diatt.grid(padx=10,pady=10,row=1,column=0)

        meditt = tk.Text(master=diagframe, height=8, width=10)
        meditt.grid(padx=10,pady=10,row=1,column=1)

        lab3 = tk.Label(master=diagframe, text="Enter Appointment ID").grid(padx=10,pady=10,row=2,column=0)
        aidtt = tk.Entry(master=diagframe)
        aidtt.grid(padx=10,pady=10, row=2,column=1)

        button11 = tk.Button(master=diagframe, text='Update Diagnosis', command=changeDiagnosis).grid(padx=10,pady=10,row=3,column=1)

        procframe = tk.Frame(self)

        lab4 = tk.Label(master=procframe, text="Enter Procedure details").grid(padx=10,pady=10,row=0,column=0)
        dett = tk.Text(master=procframe, height=8, width=10)
        dett.grid(padx=10,pady=10,row=0,column=1)

        lab5 = tk.Label(master=procframe, text="Enter Appointment ID").grid(padx=10,pady=10,row=1,column=0)
        aidtt1 = tk.Entry(master=procframe)
        aidtt1.grid(padx=10,pady=10, row=1,column=1)

        button13 = tk.Button(master=procframe, text="Update Details",command=setProc).grid(padx=10,pady=10,row=2,column=1)

class NursePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.db = MySQLDatabase("localhost", username="root")
        self.db.connection.autocommit = True

        def seeDetails():
            Table.lst = self.db.execute_query(f"select s.s_id,s.s_name,s.salary,n.seniority,s.joining,d.dep_name,s.address,s.`Ph.No.` from nurse as n join staff as s using(s_id) join departments as d using (dep_id) where  s_id = '{StaffLogin.ids}'")
            Table.lst.insert(0,('Staff ID','Staff Name','Salary','Seniority','Date of Joining','Department', 'Address', 'Ph.No.'))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showApp = tk.Tk()
            t = Table(showApp)
            showApp.geometry("1000x600")
            showApp.mainloop()

        def changePhone():
            newPh = askstring("Change Phone No.", "Enter New Phone No.")
            if newPh=="" or not newPh.isdigit or len(newPh)!=10:
                MessageBox.showerror("Operation Failed", "Please Enter a valid No.")
                return
            MessageBox.showinfo("New Phone No.", f"Changed Number is {newPh}")
            self.db.execute_query(f"update staff set `Ph.No.` = '{newPh}' where s_id='{StaffLogin.ids}'")

        def changePass():
            s_id = StaffLogin.ids
            newpass = askstring("Change Password", "Enter New Password Here")
            if newpass =="":
                MessageBox.showerror("Operation Cancelled", "Operation wasn't completed")
                return
            MessageBox.showinfo("New Password", f"Changed Password is {newpass}")
            self.db.execute_query(f"update staff set `password` = '{newpass}' where s_id='{s_id}'")

        def roomallot():
            Table.lst = self.db.execute_query(f"select r_no,r_type from room where nurse_1 = '{StaffLogin.ids}' or nurse_2='{StaffLogin.ids}'")
            Table.lst.insert(0,('Room No.', 'Room Type'))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showApp = tk.Tk()
            t = Table(showApp)
            showApp.geometry("600x600")
            showApp.mainloop()

        def patientAllot():
            Table.lst = self.db.execute_query(f"select a.a_id,r.r_no,r.r_type,p.p_id,p.p_name,p.gender from patient as p join appointment as a using(p_id) join `procedure` using(a_id) join room as r using(r_no) where r.nurse_1='{StaffLogin.ids}' or r.nurse_2='{StaffLogin.ids}'")
            Table.lst.insert(0,('Appointment ID','Room No.','Room Type','Patient ID','Patient Name','Patient Gender'))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showApp = tk.Tk()
            t = Table(showApp)
            showApp.geometry("1000x600")
            showApp.mainloop()

        def detailsPatient():
            apid = askstring("Appointment ID", "Enter Appointment ID to fetch relevant details")
            if apid=="":
                MessageBox.showerror("Operation Failed", "No ID entered")
                return
            Table.lst = self.db.execute_query(f"select a.a_id,a.p_id, ss.s_name,d.b_no,d.diagnosis,d.medicine,a.date,p.date,p.r_no,p.details from appointment as a join `procedure` as p using(a_id) join diagnosis as d using(a_id) join staff as ss using(s_id) where a_id = {apid}")
            Table.lst.insert(0,('Appointment ID','Patient ID','Doctor Name','Bill No.','Diagnosis', 'Medicine', 'Appointment Date', 'Patient Admit Date','Patient Room No.', 'Procedure Details'))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showApp = tk.Tk()
            t = Table(showApp)
            showApp.geometry("1000x600")
            showApp.mainloop()

        titletext = tk.Label(master=self, text="Welcome Nurse", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

        button1 = tk.Button(master=logframe, text="Change Password", command=changePass).grid(padx=10, pady=20, row=0, column=0)
        button2 = tk.Button(master=logframe, text="Change Phone No.", command=changePhone).grid(padx=10, pady=20, row=0, column=1)
        button3 = tk.Button(master=logframe, text="Check Personal Details", command=seeDetails).grid(padx=10, pady=20, row = 0, column=2)

        button4 = tk.Button(master=logframe, text="Check Alloted Room", command=roomallot).grid(padx=10, pady=10, row=1, column=0)
        button5 = tk.Button(master=logframe, text="Check Alloted Patient", command=patientAllot).grid(padx=10, pady=10, row =1, column=1)
        button6 = tk.Button(master=logframe, text="See Patient Details", command=detailsPatient).grid(padx=10, pady=10, row=1, column=2)

        button7 = tk.Button(master=logframe, text="Logout",command=lambda : controller.show_frame(StaffLogin)).grid(padx=10, pady=10, row=2, column=1)

        logframe.pack(padx=10,pady=10)

class NMSPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.db = MySQLDatabase("localhost", username="root")
        self.db.connection.autocommit = True

        def seeDetails():
            Table.lst = self.db.execute_query(f"select s.s_id,s.s_name,s.salary,s.joining,nm.duty_type,s.address,s.`Ph.No.` from `Non-Medical Staff` as nm join staff as s using(s_id) where  s_id = '{StaffLogin.ids}'")
            Table.lst.insert(0,('Staff ID','Staff Name','Salary','Date of Joining','Duty', 'Address', 'Ph.No.'))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showApp = tk.Tk()
            t = Table(showApp)
            showApp.geometry("1000x600")
            showApp.mainloop()

        def changePhone():
            newPh = askstring("Change Phone No.", "Enter New Phone No.")
            if newPh=="" or not newPh.isdigit or len(newPh)!=10:
                MessageBox.showerror("Operation Failed", "Please Enter a valid No.")
                return
            MessageBox.showinfo("New Phone No.", f"Changed Number is {newPh}")
            self.db.execute_query(f"update staff set `Ph.No.` = '{newPh}' where s_id='{StaffLogin.ids}'")

        def changePass():
            s_id = StaffLogin.ids
            newpass = askstring("Change Password", "Enter New Password Here")
            if newpass =="":
                MessageBox.showerror("Operation Cancelled", "Operation wasn't completed")
                return
            MessageBox.showinfo("New Password", f"Changed Password is {newpass}")
            self.db.execute_query(f"update staff set `password` = '{newpass}' where s_id='{s_id}'")

        def unassignPat():
            Table.lst = self.db.execute_query(f"select a.a_id,a.p_id,a.date,d.b_no,d.diagnosis,d.medicine,p.date,p.r_no,p.date_discharge,p.details from appointment as a join `procedure` as p using(a_id) join diagnosis as d using(a_id) where a.status = 'procedure' and p.r_no=null")
            Table.lst.insert(0,('Appointment ID','Patient ID','Appointment Date','Bill No.','Diagnosis', 'Medicine', 'Procedure Date','Room No.','Procedure Date Discharge','Procedure details'))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showApp = tk.Tk()
            t = Table(showApp)
            showApp.geometry("1600x600")
            showApp.mainloop()

        def patAssign():
            roomframe.pack(padx=10,pady=10)

        def comAssign():
            aid = aidtt.get()
            room = roomlist.get(roomlist.curselection())
            room = str(room).split()[0]
            nur1 = nurlist.get(nurlist.curselection())
            nur2 = nurlist1.get(nurlist1.curselection())
            lst1=self.db.execute_query(f"select a.a_id from appointment as a join `procedure` as p using(a_id) join diagnosis as d using(a_id) where a.status = 'procedure' and p.r_no=null")
            lst1 = list(lst1)
            if aid == "" or aid not in lst1:
                MessageBox.showerror("Operation Pause", "Enter Appropriate Appointment ID")
                return
            elif not room.isdigit():
                MessageBox.showerror("Operation Pause", "Select a Room if available")
                return
            elif nur1 == nur2:
                MessageBox.showerror("Operation Pause", "Please select nurse appropriately")
                return
            self.db.execute_query(f"update `procedure` set r_no={room} where a_id = {aid}")
            if self.db.cursor.rowcount !=1:
                MessageBox.showerror("Operation Cancelled", "Wrong Appointment ID")
                aidtt.delete(0,tk.END)
                return
            self.db.execute_query(f"update room nurse_1=if('{nur1}'='None',null,'{nur1}'),nurse_2=if('{nur2}'='None',null,'{nur2}'), status='Occupied' where r_no={room}")
            roomframe.grid_forget()

        titletext = tk.Label(master=self, text="Welcome ", font=("Arial bold", 18))
        titletext.pack(pady=20)
        titletext.config(text = f'Welcome')
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

        button1 = tk.Button(master=logframe, text="Change Password", command=changePass).grid(padx=10, pady=20, row=0, column=0)
        button2 = tk.Button(master=logframe, text="Change Phone No.", command=changePhone).grid(padx=10, pady=20, row=0, column=1)
        button3 = tk.Button(master=logframe, text="Check Personal Details", command=seeDetails).grid(padx=10, pady=20, row = 0, column=2)

        button4 = tk.Button(master=logframe, text="Show Unassigned patients", command=unassignPat).grid(padx=10,pady=10, row=1, column=0)
        button5 = tk.Button(master=logframe, text="Assign Free Room", command=patAssign).grid(padx=10,pady=10, row=1, column=1)
        button6 = tk.Button(master=logframe, text="Logout", command=lambda : controller.show_frame(StaffLogin)).grid(padx=10, pady=10, row= 1, column=2)

        logframe.pack(padx=10,pady=10)

        roomframe = tk.Frame(master=self)

        label1 = tk.Label(master=roomframe, text="Enter Appointment ID").grid(padx=10, pady=10, row=0, column=0)
        aidtt = tk.Entry(master=roomframe)
        aidtt.grid(padx=10,pady=10, row=0, column=1)

        roomlab = tk.Label(master=roomframe, text="Appoint room").grid(padx=10,pady=10,row=0,column=2)
        roomlist = tk.Listbox(master=roomframe, height=4, exportselection=False)
        resultroom = self.db.execute_query(f"select r_no, r_type from room where status='free'")
        resultroom = list(resultroom)
        roomlist.insert(tk.END,'Room No.    Type')
        for i in resultroom:
            text = str(i[0]) + "                    " +i[1]
            roomlist.insert(tk.END, text)
        roomlist.select_set(0)
        roomlist.grid(padx=10,pady=10,row=0,column=3)
        
        nurlab = tk.Label(master=roomframe, text="Appoint Nurse").grid(padx=10,pady=10, row=1, column=0)
        nurlist = tk.Listbox(master=roomframe, height=8, exportselection=False)
        result = self.db.execute_query("Select s_id from nurse")
        result = list(result)
        result[0]= 'None'
        for i in result:
            nurlist.insert(tk.END, i)
        nurlist.select_set(0)
        nurlist.grid(padx=10,pady=10, row=1, column=1)

        nurlist1 = tk.Listbox(master=roomframe, height=8, exportselection=False)
        for i in result:
            nurlist1.insert(tk.END, i)
        nurlist1.select_set(0)
        nurlist1.grid(padx=10,pady=10, row=1, column=3)

        button7 = tk.Button(master=roomframe, text="Assign Room", command=comAssign).grid(padx=10,pady=10,row=2,column=2)


class forgotPID(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.db = MySQLDatabase("localhost", "root")
        self.db.connection.autocommit = True

        def getdat():
            name = nmtt.get()
            nmtt.delete(0,tk.END)
            Table.lst = self.db.execute_query(f"select p.p_id,p.p_name,p.gender,p.address,p.`Ph.No.` from patient as p where p.p_name LIKE '%{name}%'")
            Table.lst.insert(0,('Patient ID','Patient Name','Gender','Address','Ph.No.'))
            Table.total_columns = len(Table.lst[0])
            Table.total_rows = len(Table.lst)
            showApp = tk.Tk()
            t = Table(showApp)
            showApp.geometry("1000x600")
            showApp.mainloop()
            controller.show_frame(PatientLogin)

        titletext = tk.Label(master=self, text="Forgot p_id, Enter name", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)

        lab1 = tk.Label(master=logframe, text="Enter name").grid(padx=10, pady= 20, row=0, column=0)
        nmtt = tk.Entry(master=logframe)
        nmtt.grid(padx=10, pady=20, row=0, column=1)
        button1 = tk.Button(master=logframe, text="Find!", command=getdat).grid(pady=20, row=2, column=1)

        logframe.pack(padx=10, pady=20)
        button1 = ttk.Button(self, text ="Patient Login", command = lambda : controller.show_frame(PatientLogin))
        # putting the button in its place by
        # using grid
        button1.pack(padx = 10, pady = 10)

class forgotPassPat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.db = MySQLDatabase("localhost", "root")
        self.db.connection.autocommit = True

        def getdat():
            name = nmtt.get()
            phnum = phtt.get()
            s_id = name
            newpass = askstring("Change Password", "Enter New Password Here")
            if newpass =="":
                MessageBox.showerror("Operation Cancelled", "Operation wasn't completed")
                return
            self.db.execute_query(f"update patient set `password` = '{newpass}' where s_id='{s_id}' and `Ph.No.`={phnum}")
            nmtt.delete(0,tk.END)
            phtt.delete(0,tk.END)
            if self.db.cursor.rowcount == 1:
                MessageBox.showinfo("New Password", f"Changed Password is {newpass}")
                controller.show_frame(PatientLogin)
                return
            else:
                MessageBox.showerror("Operation Cancelled", "Operation wasn't completed")
                controller.show_frame(PatientLogin)
                return

        titletext = tk.Label(master=self, text="Forgot password, Enter ID", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)

        lab1 = tk.Label(master=logframe, text="Enter ID").grid(padx=10, pady= 20, row=0, column=0)
        nmtt = tk.Entry(master=logframe)
        nmtt.grid(padx=10, pady=20, row=0, column=1)

        lab2 = tk.Label(master=logframe, text="Enter Ph.No.").grid(padx=10, pady= 20, row=1, column=0)
        phtt = tk.Entry(master=logframe)
        phtt.grid(padx=10, pady= 20, row=1, column=1)

        button1 = tk.Button(master=logframe, text="Change Password", command=getdat).grid(pady=20, row=2, column=1)
        logframe.pack(padx=10, pady=20)
        button1 = ttk.Button(self, text ="Patient Login", command = lambda : controller.show_frame(PatientLogin))
        # putting the button in its place by
        # using grid
        button1.pack(padx = 10, pady = 10)

class forgotPassStf(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.db = MySQLDatabase("localhost", "root")
        self.db.connection.autocommit = True

        def getdat():
            name = nmtt.get()
            phnum = phtt.get()
            s_id = name
            newpass = askstring("Change Password", "Enter New Password Here")
            if newpass =="":
                MessageBox.showerror("Operation Cancelled", "Operation wasn't completed")
                return
            self.db.execute_query(f"update staff set `password` = '{newpass}' where s_id='{s_id}' and `Ph.No.`={phnum}")
            nmtt.delete(0,tk.END)
            phtt.delete(0,tk.END)
            if self.db.cursor.rowcount == 1:
                MessageBox.showinfo("New Password", f"Changed Password is {newpass}")
                controller.show_frame(StaffLogin)
                return
            else:
                MessageBox.showerror("Operation Cancelled", "Operation wasn't completed")
                controller.show_frame(StaffLogin)
                return

        titletext = tk.Label(master=self, text="Forgot password, Enter ID", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)

        lab1 = tk.Label(master=logframe, text="Enter ID").grid(padx=10, pady= 20, row=0, column=0)
        nmtt = tk.Entry(master=logframe)
        nmtt.grid(padx=10, pady=20, row=0, column=1)

        lab2 = tk.Label(master=logframe, text="Enter Ph.No.").grid(padx=10, pady= 20, row=1, column=0)
        phtt = tk.Entry(master=logframe)
        phtt.grid(padx=10, pady= 20, row=1, column=1)

        button1 = tk.Button(master=logframe, text="Change Password", command=getdat).grid(pady=20, row=2, column=1)
        logframe.pack(padx=10, pady=20)
        button1 = ttk.Button(self, text ="Staff Login", command = lambda : controller.show_frame(StaffLogin))
        # putting the button in its place by
        # using grid
        button1.pack(padx = 10, pady = 10)

def main():
    app = tkinterApp()
    app.mainloop()

if __name__ == "__main__":
    main()

