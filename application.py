import tkinter as tk
from tkinter import ttk
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
    def __init__(self, host, username, password, database):
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
        for F in (StaffLogin, PatientLogin, PatientRegistration, AdminPage, PatientPage, DoctorPage, NursePage, NMSPage):

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
        self.db = MySQLDatabase("localhost", "root", "00000000", "Hospital")
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

class PatientLogin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def getdat():
            ids = idtt.get()
            idtt.delete(0, tk.END)
            passw = patt.get()
            patt.delete(0, tk.END)
            if ids == "" or passw == "":
                MessageBox.showwarning("Login Status", "All Field are Required!!!")
            else:
                controller.show_frame(PatientPage)
                pass


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

class PatientRegistration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def getdat():
            name = nmtt.get()
            gndr = gntt.get(gntt.curselection())
            phnum = phtt.get()
            adr = adtt.get()
            pwd1 = passwordtt.get()
            pwd2 = passrett.get()
            if name == "" or phnum == "" or adr=="" or pwd1=="" or pwd2=="":
                MessageBox.showwarning("Registration Status", "All Field are Required!!!")
            else:
                if not phnum.isdigit() or len(phnum)!=10:
                    MessageBox.showerror("Registration Status", "Enter Valid Phone No.")
                    phtt.delete(0,tk.END)
                elif pwd2!=pwd1:
                    MessageBox.showerror("Registration Status", "Passwords don't match")
                    passwordtt.delete(0, tk.END)
                    passrett.delete(0, tk.END)
                elif gndr == "None":
                    MessageBox.showerror("Registration Status", "Please Select Your Gender")
                elif gndr == "Others":
                    gndr = askstring("Gender", "What is your gender?")
                    MessageBox.showinfo("Patient Gender", "Gender {} registered succesfully".format(gndr))
                pass
        
        titletext = tk.Label(master=self, text="Patient Registration", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

        nm = tk.Label(master = logframe, text="Full Name").grid(row = 0, column = 0, sticky=tk.W+tk.E)
        nmtt = tk.Entry(master = logframe)
        nmtt.grid(pady=10, padx=20, row = 0, column = 1, sticky=tk.W+tk.E)

        gnd = tk.Label(master=logframe, text="Gender").grid(row=1,column=0,sticky=tk.W+tk.E)

        gntt = tk.Listbox(master=logframe)
        gntt.insert(1, "None")
        gntt.insert(2, "Male")
        gntt.insert(3, "Female")
        gntt.insert(4, "Transgender")
        gntt.insert(5, "Non-Binary")
        gntt.insert(6, "Intersex")
        gntt.insert(7, "Others")
        gntt.select_set(0)
        gntt.grid(pady=10, padx=20, row=1, column=1, sticky=tk.E+tk.W)

        phno = tk.Label(master = logframe, text="Phone No.").grid(row = 2, column = 0, sticky=tk.W+tk.E)
        phtt = tk.Entry(master = logframe)
        phtt.grid(pady=10, padx=20, row = 2, column = 1, sticky=tk.W+tk.E)

        add = tk.Label(master=logframe, text = "Address").grid(row = 3, column = 0, sticky=tk.W+tk.E)
        adtt = tk.Entry(master = logframe)
        adtt.grid(pady=10, padx=20, row = 3, column = 1, sticky=tk.W+tk.E)

        password = tk.Label(master=logframe, text="Password").grid(padx=20, row= 4, column=0, sticky=tk.E+tk.W)
        passwordtt = tk.Entry(master=logframe, show="*")
        passwordtt.grid(pady=10, padx=20, row=4, column=1, sticky=tk.E+tk.W)

        passret = tk.Label(master=logframe, text="Re-Enter Password").grid(padx=20, row = 5, column=0, sticky= tk.E+tk.W)
        passrett = tk.Entry(master=logframe,show="*")
        passrett.grid(pady=10, padx=20, row=5, column=1, sticky=tk.E+tk.W)

        logframe.pack(pady = 20, fill='x')

        button = tk.Button(master=self, command=getdat, text="Login")
        button.pack(padx = 100,pady = 20)

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
        self.db = MySQLDatabase("localhost", "root", "00000000", "Hospital")
        self.db.connection.autocommit = True
        def changePass():
            newpass = askstring("Change Password", "Enter New Password Here")
            if newpass =="":
                return
            MessageBox.showinfo("New Password", f"Changed Password is {newpass}")
            self.db.execute_query(f"update staff set `password` = '{newpass}' where s_id='DOC0000'")
        
        def addStaff():
            stafframe.pack(padx=10,pady=10)

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

        titletext = tk.Label(master=self, text="Welcome Admin", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

        button1 = tk.Button(master=logframe, text="Change Password", command=changePass).grid(padx=10, pady=10, row=0, column=0)

        button2 = tk.Button(master=logframe, text="Add Staff", command=addStaff).grid(padx=10, pady=10, row=0, column=1)

        button3 = tk.Button(master=logframe, text="Observe Staff", command=showStaff).grid(padx=10, pady=10, row=0, column=2)

        button4 = tk.Button(master=logframe, text="Observe Patients", command=showPatient).grid(padx=10, pady=10, row=1, column=0)

        button5 = tk.Button(master=logframe, text="Change Salary", command=changeSalary).grid(padx=10, pady=10, row=1, column=1)

        button6 = tk.Button(master=logframe,text="LogOut", command = lambda : controller.show_frame(StaffLogin)).grid(padx=10, pady=20, row=1, column=2)

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
        saltt.grid(padx=10, row=4, column=1)

        button7 = tk.Button(master=stafframe, text="Add Staff", command=getdat).grid(pady=10, row=5, column=2, sticky=tk.E+tk.W)

        

class PatientPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        titletext = tk.Label(master=self, text="Welcome Back", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

        def showDetails():
            pass

        def changePass():
            pass

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
        self.db = MySQLDatabase("localhost", "root", "00000000", "Hospital")
        self.db.connection.autocommit = True
        tk.Frame.__init__(self, parent)
        def changePass():
            s_id = StaffLogin.ids
            newpass = askstring("Change Password", "Enter New Password Here")
            if newpass =="":
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
            pass

        def patientsByName():
            pass

        def patientByID():
            DoctorPage.txt = f"Welcome Doctor {StaffLogin.ids}"
            print(DoctorPage.txt)
            pass

        def patientHistory():
            pass

        DoctorPage.txt = f"Welcome Doctor {StaffLogin.ids}"
        titletext = tk.Label(master=self, text=DoctorPage.txt, font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

        button1 = tk.Button(master=logframe, text="Change Password", command=changePass).grid(padx=10, pady=20, row=0, column=0)
        button2 = tk.Button(master=logframe, text="Upcoming Appointment", command=upcomingAppoint).grid(padx=10, pady=20, row=0, column=1)
        button3 = tk.Button(master=logframe, text="Ongoing Procedure", command=ongoingProcedure).grid(padx=10, pady=20, row=0, column=2)

        label1 = tk.Label(master=logframe, text="Search Patients: ").grid(padx=10, pady=20, row=1, column=0)
        button4 = tk.Button(master=logframe, text="By Name", command=patientsByName).grid(padx=10, pady=20, row=1, column=1)
        button5 = tk.Button(master=logframe, text="By ID", command=patientByID).grid(padx=10, pady=20, row=1, column=2)

        button7 = tk.Button(master=logframe, text="Patient History", command=patientHistory).grid(padx=10, pady=20, row=2, column=0)
        button8 = tk.Button(master=logframe, text="Change Appointment Date").grid(padx=10, pady=20, row=2, column=1)

        button6 = tk.Button(master=logframe, text="Logout", command=lambda : controller.show_frame(StaffLogin)).grid(padx=10, pady=20, row=4, column=1)

        logframe.pack(padx=10, pady=20)

class NursePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        titletext = tk.Label(master=self, text="Welcome {name}", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

class NMSPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        titletext = tk.Label(master=self, text="Welcome {name}", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

def main():
    app = tkinterApp()
    app.mainloop()

if __name__ == "__main__":
    main()

