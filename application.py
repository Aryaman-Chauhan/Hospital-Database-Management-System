import tkinter as tk
from tkinter import ttk
from tkinter.simpledialog import askstring
import tkinter.messagebox as MessageBox
import mysql.connector

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
        for F in (StaffLogin, PatientLogin, PatientRegistration, AdminPage, PatientPage, DoctorPage, NursePage):

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
        tk.Frame.__init__(self, parent)
        def getdat():
            StaffLogin.ids = idtt.get()
            idtt.delete(0, tk.END)
            StaffLogin.passw = patt.get()
            patt.delete(0, tk.END)
            if StaffLogin.ids == "" or StaffLogin.passw == "":
                MessageBox.showwarning("Login Status", "All Field are Required!!!")
            else:
                if StaffLogin.ids == "DOC0000" and StaffLogin.passw == "0000":
                    controller.show_frame(DoctorPage)

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
                pass


        titletext = tk.Label(master=self, text="Patient Login", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

        idss = tk.Label(master = logframe, text="Enter your ID")
        idss.grid(row = 0, column = 0, sticky=tk.W+tk.E)

        idtt = tk.Entry(master = logframe)
        idtt.grid(padx=20, row = 0, column = 1, sticky=tk.W+tk.E)

        passw = tk.Label(master = logframe, text="Enter Password")
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
            if name == "" or phnum == "" or adr=="":
                MessageBox.showwarning("Registration Status", "All Field are Required!!!")
            else:
                if not phnum.isdigit() or len(phnum)!=10:
                    MessageBox.showerror("Registration Status", "Enter Valid Phone No.")
                    phtt.delete(0,tk.END)
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

        nm = tk.Label(master = logframe, text="Full Name")
        nm.grid(row = 0, column = 0, sticky=tk.W+tk.E)

        nmtt = tk.Entry(master = logframe)
        nmtt.grid(padx=20, row = 0, column = 1, sticky=tk.W+tk.E)

        gnd = tk.Label(master=logframe, text="Gender")
        gnd.grid(row=1,column=0,sticky=tk.W+tk.E)

        gntt = tk.Listbox(master=logframe)
        gntt.insert(1, "None")
        gntt.insert(2, "Male")
        gntt.insert(3, "Female")
        gntt.insert(4, "Transgender")
        gntt.insert(5, "Non-Binary")
        gntt.insert(6, "Intersex")
        gntt.insert(7, "Others")
        gntt.select_set(0)
        gntt.grid(padx=20, row=1, column=1, sticky=tk.E+tk.W)

        phno = tk.Label(master = logframe, text="Phone No.")
        phno.grid(row = 2, column = 0, sticky=tk.W+tk.E)

        phtt = tk.Entry(master = logframe)
        phtt.grid(padx=20, row = 2, column = 1, sticky=tk.W+tk.E)

        add = tk.Label(master=logframe, text = "Address")
        add.grid(row = 3, column = 0, sticky=tk.W+tk.E)

        adtt = tk.Entry(master = logframe)
        adtt.grid(padx=20, row = 3, column = 1, sticky=tk.W+tk.E)

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
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def changePass():
            print(StaffLogin.ids, StaffLogin.passw)
            pass
        
        def addStaff():
            pass

        def showStaff():
            pass

        def showPatient():
            pass

        def changeSalary():
            pass

        titletext = tk.Label(master=self, text="Welcome Admin", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

        button1 = tk.Button(master=logframe, text="Change Password", command=changePass).grid(padx=10, pady=20, row=0, column=0)

        button2 = tk.Button(master=logframe, text="Add Staff", command=addStaff).grid(padx=10, pady=20, row=0, column=1)

        button3 = tk.Button(master=logframe, text="Observe Staff", command=showStaff).grid(padx=10, pady=20, row=0, column=2)

        button4 = tk.Button(master=logframe, text="Observe Patients", command=showPatient).grid(padx=10, pady=20, row=1, column=0)

        button5 = tk.Button(master=logframe, text="Change Salary", command=changeSalary).grid(padx=10, pady=20, row=1, column=1)

        button6 = tk.Button(master=logframe,text="LogOut", command = lambda : controller.show_frame(StaffLogin)).grid(padx=10, pady=20, row=1, column=2)

        logframe.pack(padx=20, pady=20)

class PatientPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        titletext = tk.Label(master=self, text="Welcome Back {name}", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

class DoctorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        def changePass():
            pass

        def upcomingAppoint():
            pass

        def ongoingProcedure():
            pass

        def patientsByName():
            pass

        def patientByID():
            pass

        def patientHistory():
            pass

        def txtGet():
            return f'Welcome Doctor {StaffLogin.ids}'

        titletext = tk.Label(master=self, text=txtGet(), font=("Arial bold", 18)).pack(pady=20)
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

class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        titletext = tk.Label(master=self, text="Welcome {name}", font=("Arial bold", 18)).pack(pady=20)
        logframe = tk.Frame(master=self)
        logframe.columnconfigure(0, weight=1)
        logframe.columnconfigure(1, weight=1)

def main():
    print("Hello World!")
    app = tkinterApp()
    app.mainloop()

if __name__ == "__main__":
    main()

