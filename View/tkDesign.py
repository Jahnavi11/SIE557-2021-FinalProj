from tkinter import *
import tkinter as tk
from datetime import datetime
from tkinter import ttk
from PIL import ImageTk
from tkinter import messagebox
from tkcalendar import *
from Model import operation as op
import main as mn


class UserTabDesign(object):

    global glbCitySelected
    glbCitySelected = ""
    optionZip =[]
    notebook = ttk.Notebook

    def __init__(self,master,notebook):
        #tk.Tk.__init__(self,master,notebook)
        '''self.app = Frame(master)
        self.app.grid()  # puts a frame in grid

        self.bttn1 = Button(self.app, text="Button1", command=self.clicker)
        self.bttn1.grid(row=1, column=1)

        self.bttn2 = Button(self.app, text="Button2", command=self.clicker)
        self.bttn2.grid(row=1, column=2)'''
        self.master = master
        self.userTabParent = notebook

        #========Fun begins now :)===========
        # Add style to Login
        style = ttk.Style()

        # Picka a theme fore Login
        style.theme_use("alt")
        style.configure("Login", background="white", foreground="black", rowheight=25, fieldbackground="gray97")
        style.map('Login', background=[('selected', 'royalblue')])

        # ====== tabUser to parent and child tabs assigned========

        self.tabUser = ttk.Frame(self.userTabParent)
        self.tabUserChild = ttk.Notebook(self.tabUser)
        self.tabLogin = ttk.Frame(self.tabUserChild)
        self.tabSignUp = ttk.Frame(self.tabUserChild)

        self.tabUserChild.add(self.tabLogin, text="Login")
        self.tabUserChild.add(self.tabSignUp, text="Create New Account")
        self.tabUserChild.pack(expand=1, fill='both',padx=10, pady=10)

        # =======defined variables for TAB tabLogin ======

        self.loginUser = StringVar()
        self.loginPwd = StringVar()

        self.loginFrame = Frame(self.tabLogin, bg="LightSteelBlue3")
        self.loginFrame.place(x=150, y=150, height=340, width=500)
        self.bg = ImageTk.PhotoImage(file="images/Login6.jpg")
        self.bg_image = Label(self.loginFrame, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        title = Label(self.loginFrame, text="Login Here", font=("Impact", 27, "bold"), fg="navy", bg="DarkGoldenrod3").place(x=90, y=10)
        self.loginHeader = Label(self.loginFrame, text="Client/Worker Login Area", font=("Goudy old style", 20, "bold"), fg="navy",bg="DarkGoldenRod3").place(x=90, y=50)
        self.lblUserName = Label(self.loginFrame, text="Username", font=("Goudy old style", 15, "bold"), fg="Gray11",bg="white").place(x=90, y=140)
        self.txtUser = Entry(self.loginFrame, font=("times new roman", 15), bg="gray97",textvariable=self.loginUser)
        self.txtUser.place(x=90, y=170, width=350, height=35)

        self.lblPass = Label(self.loginFrame, text="Password", font=("Goudy old style", 15, "bold"), fg="Gray11",bg="white").place(x=90, y=210)
        self.txtPass = Entry(self.loginFrame, font=("times new roman", 15), bg="gray97",show='*',textvariable=self.loginPwd)
        self.txtPass.place(x=90, y=240, width=350, height=35)

        # ==========define and add widgets for TAB tabLogin ==========

        self.btnLogin = Button(self.loginFrame, text="LOGIN",bg="ivory3", fg="navy", bd=1,font=("times new roman", 12), command=self.login).place(x=90, y=280)

        # ========== defined variables for TAB TabSignUp ==========

        self.firstNameTabSignUp = StringVar()
        self.lastNameTabSignUp = StringVar()
        self.emailTabSignUp = StringVar()
        self.phoneTabSignUp = StringVar()
        self.userNameTabSignUp = StringVar()
        self.passwordTabSignUp = StringVar()
        self.userTypeTabSignUp = StringVar()
        self.addressLineTabSignUp = StringVar()
        self.cityTabSignUp = StringVar()
        self.stateTabSignUp = StringVar()
        self.zipTabSignUp = StringVar()

        # ============ define and add widgets for TAB TabSignUp ==========
        # ======== Lables =======

        self.firstNameLableTabSignUp = Label(self.tabSignUp, text="First Name").grid(row=0, column=0, padx=15, pady=15)
        self.lastNameLableTabSignUp = Label(self.tabSignUp, text="Last Name").grid(row=1, column=0, padx=15, pady=15)
        self.emailLableTabSignUp = Label(self.tabSignUp, text="Email Id").grid(row=2, column=0, padx=15, pady=15)
        self.phoneLableTabSignUp = Label(self.tabSignUp, text="Contact No").grid(row=3, column=0, padx=15, pady=15)
        self.userNameLableTabSignUp = Label(self.tabSignUp, text="User Name").grid(row=4, column=0, padx=15, pady=15)
        self.passwordLableTabSignUp = Label(self.tabSignUp, text="Password").grid(row=5, column=0, padx=15, pady=15)
        self.userTypeLableTabSignUp = Label(self.tabSignUp, text="User Type").grid(row=6, column=0, padx=15, pady=15)
        self.addreLineLableTabSignUp = Label(self.tabSignUp, text="Address Line").grid(row=7, column=0, padx=15, pady=15)
        self.cityLableTabSignUp = Label(self.tabSignUp, text="City").grid(row=8, column=0, padx=15, pady=15)
        self.stateNameLableTabSignUp = Label(self.tabSignUp, text="State").grid(row=9, column=0, padx=15, pady=15)
        self.zipcodeNameLableTabSignUp = Label(self.tabSignUp, text="Zipcode").grid(row=10, column=0, padx=15, pady=15)

        #======= Text box entries =======

        self.firstNameEntryTabSignUp = Entry(self.tabSignUp, textvariable=self.firstNameTabSignUp)
        self.firstNameEntryTabSignUp.grid(row=0, column=1, padx=15, pady=15)
        self.lastNameEntryTabSignUp = Entry(self.tabSignUp, textvariable=self.lastNameTabSignUp)
        self.lastNameEntryTabSignUp.grid(row=1, column=1, padx=15, pady=15)
        self.emailEntryTabSignUp = Entry(self.tabSignUp, textvariable=self.emailTabSignUp)
        self.emailEntryTabSignUp.grid(row=2, column=1, padx=15, pady=15)
        self.phoneEntryTabSignUp = Entry(self.tabSignUp, textvariable=self.phoneTabSignUp)
        self.phoneEntryTabSignUp.grid(row=3, column=1, padx=15, pady=15)
        self.userNameEntryTabSignUp = Entry(self.tabSignUp, textvariable=self.userNameTabSignUp)
        self.userNameEntryTabSignUp.grid(row=4, column=1, padx=15, pady=15)
        self.passwordEntryTabSignUp = Entry(self.tabSignUp, textvariable=self.passwordTabSignUp)
        self.passwordEntryTabSignUp.grid(row=5, column=1, padx=15, pady=15)
        self.addressLineEntryTabSignUp = Entry(self.tabSignUp, textvariable=self.addressLineTabSignUp)
        self.addressLineEntryTabSignUp.grid(row=7, column=1, padx=15, pady=15)

        #======= Dropdown Combobox =======

        opObj = op.UserOperation
        self.optionUserType = opObj.getUserType(opObj)
        self.optionCity = opObj.getCity(opObj)
        self.optionState = opObj.getState(opObj)
        self.optionZip = opObj.getZip(opObj,None)

        self.userTypeDDTabSignUp = ttk.Combobox(self.tabSignUp, value=self.optionUserType)
        self.userTypeDDTabSignUp.grid(row=6, column=1, padx=15, pady=15)
        self.userTypeDDTabSignUp.set("Select Usertype")

        #self.cityTabSignUp.set("Select City")
        #self.cityDDTabSignUp = ttk.OptionMenu(self.TabSignUp, self.cityTabSignUp, *self.optionCity, command=self.onCitySelected).grid(row=7, column=1, padx=15, pady=15)
        self.cityDDTabSignUp = ttk.Combobox(self.tabSignUp, value = self.optionCity)
        self.cityDDTabSignUp.grid(row=8, column=1, padx=15, pady=15)
        self.cityDDTabSignUp.set("Select City")
        self.cityDDTabSignUp.bind("<<ComboboxSelected>>",self.onCityComboSelected)

        self.stateDDTabSignUp = ttk.Combobox(self.tabSignUp, value=self.optionState)
        self.stateDDTabSignUp.grid(row=9, column=1, padx=15, pady=15)
        self.stateDDTabSignUp.set("Select State")

        self.zipDDTabSignUp = ttk.Combobox(self.tabSignUp, value = self.optionZip)
        self.zipDDTabSignUp.grid(row=10, column=1, padx=15, pady=15)
        self.zipDDTabSignUp.set("Select Zipcode")
        #self.zipDDTabSignUp.bind("<<ComboboxSelected>>",self.clicker)
        #self.zipDDTabSignUp.bind("<<ComboboxSelected>>", self.onCitySelected)

        #======== Button ========

        self.btnRegister = Button(self.tabSignUp, text="Sign Up", command=self.register).grid(row=11, column=0, padx=15, pady=15)
        self.userTabParent.bind("<<NotebookTabChanged>>", self.onCitySelected)
        self.userTabParent.add(self.tabUser, text="User")
        self.userTabParent.pack(expand=1, fill='both',padx=20, pady=20)

    def login(self):
        opObj = op.UserOperation
        (self.loginResult,self.lastNameResult,self.firstNameResult) = opObj.checkLogin(opObj,self.loginUser.get(),self.loginPwd.get())

        #self.loginResult = 1 # Please uncomment the above code to enable login functionality
        if self.loginResult == 1:
            print("From login method the FirstName:"+self.lastNameResult+" ,"+self.firstNameResult)
            self.userTabParent.hide(0)
            messagebox.showinfo("Message", "Login Successful")
            objProjTabDesign = ProjTabDesign
            objProjTabDesign(self.master, self.userTabParent, self.lastNameResult, self.firstNameResult)
        else:
            messagebox.showinfo("Message", "Incorrect Username or Password! Please login again..")


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
        #self.tab_parent.hide(self.master,2)
        #print(self.cityTabSignUp.get())
        '''placeHolder = self.cityTabSignUp.get()
        placeHolder = placeHolder.replace("('", "")
        placeHolder = placeHolder.replace("',)", "")
        global glbCitySelected
        glbCitySelected = placeHolder
        print(glbCitySelected)
        opObj = op.DbOperation
        self.optionZip = opObj.getZip(glbCitySelected)
        optionZip = self.optionZip'''

    #==============def formatSelection(self,val): =========

    def onCitySelected(self,event):
        placeHolder = self.cityTabSignUp.get()
        placeHolder = placeHolder.replace("('","")
        placeHolder = placeHolder.replace("',)","")
        global glbCitySelected
        glbCitySelected = placeHolder
        print(glbCitySelected)


    def onCityComboSelected(self,event):
        cityName = self.cityDDTabSignUp.get()
        print("place Holder First time:",cityName)
        cityName = cityName.replace("('","")
        cityName = cityName.replace("',)","")
        print("place Holder after chop:", cityName)
        opObj = op.UserOperation
        self.zipDDTabSignUp.config(value=opObj.getZip(opObj,cityName))
        '''global glbCitySelected
        glbCitySelected = placeHolder
        print(glbCitySelected)'''

    def register(self):
        print(self.firstNameTabSignUp.get())
        print(self.lastNameTabSignUp.get())
        print(self.emailTabSignUp.get())
        print(self.phoneTabSignUp.get())
        print(self.userNameTabSignUp.get())
        print(self.passwordTabSignUp.get())
        print(self.userTypeDDTabSignUp.get())
        print(self.addressLineTabSignUp.get())
        print(self.cityDDTabSignUp.get())
        print(self.stateDDTabSignUp.get())
        print(self.zipDDTabSignUp.get())

        opObj = op.UserOperation
        message=opObj.createUser(opObj, self.firstNameTabSignUp.get(), self.lastNameTabSignUp.get(), self.emailTabSignUp.get(),self.phoneTabSignUp.get(), self.userNameTabSignUp.get(), self.passwordTabSignUp.get(), self.userTypeDDTabSignUp.get(),self.addressLineTabSignUp.get(), self.cityDDTabSignUp.get(), self.stateDDTabSignUp.get(),self.zipDDTabSignUp.get())
        self.firstNameEntryTabSignUp.delete(0,'end')
        self.lastNameEntryTabSignUp.delete(0,'end')
        self.emailEntryTabSignUp.delete(0,'end')
        self.phoneEntryTabSignUp.delete(0, 'end')
        self.userNameEntryTabSignUp.delete(0,'end')
        self.passwordEntryTabSignUp.delete(0,'end')
        self.addressLineEntryTabSignUp.delete(0,'end')
        self.userTypeDDTabSignUp.set("Select Usertype")
        self.cityDDTabSignUp.set("Select City")
        self.stateDDTabSignUp.set("Select State")
        self.zipDDTabSignUp.set("Select Zipcode")
        messagebox.showinfo("Message", message)

        #self,firstName=None,lastName=None,email=None,userName=None,password=None,userType=None,addressLine=None,city=None,state=None,zip=None
class ProjTabDesign(object):
    notebook = ttk.Notebook
    def __init__(self,master,notebook,lastNameResult,firstNameResult):
        self.lastNameResult = lastNameResult
        self.firstNameResult = firstNameResult
        self.welcomeStr = "Welcome " + self.lastNameResult + " ," + self.firstNameResult + ""
        self.master = master
        self.projTabParent = notebook
        self.lblLoggedInUser = ttk.Label(self.projTabParent,text=self.welcomeStr)
        self.lblLoggedInUser.pack(side="top")
        #****************Service tab design*****************************************************************************
        # =============== Add tabs to TAB Services
        self.tabServices = ttk.Frame(self.projTabParent)

        # ========== Add controls to tabListService ==========
        #Add style to treeview
        style = ttk.Style()

        #Picka a theme fore treeview
        style.theme_use("alt")
        style.configure("Treeview",background="white",foreground="black",rowheight=25,fieldbackground="white")
        style.map('Treeview',background=[('selected','royalblue')])

        #Add Treeview Frame
        # create Treeview frame
        self.serviceTreeFrame = Frame(self.tabServices)
        self.serviceTreeFrame.pack(pady=20)

        #Treeview scrollbar
        self.serviceTreeScroll = Scrollbar(self.serviceTreeFrame)
        self.serviceTreeScroll.pack(side=RIGHT,fill=Y)

        #Add Treeeview
        self.serviceTree = ttk.Treeview(self.serviceTreeFrame,yscrollcommand=self.serviceTreeScroll.set)

        #Add Columns to Treeview
        self.serviceTree['columns'] = ('serviceId', 'serviceType', 'rate')
        self.serviceTree.column("#0", width=0, stretch=NO)
        self.serviceTree.column("serviceId",anchor=CENTER,width=80)
        self.serviceTree.column("serviceType",anchor=CENTER,width=120)
        self.serviceTree.column("rate", anchor=CENTER, width=120)

        #Add heading to treeview columns
        self.serviceTree.heading("#0",text="",anchor=W)
        self.serviceTree.heading("serviceId", text="Id", anchor=CENTER)
        self.serviceTree.heading("serviceType", text="Services", anchor=CENTER)
        self.serviceTree.heading("rate", text="Rate/Hr", anchor=CENTER)
        self.serviceTree.pack()

        #configure the scrollbar
        self.serviceTreeScroll.config(command=self.serviceTree.yview)

        #Insert data into the service treeview
        self.addRowsTreeView("services")

        #=== create a frame for IO operation for treeview
        self.treeviewFrameIO = Frame(self.tabServices, bg="LightSteelBlue3")
        self.treeviewFrameIO.pack(pady=20)

        #Lables for Treeview
        self.idLblService = Label(self.treeviewFrameIO, text="Id")
        self.idLblService.grid(row=1,column=0)
        self.nameLblService = Label(self.treeviewFrameIO, text="Services")
        self.nameLblService.grid(row=1, column=1)
        self.rateLblService = Label(self.treeviewFrameIO, text="Rates/Hr")
        self.rateLblService.grid(row=1, column=2)

        # Entryboxes for Treeview
        self.idEntryService = Entry(self.treeviewFrameIO)
        self.idEntryService.grid(row=2,column=0)
        self.serviceEntryService = Entry(self.treeviewFrameIO)
        self.serviceEntryService.grid(row=2, column=1)
        self.rateEntryService = Entry(self.treeviewFrameIO)
        self.rateEntryService.grid(row=2, column=2)

        #Buttons
        self.btnServiceFrame = Frame(self.tabServices, bg="LightSteelBlue3")
        self.addServiceBtn = Button(self.btnServiceFrame, text="Add Service", command= self.addService)
        self.addServiceBtn.pack(pady=10)
        self.selectServiceBtn = Button(self.btnServiceFrame, text="Select Service", command=self.selectServiceRecord)
        self.selectServiceBtn.pack(pady=10)
        self.updateServiceBtn = Button(self.btnServiceFrame, text="Update Service", command=self.updateService)
        self.updateServiceBtn.pack(pady=10)
        self.btnServiceFrame.pack(pady=20,padx=20)

        #********Workorder Tab Design***********************************************************************************
        # === widgets for TAB workorder
        self.tabWorkorder = ttk.Frame(self.projTabParent)

        # create Treeview frame
        self.workorderTreeFrame = Frame(self.tabWorkorder)
        self.workorderTreeFrame.pack(pady=10)

        # Treeview scrollbar
        self.workorderTreeScroll = Scrollbar(self.workorderTreeFrame)
        self.workorderTreeScroll.pack(side=RIGHT, fill=Y)

        # ==== Adding Treeview for workorder
        self.workorderTree = ttk.Treeview(self.workorderTreeFrame,yscrollcommand=self.workorderTreeScroll.set)

        # ==== Add columns to the treeview
        self.workorderTree['columns'] = ('OrderId', 'ClientName', 'ServiceName', 'AssignedWorker', 'RequestDate', 'CompletionDate', 'WorkorderStatus', 'Invoice', 'PaymentStatus')
        self.workorderTree.column("#0", width=0, stretch=NO)
        self.workorderTree.column("OrderId", anchor=CENTER, width=80)
        self.workorderTree.column("ClientName", anchor=CENTER, width=120)
        self.workorderTree.column("ServiceName", anchor=CENTER, width=120)
        self.workorderTree.column("AssignedWorker", anchor=CENTER, width=120)
        self.workorderTree.column("RequestDate", anchor=CENTER, width=120)
        self.workorderTree.column("CompletionDate", anchor=CENTER, width=120)
        self.workorderTree.column("WorkorderStatus", anchor=CENTER, width=120)
        self.workorderTree.column("Invoice", anchor=CENTER, width=120)
        self.workorderTree.column("PaymentStatus", anchor=CENTER, width=120)

        # === Adding headings to columns
        self.workorderTree.heading("#0", text="", anchor=W)
        self.workorderTree.heading("OrderId", text="Order Id", anchor=CENTER)
        self.workorderTree.heading("ClientName", text="Client Name", anchor=CENTER)
        self.workorderTree.heading("ServiceName", text="Service Name", anchor=CENTER)
        self.workorderTree.heading("AssignedWorker", text="Assigned Worker", anchor=CENTER)
        self.workorderTree.heading("RequestDate", text="Request Date", anchor=CENTER)
        self.workorderTree.heading("CompletionDate", text="Completion Date", anchor=CENTER)
        self.workorderTree.heading("WorkorderStatus", text="Workorder Status", anchor=CENTER)
        self.workorderTree.heading("Invoice", text="Invoice", anchor=CENTER)
        self.workorderTree.heading("PaymentStatus", text="Payment Status", anchor=CENTER)
        self.workorderTree.pack()

        # === configure the scrollbar
        self.workorderTreeScroll.config(command=self.workorderTree.yview)
        self.addRowsTreeView("workorder")

        #========Workorder IO begins
        self.wkTreeviewFrameIo = Frame(self.tabWorkorder,bg="LightSteelBlue3",padx=5,pady=5)
        self.wkTreeviewFrameIo.pack(pady=20)

        # Lables Insert/Update Lable Texbox Frame
        self.idLblWorkorder = Label(self.wkTreeviewFrameIo, text="Order Id")
        self.idLblWorkorder.grid(row=1, column=0)
        self.cNameLblWorkorder = Label(self.wkTreeviewFrameIo, text="Client Name")
        self.cNameLblWorkorder.grid(row=1, column=1)
        self.srvNameLblWorkorder = Label(self.wkTreeviewFrameIo, text="Service Name")
        self.srvNameLblWorkorder.grid(row=1, column=2)
        self.wNameLblWorkorder = Label(self.wkTreeviewFrameIo, text="Worker Name")
        self.wNameLblWorkorder.grid(row=1, column=3)
        self.startDtLblWorkorder = Label(self.wkTreeviewFrameIo, text="Request Date")
        self.startDtLblWorkorder.grid(row=1, column=4)
        self.endDtLblWorkorder = Label(self.wkTreeviewFrameIo, text="Completion Date")
        self.endDtLblWorkorder.grid(row=1, column=5)
        self.statusLblWorkorder = Label(self.wkTreeviewFrameIo, text="Workorder Status")
        self.statusLblWorkorder.grid(row=1, column=6)
        self.invoiceLblWorkorder = Label(self.wkTreeviewFrameIo, text="Invoice")
        self.invoiceLblWorkorder.grid(row=1, column=7)
        self.pStatusLblWorkorder = Label(self.wkTreeviewFrameIo, text="Payment Status")
        self.pStatusLblWorkorder.grid(row=1, column=8)

        # Entryboxes for workorder treeview
        self.idEntWorkorder = Entry(self.wkTreeviewFrameIo)
        self.idEntWorkorder.grid(row=2, column=0)

        # Dropdown boxes for workorder treeview

        objWkOp = op.WorkorderOperation
        self.wkDDTwClientRowNum, self.optionClientName =  objWkOp.getClient(objWkOp)
        self.cNameDDWorkorder = ttk.Combobox(self.wkTreeviewFrameIo, value=self.optionClientName)
        self.cNameDDWorkorder.grid(row=2, column=1)
        self.cNameDDWorkorder.set("Select")

        self.wkDDTwServiceRowNum, self.optionServiceName = objWkOp.getservices(objWkOp)
        self.srvNameDDWorkorder = ttk.Combobox(self.wkTreeviewFrameIo, value=self.optionServiceName)
        self.srvNameDDWorkorder.grid(row=2, column=2)
        self.srvNameDDWorkorder.set("Select")

        self.wkDDTwWorkerRowNum, self.optionWorkerName = objWkOp.getWorker(objWkOp)
        self.wNameDDWorkorder = ttk.Combobox(self.wkTreeviewFrameIo, value=self.optionWorkerName)
        self.wNameDDWorkorder.grid(row=2, column=3)
        self.wNameDDWorkorder.set("Select")

        self.startDtCalWorkorder = Entry(self.wkTreeviewFrameIo)
        self.startDtCalWorkorder.grid(row=2, column=4)
        self.endDtCalWorkorder = Entry(self.wkTreeviewFrameIo)
        self.endDtCalWorkorder.grid(row=2, column=5)

        self.wkDDTwStatusRowNum, self.optionStatusName = objWkOp.getOrderstatus(objWkOp)
        self.statusDDWorkorder = ttk.Combobox(self.wkTreeviewFrameIo, value=self.optionStatusName)
        self.statusDDWorkorder.grid(row=2, column=6)
        self.statusDDWorkorder.set("Select")

        self.invoiceEntryWorkorder = Entry(self.wkTreeviewFrameIo)
        self.invoiceEntryWorkorder.grid(row=2, column=7)

        objPay = op.PaymentOperation
        self.pstatusDDRowNum, self.optionPymntStatusName = objPay.getPaymentStatus(objPay)
        self.pStatusDDWorkorder = ttk.Combobox(self.wkTreeviewFrameIo, value=self.optionPymntStatusName)
        self.pStatusDDWorkorder.grid(row=2, column=8)
        self.pStatusDDWorkorder.set("Select")

        # ========Workorder Button/Search Frame
        self.wkTreeviewFrameOp = Frame(self.tabWorkorder,bg="LightSteelBlue3")
        self.btnRequestWk = Button(self.wkTreeviewFrameOp, text="Request Workorder", command=self.requestWorkOrder)
        self.btnRequestWk.grid(row=0, column=0, padx=10,pady=5)
        self.btnSelectWk = Button(self.wkTreeviewFrameOp, text="Select Workorder", command=self.selectWorkorderRecord)
        self.btnSelectWk.grid(row=0, column=1, padx=10,pady=5)
        self.btnUpdateWk = Button(self.wkTreeviewFrameOp, text="Update Workorder", command=self.updateWorkorder)
        self.btnUpdateWk.grid(row=1, column=0, padx=10,pady=5)
        self.btnCalcInvoice = Button(self.wkTreeviewFrameOp, text="Calculate Invoice", command=self.calcInvoice)
        self.btnCalcInvoice.grid(row=1,column=1, padx=10,pady=5)
        self.btnStartDate = Button(self.wkTreeviewFrameOp, text="Get Startdate", command=self.getWrkStartDate)
        self.btnStartDate.grid(row=0,column=2, padx=10,pady=5)
        self.btnEndDate = Button(self.wkTreeviewFrameOp, text="Get Enddate", command=self.getWrkEndDate)
        self.btnEndDate.grid(row=1,column=2, padx=10,pady=5)
        self.btnWkSearch = Button(self.wkTreeviewFrameOp, text="Search", command=self.getSearch)
        self.btnWkSearch.grid(row=0, column=3, padx=10,pady=5)
        self.btnClear = Button(self.wkTreeviewFrameOp, text="Clear", command=self.setClear)
        self.btnClear.grid(row=1, column=3, padx=10, pady=5)
        #pack wkTreeviewFrameOp
        self.wkTreeviewFrameOp.pack(padx=170,side="left")

        # === Add Calendar
        self.wkTreeviewFrameCal = Frame(self.tabWorkorder, bg="LightSteelBlue3")
        self.calFrame = Frame(self.wkTreeviewFrameCal)
        #self.cal = Calendar(self.calFrame, selectmode="day", year=2021, month=5, day=6)
        self.cal = Calendar(self.calFrame, selectmode="day", date_pattern = 'yyyy/mm/dd', year=2021, month=5, day=6)
        self.cal.pack(side="top")
        self.calFrame.pack(padx=20,pady=20)
        self.wkTreeviewFrameCal.pack(padx=200,pady=20, side="right")

        # ==============================================User management ======================
        self.tabManageUser = ttk.Frame(self.projTabParent)
        # create Treeview frame
        self.userTreeFrame = Frame(self.tabManageUser)
        self.userTreeFrame.pack(pady=10)

        # Treeview scrollbar
        self.userTreeScroll = Scrollbar(self.userTreeFrame)
        self.userTreeScroll.pack(side=RIGHT, fill=Y)

        # ==== Adding Treeview for workorder
        self.userTree = ttk.Treeview(self.userTreeFrame, yscrollcommand=self.userTreeScroll.set)

        # ==== Add columns to the treeview
        self.userTree['columns'] = (
            'userId', 'Name', 'UserName', 'UserType', 'AddressLine', 'AddressId',
            'Email','Phone')
        self.userTree.column("#0", width=0, stretch=NO)
        self.userTree.column("userId", anchor=CENTER, width=80)
        self.userTree.column("Name", anchor=CENTER, width=120)
        self.userTree.column("UserName", anchor=CENTER, width=120)
        self.userTree.column("UserType", anchor=CENTER, width=120)
        self.userTree.column("AddressLine", anchor=CENTER, width=120)
        self.userTree.column("AddressId", anchor=CENTER, width=120)
        self.userTree.column("Email", anchor=CENTER, width=120)
        self.userTree.column("Phone", anchor=CENTER, width=120)

        # === Adding headings to columns
        self.userTree.heading("#0", text="", anchor=W)
        self.userTree.heading("userId", text="Id", anchor=CENTER)
        self.userTree.heading("Name", text="Name", anchor=CENTER)
        self.userTree.heading("UserName", text="User Name", anchor=CENTER)
        self.userTree.heading("UserType", text="User Type", anchor=CENTER)
        self.userTree.heading("AddressLine", text="AddressLine", anchor=CENTER)
        self.userTree.heading("AddressId", text="AddressId", anchor=CENTER)
        self.userTree.heading("Email", text="Email", anchor=CENTER)
        self.userTree.heading("Phone", text="Phone", anchor=CENTER)
        self.userTree.pack()

        # === configure the scrollbar
        self.userTreeScroll.config(command=self.userTree.yview)
        self.addRowsTreeView("user")

        # =============== Add Widgets to GRID on TAB Payment
        self.tabPayment = ttk.Frame(self.projTabParent)
        self.tabPaymentChild = ttk.Notebook(self.tabPayment)
        self.tabCalculatePayment = ttk.Frame(self.tabPaymentChild)
        self.tabUpdatePayment = ttk.Frame(self.tabPaymentChild)
        self.tabListPayment = ttk.Frame(self.tabPaymentChild)
        self.tabPaymentChild.add(self.tabCalculatePayment, text="Generate Bill")
        self.tabPaymentChild.add(self.tabListPayment, text="Payment Report ")
        self.tabPaymentChild.add(self.tabUpdatePayment, text="Update Payment")
        self.tabPaymentChild.pack(expand=1, fill='both', padx=10, pady=10)

        # =============== Add Widgets to GRID for tabl logout
        self.tabLogoutParent = ttk.Frame(self.projTabParent)
        self.tabExitParent = ttk.Frame(self.projTabParent)
        # self.tabLogoutChild = ttk.Notebook(self.tabLogoutParent)
        # self.tabLogout =ttk.Frame(self.tabLogoutChild)
        # self.tabExit = ttk.Frame(self.tabLogoutChild)
        # self.tabLogoutChild.add(self.tabLogout, text="Logout")
        # self.tabLogoutChild.add(self.tabExit, text="Exit")
        # self.tabLogoutChild.pack()

        # =============== Add Widgets to GRID on TAB Manage Users

        self.projTabParent.add(self.tabServices, text="Services")
        self.projTabParent.add(self.tabWorkorder, text="Workorder")
        self.projTabParent.add(self.tabManageUser, text="Manage User")
        self.projTabParent.add(self.tabPayment, text="Payment")
        self.projTabParent.add(self.tabLogoutParent, text="Logout")
        self.projTabParent.add(self.tabExitParent, text="Exit")
        self.projTabParent.pack(expand=1, fill='both', padx=20, pady=20)
        self.projTabParent.bind("<<NotebookTabChanged>>", self.on_projTab_selected)
        # self.tabLogoutChild.bind("<<NotebookTabChanged>>", self.on_logoutTab_selected)

    def setClear(self):
        self.idEntWorkorder.config(state=NORMAL)
        self.idEntWorkorder.delete(0, END)
        self.startDtCalWorkorder.delete(0, END)
        self.endDtCalWorkorder.delete(0, END)
        self.invoiceEntryWorkorder.delete(0, END)
        self.cNameDDWorkorder.set("Select")
        self.srvNameDDWorkorder.set("Select")
        self.wNameDDWorkorder.set("Select")
        self.statusDDWorkorder.set("Select")
        self.pStatusDDWorkorder.set("Select")

    def getWrkStartDate(self):
        self.startDtCalWorkorder.delete(0, END)
        self.startDtCalWorkorder.insert(0, self.cal.get_date().replace("/", "-"))

    def getWrkEndDate(self):
        self.endDtCalWorkorder.delete(0, END)
        self.endDtCalWorkorder.insert(0, self.cal.get_date().replace("/", "-"))

    def getSearch(self):
        pOrderId = self.idEntWorkorder.get()
        self.pClientName = self.cNameDDWorkorder.get()
        self.pServiceName = self.srvNameDDWorkorder.get()
        self.pWorkerName = self.wNameDDWorkorder.get()
        self.pStartDate = self.startDtCalWorkorder.get()
        self.pEndDate = self.endDtCalWorkorder.get()
        self.pWStatus = self.statusDDWorkorder.get()
        self.pInvoice = self.invoiceEntryWorkorder.get()
        self.pIStatus = self.pStatusDDWorkorder.get()

        if pOrderId == "":
            self.pOrderId = None
        if self.pClientName == "Select":
            self.pClientName = None
        if self.pServiceName == "Select":
            self.pServiceName = None
        if self.pWorkerName == "Select":
            self.pWorkerName = None
        if self.pStartDate == "":
            self.pStartDate = None
        if self.pEndDate == "":
            self.pEndDate = None
        if self.pWStatus == "Select":
            self.pWStatus = None
        if self.pInvoice == "":
            self.pInvoice = None
        if self.pIStatus == "Select":
            self.pIStatus = None

        # delete existing record to load filtered results
        for i in self.workorderTree.get_children():
            self.workorderTree.delete(i)
        # DB call
        opObjWK = op.WorkorderOperation
        self.workOrderRowCnt, self.WorkOrderFilterList = opObjWK.getWorkordersFilters(opObjWK, self.pOrderId,
                                                                                      self.pClientName,
                                                                                      self.pServiceName,
                                                                                      self.pWorkerName, self.pStartDate,
                                                                                      self.pEndDate, self.pWStatus,
                                                                                      self.pInvoice, self.pIStatus)

        # create striped row tags
        self.workorderTree.tag_configure('oddrow', background="white")
        self.workorderTree.tag_configure('evenrow', background="lightblue")

        # insert rows in workorder treeview
        self.workorderFilterCnt = 0
        for i in self.WorkOrderFilterList:
            if self.workorderFilterCnt % 2 == 0:
                self.workorderTree.insert(parent='', index='end', iid=self.workorderFilterCnt, text='',
                                          values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]),
                                          tags=('evenrow',))
            else:
                self.workorderTree.insert(parent='', index='end', iid=self.workorderFilterCnt, text='',
                                          values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]),
                                          tags=('oddrow',))
            self.workorderFilterCnt += 1

        self.idEntWorkorder.delete(0, END)
        self.startDtCalWorkorder.delete(0, END)
        self.endDtCalWorkorder.delete(0, END)
        self.invoiceEntryWorkorder.delete(0, END)
        self.cNameDDWorkorder.set("Select")
        self.srvNameDDWorkorder.set("Select")
        self.wNameDDWorkorder.set("Select")
        self.statusDDWorkorder.set("Select")
        self.pStatusDDWorkorder.set("Select")

    def addRowsTreeView(self, treeviewName):
        if treeviewName == "services":
            # =========get list from db
            opObj = op.ServiceOperation
            self.serviceListCnt, self.serviceList = opObj.getServices(opObj)

            # create striped row tags
            self.serviceTree.tag_configure('oddrow', background="white")
            self.serviceTree.tag_configure('evenrow', background="lightblue")

            # insert rows in service treeview
            self.serviceCnt = 0
            for item in self.serviceList:
                if self.serviceCnt % 2 == 0:
                    self.serviceTree.insert(parent='', index='end', iid=self.serviceCnt, text='',
                                            values=(item[0], item[1], item[2]), tags=('evenrow',))
                    print(str(item[0]), str(item[1]), str(item[2]))
                else:
                    self.serviceTree.insert(parent='', index='end', iid=self.serviceCnt, text='',
                                            values=(item[0], item[1], item[2]), tags=('oddrow',))
                    print(str(item[0]), str(item[1]), str(item[2]))
                self.serviceCnt += 1
        if treeviewName == "workorder":
            # === get list from db
            opObjWK = op.WorkorderOperation
            self.workorderListCnt, self.workorderList = opObjWK.getWorkorders(opObjWK)

            # create striped row tags
            self.workorderTree.tag_configure('oddrow', background="white")
            self.workorderTree.tag_configure('evenrow', background="lightblue")

            # insert rows in workorder treeview
            self.workorderCnt = 0
            for i in self.workorderList:
                if self.workorderCnt % 2 == 0:
                    self.workorderTree.insert(parent='', index='end', iid=self.workorderCnt, text='',
                                              values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]),
                                              tags=('evenrow',))
                else:
                    self.workorderTree.insert(parent='', index='end', iid=self.workorderCnt, text='',
                                              values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]),
                                              tags=('oddrow',))
                self.workorderCnt += 1

        if treeviewName == "user":
            # === get list from db
            objUser = op.UserOperation
            self.userListCnt, self.userList = objUser.selectUser(objUser)

            # create striped row tags
            self.userTree.tag_configure('oddrow', background="white")
            self.userTree.tag_configure('evenrow', background="lightblue")

            # insert rows in workorder treeview
            self.userCnt = 0
            for i in self.userList:
                if self.userCnt % 2 == 0:
                    self.userTree.insert(parent='', index='end', iid=self.userCnt, text='',
                                         values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]),
                                         tags=('evenrow',))
                else:
                    self.userTree.insert(parent='', index='end', iid=self.userCnt, text='',
                                         values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]),
                                         tags=('oddrow',))
                self.userCnt += 1

    def requestWorkOrder(self):
        objWkOp = op.WorkorderOperation
        if self.srvNameDDWorkorder.get() == "Select":
            messagebox.showinfo("Plese select service to request a workeorder")
        elif self.cNameDDWorkorder.get() == "Select":
            messagebox.showinfo("Plese select client for a workeorder")
        elif self.wNameDDWorkorder.get() == "Select":
            messagebox.showinfo("Plese select worker for a workeorder")
        elif self.statusDDWorkorder.get() == "Select":
            messagebox.showinfo("Plese select initial workorder status")
        elif self.startDtCalWorkorder.get() == "" or self.startDtCalWorkorder.get() == None:
            self.startDtCalWorkorder.get() == None
        self.requestWorkorderResult = objWkOp.createWorkorder(objWkOp, self.srvNameDDWorkorder.get(),
                                                              self.cNameDDWorkorder.get(), self.wNameDDWorkorder.get(),
                                                              self.statusDDWorkorder.get(),
                                                              self.startDtCalWorkorder.get())

        for i in self.workorderTree.get_children():
            self.workorderTree.delete(i)

        self.addRowsTreeView("workorder")
        self.idEntWorkorder.delete(0, END)
        self.startDtCalWorkorder.delete(0, END)
        self.endDtCalWorkorder.delete(0, END)
        self.invoiceEntryWorkorder.delete(0, END)
        self.cNameDDWorkorder.set("Select")
        self.srvNameDDWorkorder.set("Select")
        self.wNameDDWorkorder.set("Select")
        self.statusDDWorkorder.set("Select")
        self.pStatusDDWorkorder.set("Select")
        messagebox.showinfo("Message", self.requestWorkorderResult)

    def addService(self):
        # self.serviceTree.insert(parent='', index='end', iid=self.serviceCnt, text='',values=(self.idEntryService.get(), self.serviceEntryService.get(), self.rateEntryService.get()))
        # self.idEntryService.config(state=DISABLED)
        opObj = op.ServiceOperation
        self.addServiceResult = opObj.addServices(opObj, self.serviceEntryService.get(), self.rateEntryService.get())

        # delete current records from service treeview
        for i in self.serviceTree.get_children():
            self.serviceTree.delete(i)
        # repopulate the data into the treeview
        self.addRowsTreeView("services")
        # clear the text box for further operations
        self.idEntryService.delete(0, END)
        self.serviceEntryService.delete(0, END)
        self.rateEntryService.delete(0, END)
        messagebox.showinfo("Message", self.addServiceResult)

    def selectWorkorderRecord(self):
        self.idEntWorkorder.delete(0, END)
        self.startDtCalWorkorder.delete(0, END)
        self.endDtCalWorkorder.delete(0, END)
        self.invoiceEntryWorkorder.delete(0, END)
        self.cNameDDWorkorder.set("Select")
        self.srvNameDDWorkorder.set("Select")
        self.wNameDDWorkorder.set("Select")
        self.statusDDWorkorder.set("Select")
        self.pStatusDDWorkorder.set("Select")
        # Grab record number
        selected = self.workorderTree.focus()
        val = self.workorderTree.item(selected, 'values')

        # output to entry boxes
        self.idEntWorkorder.insert(0, val[0])
        self.cNameDDWorkorder.set(val[1])
        self.srvNameDDWorkorder.set(val[2])
        self.wNameDDWorkorder.set(val[3])
        self.startDtCalWorkorder.insert(0, val[4])
        self.endDtCalWorkorder.insert(0, val[5])
        self.statusDDWorkorder.set(val[6])
        self.invoiceEntryWorkorder.insert(0, val[7])
        self.pStatusDDWorkorder.set(val[8])
        self.idEntWorkorder.config(state=DISABLED)

    def selectServiceRecord(self):
        self.idEntryService.delete(0, END)
        self.serviceEntryService.delete(0, END)
        self.rateEntryService.delete(0, END)
        # Grab record number
        selected = self.serviceTree.focus()
        val = self.serviceTree.item(selected, 'values')

        # output to entry boxes
        self.idEntryService.insert(0, val[0])
        self.serviceEntryService.insert(0, val[1])
        self.rateEntryService.insert(0, val[2])
        self.idEntryService.config(state=DISABLED)

    def calcInvoice(self):
        obPayOp = op.PaymentOperation
        if self.endDtCalWorkorder.get() == "None" or self.endDtCalWorkorder.get() == "":
            messagebox.showinfo("Message", "Please select completion date to calculate invoice")
        else:
            self.updateWorkorderResult = obPayOp.calcUpdateInvoice(obPayOp, self.idEntWorkorder.get(),
                                                                   self.invoiceEntryWorkorder.get(),
                                                                   self.pStatusDDWorkorder.get())
            self.idEntWorkorder.config(state=NORMAL)
            # remove old data from workorder treeview
            for i in self.workorderTree.get_children():
                self.workorderTree.delete(i)
            # repopulate the data with updated record
            self.addRowsTreeView("workorder")
            self.idEntWorkorder.delete(0, END)
            self.startDtCalWorkorder.delete(0, END)
            self.endDtCalWorkorder.delete(0, END)
            self.invoiceEntryWorkorder.delete(0, END)
            self.cNameDDWorkorder.set("Select")
            self.srvNameDDWorkorder.set("Select")
            self.wNameDDWorkorder.set("Select")
            self.statusDDWorkorder.set("Select")
            self.pStatusDDWorkorder.set("Select")
            messagebox.showinfo("Message", self.updateWorkorderResult)

    def updateWorkorder(self):
        selected = self.workorderTree.focus()
        objWkOp = op.WorkorderOperation
        self.updateWorkorderResult = objWkOp.updateWorkorder(objWkOp, self.idEntWorkorder.get(),
                                                             self.srvNameDDWorkorder.get(), self.cNameDDWorkorder.get(),
                                                             self.wNameDDWorkorder.get(), self.statusDDWorkorder.get(),
                                                             self.startDtCalWorkorder.get(),
                                                             self.endDtCalWorkorder.get())
        # self.updateWorkorderResult = objWkOp.updateWorkorder(objWkOp,self.idEntWorkorder.get(),self.statusDDWorkorder.get())
        self.idEntWorkorder.config(state=NORMAL)

        # remove old data from workorder treeview
        for i in self.workorderTree.get_children():
            self.workorderTree.delete(i)

        # repopulate the data with updated record
        self.addRowsTreeView("workorder")
        self.idEntWorkorder.delete(0, END)
        self.startDtCalWorkorder.delete(0, END)
        self.endDtCalWorkorder.delete(0, END)
        self.invoiceEntryWorkorder.delete(0, END)
        self.cNameDDWorkorder.set("Select")
        self.srvNameDDWorkorder.set("Select")
        self.wNameDDWorkorder.set("Select")
        self.statusDDWorkorder.set("Select")
        self.pStatusDDWorkorder.set("Select")
        messagebox.showinfo("Message", self.updateWorkorderResult)

    def updateService(self):
        # messagebox.showinfo("Message","Functionality in Progress, Be patient!")
        selected = self.serviceTree.focus()
        # save new data
        opObj = op.ServiceOperation
        self.updateServiceResult = opObj.updateServices(opObj, self.idEntryService.get(),
                                                        self.serviceEntryService.get(), self.rateEntryService.get())

        # self.serviceTree.item(selected,text="",values=(self.idEntryService.get(),self.serviceEntryService.get(),self.rateEntryService.get()))
        self.idEntryService.config(state=NORMAL)
        # self.serviceListCnt, self.serviceList = opObj.getServices(opObj) --> Remove after testing not needed

        # delete the old records from service treeview
        for i in self.serviceTree.get_children():
            self.serviceTree.delete(i)

        # repopulate the records into the services
        self.addRowsTreeView("services")
        self.idEntryService.delete(0, END)
        self.serviceEntryService.delete(0, END)
        self.rateEntryService.delete(0, END)
        messagebox.showinfo("Message", self.updateServiceResult)

    def on_projTab_selected(self, event):
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        if tab_text == "Logout":
            #     self.projTabParent.hide(0)
            #     self.projTabParent.hide(1)
            #     self.projTabParent.hide(2)
            #     self.projTabParent.hide(3)
            #     self.projTabParent.hide(4)
            #     self.lblLoggedInUser.pack_forget()
            self.master.destroy()
            mn.run()
        if tab_text == "Exit":
            self.master.destroy()

        # def on_logoutTab_selected(self, event):
        #     selected_tab = event.widget.select()
        #     tab_text = event.widget.tab(selected_tab, "text")
        #     if tab_text == "Logout":
        #         self.master.dstroy()
        #         mn.run()
        #     if tab_text == "Exit":
        #         self.master.dstroy()

    def deleteLoginUserLbl(self):
        self.lblLoggedInUser.pack_forget()

    # if __name__ == '__main__':
    #     op = ProjTabDesign
    #     op.getWrkStartDate(op)









