from tkinter import *
import tkinter as tk
from tkinter import ttk
from Model import operation as op
global glbCitySelected
glbCitySelected = ""

class TabDesign(object):

    def on_tab_selected(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        if tab_text == "Add User":
            print("Add User tab selected")

        if tab_text == "Add Workorder":
            print("Add Workorder tab selected")

        if tab_text == "Update Workorder":
            print("Update Workorder tab selected")

        if tab_text == "List Workrder":
            print("List Workrder tab selected")
        if tab_text == "Payment":
            print("Payment tab selected")

    def clicker(self):
        #print(self.cityTabAddUser.get())
        placeHolder = self.cityTabAddUser.get()
        placeHolder = placeHolder.replace("('", "")
        placeHolder = placeHolder.replace("',)", "")
        global glbCitySelected
        glbCitySelected = placeHolder
        print(glbCitySelected)

    def onCitySelected(self,event):
        placeHolder = self.cityTabAddUser.get()
        placeHolder = placeHolder.replace("('","")
        placeHolder = placeHolder.replace("',)","")
        global glbCitySelected
        glbCitySelected = placeHolder
        print(glbCitySelected)

    def create(self):
        print(self.firstNameTabAddUser.get())
        print(self.lastNameTabAddUser.get())
        print(self.emailTabAddUser.get())
        print(self.userNameTabAddUser.get())
        print(self.passwordTabAddUser.get())
        print(self.userTypeTabAddUser.get())
        print(self.addressLineTabAddUser.get())
        print(self.cityTabAddUser.get())
        print(self.stateTabAddUser.get())
        print(self.zipTabAddUser.get())

    def __init__(self,master):
        #tk.Tk.__init__(self,master)
        '''self.app = Frame(master)
        self.app.grid()  # puts a frame in grid

        self.bttn1 = Button(self.app, text="Button1", command=self.clicker)
        self.bttn1.grid(row=1, column=1)

        self.bttn2 = Button(self.app, text="Button2", command=self.clicker)
        self.bttn2.grid(row=1, column=2)'''
        self.tab_parent = ttk.Notebook(master)


        # === defined variables for TAB AddUser
        self.firstNameTabAddUser = StringVar()
        self.lastNameTabAddUser = StringVar()
        self.emailTabAddUser = StringVar()
        self.userNameTabAddUser = StringVar()
        self.passwordTabAddUser = StringVar()
        self.userTypeTabAddUser = StringVar()
        self.addressLineTabAddUser = StringVar()
        self.cityTabAddUser = StringVar()
        self.stateTabAddUser = StringVar()
        self.zipTabAddUser = StringVar()

        # === assign tabAddUser to parent
        self.tabAddUser = ttk.Frame(self.tab_parent)

        # === define and add widgets for TAB AddUser
            # lables
        self.firstNameLableTabAddUser = Label(self.tabAddUser, text="First Name").grid(row=0, column=0, padx=15, pady=15)
        self.lastNameLableTabAddUser = Label(self.tabAddUser, text="Last Name").grid(row=1, column=0, padx=15, pady=15)
        self.emailLableTabAddUser = Label(self.tabAddUser, text="Email Id").grid(row=2, column=0, padx=15, pady=15)
        self.userNameLableTabAddUser = Label(self.tabAddUser, text="User Name").grid(row=3, column=0, padx=15, pady=15)
        self.passwordLableTabAddUser = Label(self.tabAddUser, text="Password").grid(row=4, column=0, padx=15, pady=15)
        self.userTypeLableTabAddUser = Label(self.tabAddUser, text="User Type").grid(row=5, column=0, padx=15, pady=15)
        self.addreLineLableTabAddUser = Label(self.tabAddUser, text="Address Line").grid(row=6, column=0, padx=15, pady=15)
        self.cityLableTabAddUser = Label(self.tabAddUser, text="City").grid(row=7, column=0, padx=15, pady=15)
        self.stateNameLableTabAddUser = Label(self.tabAddUser, text="State").grid(row=8, column=0, padx=15, pady=15)
        self.zipcodeNameLableTabAddUser = Label(self.tabAddUser, text="Zipcode").grid(row=9, column=0, padx=15, pady=15)

            # text box entries
        self.firstNameEntryTabAddUser = Entry(self.tabAddUser, textvariable=self.firstNameTabAddUser).grid(row=0, column=1, padx=15, pady=15)
        self.lastNameEntryTabAddUser = Entry(self.tabAddUser, textvariable=self.lastNameTabAddUser).grid(row=1, column=1, padx=15, pady=15)
        self.emailEntryTabAddUser = Entry(self.tabAddUser, textvariable=self.emailTabAddUser).grid(row=2, column=1, padx=15, pady=15)
        self.userNameEntryTabAddUser = Entry(self.tabAddUser, textvariable=self.userNameTabAddUser).grid(row=3, column=1, padx=15, pady=15)
        self.passwordEntryTabAddUser = Entry(self.tabAddUser, textvariable=self.passwordTabAddUser).grid(row=4, column=1, padx=15, pady=15)
        self.addressLineEntryTabAddUser = Entry(self.tabAddUser, textvariable=self.addressLineTabAddUser).grid(row=6, column=1,padx=15, pady=15)


            #drop down boxes
        opObj = op.UserOperation

        self.optionUserType = [
            "Client",
            "Worker"
        ]
        '''optionCity = [
            "Irving",
            "Dallas",
            "Addison"
        ]'''
        self.optionCity = opObj.getCity(opObj)
        self.optionState = [
            "TX",
            "ME"
        ]
        '''optionZip = [
            75063,
            75062
        ]'''

        self.userTypeTabAddUser.set("Select User Type")
        self.userTypeDDTabAddUser = OptionMenu(self.tabAddUser, self.userTypeTabAddUser, *self.optionUserType).grid(row=5, column=1, padx=15, pady=15)
        self.cityTabAddUser.set("Select City")
        self.cityDDTabAddUser = OptionMenu(self.tabAddUser, self.cityTabAddUser, *self.optionCity, command=self.onCitySelected).grid(row=7, column=1, padx=15, pady=15)
        self.stateTabAddUser.set("TX")
        self.stateDDTabAddUser = OptionMenu(self.tabAddUser, self.stateTabAddUser, *self.optionState).grid(row=8, column=1, padx=15, pady=15)
        self.passCity = glbCitySelected
        self.optionZip = opObj.getZip(opObj,glbCitySelected)
        self.zipTabAddUser.set(00000)
        self.zipDDTabAddUser = OptionMenu(self.tabAddUser, self.zipTabAddUser, *self.optionZip).grid(row=9, column=1, padx=15, pady=15)


            # Button
        self.btnCreate = Button(self.tabAddUser, text="Create", command=self.create).grid(row=10, column=0, padx=15, pady=15)
        self.btnCitySelect = Button(self.tabAddUser, text="RefreshZip", command=self.clicker).grid(row=10, column=1, padx=15, pady=15)

        # === widgets for TAB AddWorkorder
        self.tabAddWorkorder = ttk.Frame(self.tab_parent)

        # =============== Add Widgets to GRID on TAB AddWorkorder

        # =============== Add Widgets to GRID on TAB UpdateWorkorder
        self.tabUpdateWorkorder = ttk.Frame(self.tab_parent)

        # =============== Add Widgets to GRID on TAB ListWorkorder
        self.tabListWorkorder = ttk.Frame(self.tab_parent)

        # =============== Add Widgets to GRID on TAB Payment
        self.tabPayment = ttk.Frame(self.tab_parent)

        self.tab_parent.bind("<<NotebookTabChanged>>", self.on_tab_selected)
        self.tab_parent.add(self.tabAddUser, text="Add User")
        self.tab_parent.add(self.tabAddWorkorder, text="Add Workorder")
        self.tabWorkorderChild = ttk.Notebook(self.tabAddWorkorder)
        self.tabWorkOrder1 = ttk.Frame(self.tabWorkorderChild)
        self.tabWorkOrder2 = ttk.Frame(self.tabWorkorderChild)
        self.tabWorkorderChild.add(self.tabWorkOrder1, text="WorkOrder1")
        self.tabWorkorderChild.add(self.tabWorkOrder2, text="WorkOrder2")
        self.tabWorkorderChild.pack(expand=1, fill='both')
        self.tab_parent.add(self.tabUpdateWorkorder, text="Update Workorder")
        self.tab_parent.add(self.tabListWorkorder, text="List Workrder")
        self.tab_parent.add(self.tabPayment, text="Payment")
        self.tab_parent.pack(expand=1, fill='both')


