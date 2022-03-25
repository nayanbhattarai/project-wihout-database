from tkinter import *
import tkinter.messagebox
import os

class EmployeeManagementSystem(Tk):
    """This is the heart of my app main class known as parent class"""
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Employee management system")
        self.geometry("1000x500+0+0")
        self.minsize(500,300)

        container =Frame(self)
        container.pack(side='top', fill='both', expand=True)
        # container.grid(row=0,column=0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # creating frame
        self.frames = {}

        for F in (StartPage, Login, Register,AddEmpPage,SearchPage,RegisterEmployee,RemovePage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, context):
        frame = self.frames[context]
        frame.tkraise()


class StartPage(Frame):
    """Start Page is the first page of our app which where login and register btn are located"""
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
         #label of the application window
        self.heading= Label(self, text="Welcome to Start Page", font=('Arial 40 bold'), fg='black', bg='lightgreen')
        self.heading.pack()


        #buttons
        Login_btn = Button(self,text="Login", width=30,height=2,bg='green',fg='white',font=('Arial 15 bold'),command=lambda:controller.show_frame(Login))
        Login_btn.pack_configure()
        Register_btn = Button(self,text="Register", width=30,height=2,bg='green',fg='white',font=('Arial 15 bold'),command=lambda:controller.show_frame(Register))
        Register_btn.pack(padx=10,pady=10)

class Register(Frame):
    """This calss and method is used to registered the admin users only"""
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller=controller

        self.heading = Label(self, text="Welcome to Registration Page", font=('Arial 40 bold'), fg='black',
                                 bg='lightgreen')
        self.heading.pack()


        fullname_label = Label(self, text="Username *")
        fullname_label.pack()
        self.fullname_val = Entry(self, width=50)
        self.fullname_val.pack()

        password1_label = Label(self, text='Password *')
        password1_label.pack()
        self.password1_val = Entry(self, width=50, show="*")
        self.password1_val.pack()

        password2_label = Label(self, text='Confirm Password *')
        password2_label.pack()
        self.password2_val = Entry(self, width=50, show="*")
        self.password2_val.pack()

        Homepage_btn = Button(self, text="Start Page", command=lambda: controller.show_frame(StartPage))
        Homepage_btn.pack()

        Register_btn = Button(self, text="Submit",command=self.user_register)
        Register_btn.pack()
    def user_register(self):
        """This method is used to get User Data"""
        self.val3 = self.fullname_val.get()
        self.val4 = self.password1_val.get()
        self.val5= self.password2_val.get()

        if self.val3 == '' or self.val4 == '' or self.val4=='': # checking if the user input is empty
            tkinter.messagebox.showwarning("Warning", "Please Fill Up All Boxes")
        elif self.val4 != self.val5:
            tkinter.messagebox.showwarning("Warning", "Both password did not match")

        elif len(self.val4) < 6 or len(self.val3)<6:
            tkinter.messagebox.showwarning("Warning", "Please enter six digit password/username")
            self.password1_val.delete(0, END)
            self.password2_val.delete(0, END)
        elif self.val3.isdigit():
            tkinter.messagebox.showwarning("Warning", "username can't be number only !")
            self.val3.delete(0, END)
        elif self.val4.isdigit():
            tkinter.messagebox.showwarning("Warning", "Password  can't be number only !")
            self.val4.delete(0, END)



        else:# saving into file
            file = open('loginverify.txt', 'a')
            file.write(self.val3 + ';' + self.val4)
            file.write("\n")
            file.close()
            tkinter.messagebox.showinfo('Information', "Registered Successfully")
            self.controller.show_frame(StartPage)

class Login(Frame):
    """This is the login page of our system """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller=controller

        # label of the application window
        self.heading = Label(self, text="Welcome to Login Page", font=('Arial 40 bold'), fg='black',
                                 bg='lightgreen')
        self.heading.pack()

        label_username = Label(self, text='Username or Email *')
        label_username.pack()
        self.user_name_value = Entry(self, width=50)
        self.user_name_value.pack()

        label_pass = Label(self, text='Password *')
        label_pass.pack()
        self.pass_val = Entry(self, width=50, show="*")
        self.pass_val.pack()

        Homepage_btn = Button(self, text="Start Page", command=lambda: controller.show_frame(StartPage))
        Homepage_btn.pack()

        Login_btn = Button(self, text="Login",command=self.user_auth)
        Login_btn.pack()


    def user_auth(self):
        """This method helps to identify the valid user and their credentials """
        val1 = self.user_name_value.get()
        val2 = self.pass_val.get()
        data = val1 + ';' + val2 + "\n"
        fr = open('loginverify.txt', 'r')
        line = fr.readlines()
        if data in line:
            tkinter.messagebox.showinfo('Information', "Login successful")
            self.controller.show_frame(AddEmpPage)

            #record_form()
        else:
            tkinter.messagebox.showerror('Error', 'Invalid Username or Password/ Fill the Blanks')
            self.user_name_value.delete(0, END)
            self.pass_val.delete(0, END)

        fr.close()
class AddEmpPage(Frame):
    """This is out heart of our app which allows the admin user to add, remove, delete, search the employee add department and so on"""
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.heading= Label(self, text="Employee and Department", font=('Arial 40 bold'), fg='black', bg='lightgreen')
        self.heading.pack(pady=10)

        self.search_frame = Frame(self)
        self.search_frame.pack()
        searchEmp_btn = Button(self.search_frame,text="Search Employee", width=25,height=1,bg='green',fg='white',font=('Arial 15 bold'),command=lambda:controller.show_frame(SearchPage))
        searchEmp_btn.pack_configure(pady=10)
        searchEmp_btn = Button(self.search_frame,text="Add employee", width=25,height=1,bg='green',fg='white',font=('Arial 15 bold'),command=lambda:controller.show_frame(RegisterEmployee))
        searchEmp_btn.pack_configure(pady=10)
        searchEmp_btn = Button(self.search_frame,text="Delete Employee", width=25,height=1,bg='green',fg='white',font=('Arial 15 bold'),command=lambda:controller.show_frame(RemovePage))
        searchEmp_btn.pack_configure(pady=10)

        searchEmp_btn = Button(self.search_frame,text="Department Options", width=25,height=1,bg='green',fg='white',font=('Arial 15 bold'),
                               command=lambda:(a.withdraw(),self.Department_form()))
        searchEmp_btn.pack_configure(pady=10)
        searchEmp_btn = Button(self.search_frame, text="Exit", width=25, height=1, bg='green', fg='white',
                               font=('Arial 15 bold'),
                               command=lambda:a.destroy())
        searchEmp_btn.pack_configure(pady=10)

    def Department_form(self):
        """This method helps to add the new department by the admin users"""
        top3 = Toplevel()
        top3.title("Add Department")
        top3.geometry("1000x500+0+0")
        top3.minsize(500, 300)

        l1 = Label(top3, text="Department Name")
        l1.pack()
        self.depn_name = Entry(top3,width=25)
        self.depn_name.pack()
        btn = Button(top3,text="Add Department", width=15,bg='green',fg='white',font=('Arial 10 bold'),command=self.department_add)
        btn.pack(pady=10)

        btn = Button(top3,text="Available Department", width=19,bg='green',fg='white',font=('Arial 10 bold'),command=self.show_departments)
        btn.pack(pady=20)
        searchEmp_btn = Button(top3, text="Back To DashBoard", width=25, height=1, bg='green', fg='white',
                               font=('Arial 15 bold'),
                               command=lambda: (a.deiconify(),top3.destroy()))
        searchEmp_btn.pack_configure(pady=10)
    def department_add(self):
        """This is aslo the method to add the departments """
        daname = self.depn_name.get()
        if daname == '':
            tkinter.messagebox.showwarning("Warning", "Please Fill Up All Information")
        else:
            file = open('availabledepartment.txt', 'a')
            file.write(daname.upper())
            file.write('\n')
            file.close()
            tkinter.messagebox.showinfo("Information", "Department registered Successfully")
    def show_departments(self):
        """This is the method which shows the registered Departments in our system"""
        files = os.listdir()
        if 'availabledepartment.txt' in files:
            file = open('availabledepartment.txt', 'r')
            line = file.read()
            file.close()
            tkinter.messagebox.showinfo("Available Departments ", line)
        else:
            tkinter.messagebox.showerror('Error', 'Currently No Department Available')
class RegisterEmployee(Frame):
    """This is class is used to add the employee by the admins users """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

         #label of the application window
        self.heading= Label(self, text="Welcome to Employee Registration Page", font=('Arial 40 bold'), fg='black', bg='lightgreen')
        self.heading.pack()


        fullname_label = Label(self,text="Full Name *")
        fullname_label.pack()
        self.fullname_val = Entry(self,width=50)
        self.fullname_val.pack()

        email_label = Label(self,text='Email *')
        email_label.pack()
        self.email_val = Entry(self,width=50)
        self.email_val.pack()

        address_label = Label(self,text='Address *')
        address_label.pack()
        self.address_val = Entry(self,width=50)
        self.address_val.pack()

        age_label = Label(self, text='Age *')
        age_label.pack()
        self.age_val = Entry(self,width=50)
        self.age_val.pack()

        contact_label = Label(self,text='Contact *')
        contact_label.pack()
        self.contact_val = Entry(self,width=50)
        self.contact_val.pack()


        department_label = Label(self, text="Department *")
        department_label.pack()
        self.drop = Entry(self,width=50)
        self.drop.pack()

        Register_btn = Button(self,text="Submit",command=self.add_employee)
        Register_btn.pack()
        Clear_btn=Button(self,text="Clear",command=self.clear_field)
        Clear_btn.pack()
        Homepage_btn = Button(self,text="Return To Dashboard",bg='green',fg='white',font=('Arial 10 bold'),command=lambda:controller.show_frame(AddEmpPage))
        Homepage_btn.pack()
    def clear_field(self):

        self.fullname_val=self.fullname_val.delete(0,END)
        self.email_val=self.email_val.delete(0,END)
        self.address_val=self.address_val.delete(0,END)
        self.age_val=self.age_val.delete(0,END)
        self.contact_val=self.contact_val.delete(0,END)
        self.drop=self.drop.delete(0, END)
    def add_employee(self):
        """This method helps to gatherd the registered employee details """
        name = self.fullname_val.get()
        name = name.lower()
        email = self.email_val.get()
        email = email.lower()
        dept = self.drop.get()
        dept = dept.lower()
        address=self.address_val.get()
        address=address.lower()
        age = self.age_val.get()
        contact = self.contact_val.get()
        while True:
            if name == '' or email == '' or dept == '' or age == '' or contact == '':
                tkinter.messagebox.showwarning("Warning", "Please Fill Up All Information")
                break

            elif  len(age) < 1 or len(contact) < 10:
                tkinter.messagebox.showwarning("Warning", "Invalid age or phone number")
                break
            try:
                int(age) and int(contact)
            except ValueError:
                tkinter.messagebox.showwarning("Warning", "Contact and age can only be digit")
                break

            else:
                file = open(name + '.txt', 'a')
                file.write(name + ';' + email + ';' + dept + ';' + age +  ';'+ address + ';' + contact)
                file.close()
                tkinter.messagebox.showinfo("Information", "Employee registered Successfully")
                break
class SearchPage(Frame):
    """This class helps us to find the users by their full name """
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
         #label of the application window
        self.heading= Label(self, text="Welcome to Search Page", font=('Arial 40 bold'), fg='black', bg='lightgreen')
        self.heading.pack(padx=10,pady=10)

        self.search_frame = Frame(self,width=300,height=500)

        self.l1 = Label(self.search_frame,text="Enter Full Name *")
        self.l1.pack(side='left')
        self.search_val = Entry(self.search_frame,width=30)
        self.search_val.pack(side='left',padx=10,pady=10)



        search_btn  = Button(self.search_frame,width=20, text='Search',  command=self.Employee_search)
        search_btn.pack(side='left')
        res_frame = Frame(self.search_frame,bg="green")
        res_frame.pack()


        dash_btn = Button(self.search_frame,text="Return To dashboard",bg='green',fg='white',font=('Arial 10 bold'),command=lambda:controller.show_frame(AddEmpPage))
        dash_btn.pack(side='left')
        self.search_frame.pack()
    def Employee_search(self):
        """This is the method which helps to search the employee by the name"""
        sname = self.search_val.get()
        sname = sname.lower()
        sdata_file= sname + '.txt'
        files=os.listdir()
        if sdata_file in files:
            file = open(sdata_file , 'r')
            line = file.readline()
            string=line.strip()
            userinfo=string.split(';')
            name=userinfo[0]
            email=userinfo[1]
            department=userinfo[2]
            ageinf=userinfo[3]
            adrrs=userinfo[4]
            phone=userinfo[5]
            print(string)
            file.close()
            tkinter.messagebox.showinfo("Information :", 'Name:'+name.upper()+'\n'+'Email:'+email.upper()+'\n'+'Department:'+department.upper()+'\n'+
                                        'Age:'+ageinf+'\n'+'Address:'+adrrs.upper()+'\n'+'Phone no.:'+phone)

        else:
            tkinter.messagebox.showerror('Error', 'Employee record doesnt exist')
class RemovePage(Frame):
    """This class helps to delete the employee"""
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller=controller
         #label of the application window
        self.heading= Label(self, text="Welcome to Remove Page", font=('Arial 40 bold'), fg='black', bg='lightgreen')
        self.heading.pack(padx=10,pady=10)

        self.remove_frame = Frame(self,width=300,height=500)

        self.l1 = Label(self.remove_frame,text="Enter Full Name  *")
        self.l1.pack(side='left')
        self.remove_val = Entry(self.remove_frame,width=30)
        self.remove_val.pack(side='left',padx=10,pady=10)



        search_btn  = Button(self.remove_frame,width=20, text='Delete',command=self.Delete_Employee)
        search_btn.pack(side='left')
        res_frame = Frame(self.remove_frame,bg="green")
        res_frame.pack()

        dash_btn = Button(self.remove_frame,text="Return To dashboard",bg='green',fg='white',font=('Arial 10 bold'),command=lambda:controller.show_frame(AddEmpPage))
        dash_btn.pack(side='left')
        self.remove_frame.pack()
    def Delete_Employee(self):
        """This method helps to remove the file of registered employee"""
        rname = self.remove_val.get()
        data_file = str(rname)+'.txt'
        file_list=os.listdir()
        print(file_list)
        if data_file in file_list:
            os.remove(data_file)
            tkinter.messagebox.showinfo("Information", "Employee record deleted successfully")
            self.controller.show_frame(AddEmpPage)
        else:
            tkinter.messagebox.showerror('Error', 'Employee record doesnt exist')



a=EmployeeManagementSystem()
a.mainloop()
