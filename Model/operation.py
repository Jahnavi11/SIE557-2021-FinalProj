from Model import DbConnect as dbc
from tkinter import messagebox

'''##To Do --> Write select statement to get all users'''

class UserOperation:
    '''def __init__(self,city=None):
        if city is None:
            city = {}
        self.city = city'''

    def selectUser(self):
        db = dbc.DbAccess
        conn = db.createConn(db)
        sql = "select a.userId,CONCAT(a.lastName,',',a.firstName) as Name, a.userName, c.type as userType, a.addressLine, CONCAT(b.city,',',b.state,',',b.zipcode) as location, a.emailAddress, a.contactNumber from `sie557-2021-fp`.`user` a inner join `sie557-2021-fp`.`address` b on a.addressId = b.addressId inner join `sie557-2021-fp`.`usertype` c on a.userTypeId = c.userTypeId"
        rowNums = None
        rows = None
        try:
            rowNums,rows = db.query_database(conn,sql,None,"select")
        except (Exception) as error:
            print("Error while inserting data to MYSQL", error)
            exit()
        finally:
            return rowNums,rows


    def loadIterableData(self,sql,val):
        db = dbc.DbAccess
        conn = db.createConn(db)
        rowNums = None
        rows = None
        try:
            rowNums, rows = db.query_database(conn, sql, val, "select")
        except (Exception) as error:
            print("Error while inserting data to MYSQL", error)
            exit()
        finally:
            return rowNums,rows

    # def database_error(err):
    #     return False
    #
    # def scroll_forward():
    #     global rowCount
    #     global rowNums
    #
    #     if rowCount >= (num_of_rows - 1):
    #         messagebox.showinfo("Database Error", "End of database")
    #     else:
    #         row_counter = row_counter + 1
    #         fName.set(rows[row_counter][1])
    #         fam.set(rows[row_counter][2])
    #         id.set(rows[row_counter][0])
    #
    # def scroll_back():
    #     global row_counter
    #     global num_of_rows
    #
    #     if row_counter == 0:
    #         messagebox.showinfo("Database Error", "Start of database")
    #     else:
    #         row_counter = row_counter - 1
    #         fName.set(rows[row_counter][1])
    #         fam.set(rows[row_counter][2])
    #         id.set(rows[row_counter][0])

    def checkLogin(self,username,password):
        db = dbc.DbAccess
        conn = db.createConn(db)
        lastNameResult = None
        firstNameResult = None
        try:
            with conn.cursor() as cursor:
                # Create a new record as a test example
                sql = "SELECT IF(EXISTS (SELECT * FROM `sie557-2021-fp`.`user` WHERE userName=%s AND pwd=%s), 1, 0)"
                sqlCred = "SELECT lastName, firstName FROM `sie557-2021-fp`.`user` WHERE userName=%s"

                cursor.execute(sql, (username, password))
                (loginResult,) = cursor.fetchone()
                if loginResult == 1:
                    cursor.execute(sqlCred,username)
                    ((lastNameResult,firstNameResult)) = cursor.fetchone()
                    print("Result Login 1 where Last Name: "+lastNameResult+" and "+firstNameResult)
                num_of_rows = cursor.rowcount
                print("Successfully selected number of rows: " + str(num_of_rows) + " Actual value: " + str(loginResult))

        except (Exception) as error:
            print("Error while inserting data to MYSQL", error)
            exit()
        finally:
            return loginResult, lastNameResult, firstNameResult
            print("value has been returned successfully from finally block")
            cursor.close()
            db.closeConn(db, conn)

    def getCity(self):
        db = dbc.DbAccess
        conn = db.createConn(db)
        try:
            with conn.cursor() as cursor:
                # Create a new record as a test example
                sql = "SELECT DISTINCT city FROM `sie557-2021-fp`.`address`"
                cursor.execute(sql)
                rows = cursor.fetchall()
                num_of_rows = cursor.rowcount
                print("Successfully selected number of rows: " + str(num_of_rows))

        except (Exception) as error:
            print("Error while inserting data to MYSQL", error)
            exit()
        finally:
            return rows
            print("value has been returned successfully from finally block")
            cursor.close()
            db.closeConn(db, conn)

    def getUserType(self):
        db = dbc.DbAccess
        conn = db.createConn(db)
        try:
            with conn.cursor() as cursor:
                # Create a new record as a test example
                sql = "SELECT DISTINCT type FROM `sie557-2021-fp`.`usertype`"
                cursor.execute(sql)
                rows = cursor.fetchall()
                num_of_rows = cursor.rowcount
                print("Successfully selected number of rows: " + str(num_of_rows))

        except (Exception) as error:
            print("Error while inserting data to MYSQL", error)
            exit()
        finally:
            return rows
            print("value has been returned successfully from finally block")
            cursor.close()
            db.closeConn(db, conn)

    def getState(self):
        db = dbc.DbAccess
        conn = db.createConn(db)
        try:
            with conn.cursor() as cursor:
                # Create a new record as a test example
                sql = "SELECT DISTINCT state FROM `sie557-2021-fp`.`address`"
                cursor.execute(sql)
                rows = cursor.fetchall()
                num_of_rows = cursor.rowcount
                print("Successfully selected number of rows: " + str(num_of_rows))

        except (Exception) as error:
            print("Error while inserting data to MYSQL", error)
            exit()
        finally:
            return rows
            print("value has been returned successfully from finally block")
            cursor.close()
            db.closeConn(db, conn)



    def getZip(self,city=None):
        print("Printing city from getZip Method:",city)
        sql=""
        if city is None:
            sql="SELECT zipcode FROM `sie557-2021-fp`.`address`"
        else:
            sql="SELECT zipcode FROM `sie557-2021-fp`.`address` where city=%s"

        db = dbc.DbAccess
        conn = db.createConn(db)

        try:
            with conn.cursor() as cursor:
                # Create a new record as a test example
                #sql = "SELECT zipcode FROM `sie557-2021-fp`.`address` where city=%s"
                if city is None:
                    cursor.execute(sql)
                else:
                    cursor.execute(sql,city)
                rows = cursor.fetchall()
                num_of_rows = cursor.rowcount
                print("Successfully selected number of rows: " + str(num_of_rows))

        except (Exception) as error:
            print("Error while inserting data to MYSQL", error)
            exit()
        finally:
            return rows
            print("value has been returned successfully from finally block")
            cursor.close()
            db.closeConn(db, conn)

    def createUser(self,firstName=None,lastName=None,email=None,phone=None,userName=None,password=None,userType=None,addressLine=None,city=None,state=None,zip=None):
        val = ()
        db = dbc.DbAccess
        conn = db.createConn(db)
        sqlUserTypeId = "select userTypeId from `sie557-2021-fp`.`usertype` where type = %s"
        sqlAddressId = "select addressId from `sie557-2021-fp`.`address` where zipcode = %s"
        sqlInsert = "INSERT INTO `user`(`pwd`, `firstName`, `lastName`, `userTypeId`, `addressLine`, `addressId`, `userName`, `emailAddress`,`contactNumber`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            with conn.cursor() as cursor:
                # Create a new record as a test example
                cursor.execute(sqlUserTypeId,userType)
                (rowUserTypeId,) = cursor.fetchone()
                print("UserId:",rowUserTypeId)
                cursor.execute(sqlAddressId,zip)
                (rowAddressId,) = cursor.fetchone()
                print("AddressId:", rowAddressId)
                val = (password,firstName,lastName,rowUserTypeId,addressLine,rowAddressId,userName,email,phone)
                cursor.execute(sqlInsert,(val))
                conn.commit()

                #print("Successfully selected number of rows: " + str(num_of_rows))

        except (Exception) as error:
            print("Error while inserting data to MYSQL", error)
            exit()
        finally:
            #return rows
            return ("Successfully inserted record for "+firstName+" "+lastName)
            cursor.close()
            db.closeConn(db, conn)

class WorkorderOperation(object):

    def getservices (self):
        db = dbc.DbAccess
        conn = db.createConn(db)
        try:
            with conn.cursor() as cursor:
                sql = "SELECT DISTINCT `serviceType` FROM `sie557-2021-fp`.`service`"
                cursor.execute(sql)
                rows = cursor.fetchall()
                num_of_rows = cursor.rowcount
                # for record in rows:
                #     print(record)
                print("Successfully selected number of rows: " + str(num_of_rows))

        except (Exception) as error:
            print("error while inserting data to MYSQL", error)
            exit()
        finally:
            return num_of_rows,rows
            print("value has been returned successfully from finally block")
            cursor.close()
            db.closeConn(db, conn)

    def getClient (self):
        db = dbc.DbAccess
        conn = db.createConn(db)
        try:
            with conn.cursor() as cursor:
                sql = "select concat(lastName,',',firstName) as clientName from User where userTypeId = 1"
                cursor.execute(sql)
                rows = cursor.fetchall()
                num_of_rows = cursor.rowcount
                # for record in rows:
                #     print(record)
                print("Successfully selected number of rows: " + str(num_of_rows))

        except (Exception) as error:
            print("error while selecting data to MYSQL", error)
            exit()
        finally:
            return num_of_rows,rows
            cursor.close()
            db.closeConn(db, conn)

    def getWorker (self):
        db = dbc.DbAccess
        conn = db.createConn(db)
        try:
            with conn.cursor() as cursor:
                sql = "select concat(lastName,',',firstName) as workerName from User where userTypeId = 2"
                cursor.execute(sql)
                rows = cursor.fetchall()
                num_of_rows = cursor.rowcount
                # for record in rows:
                #     print(record)
                print("Successfully selected number of rows: " + str(num_of_rows))

        except (Exception) as error:
            print("error while inserting data to MYSQL", error)
            exit()
        finally:
            return num_of_rows, rows
            print("value has been returned successfully from finally block")
            cursor.close()
            db.closeConn(db, conn)

    def getOrderstatus (self):
        db = dbc.DbAccess
        conn = db.createConn(db)
        try:
            with conn.cursor() as cursor:
                sql = "SELECT DISTINCT status FROM `orderstatus`"
                cursor.execute(sql)
                rows = cursor.fetchall()
                num_of_rows = cursor.rowcount
                # for record in rows:
                #     print(record)
                print("Successfully selected number of rows: " + str(num_of_rows))

        except (Exception) as error:
            print("error while inserting data to MYSQL", error)
            exit()
        finally:
            return num_of_rows, rows
            cursor.close()
            db.closeConn(db, conn)

    def getWorkorders(self):
        db = dbc.DbAccess
        conn = db.createConn(db)
        sql = "select a.orderId ,CONCAT(b.lastName,',',b.firstName) as clientName ,d.serviceType as serviceName ,CONCAT(c.lastName,',',c.firstName) as workerName ,a.startDate ,a.endDate ,e.status as orderStatus ,f.invoice ,g.paymentStatus from `order` a left join `user` b on a.clientId = b.userId left join `user` c on a.workerId = c.userId left join `service` d on a.serviceId = d.serviceId left join `orderStatus` e on a.orderStatusId = e.orderStatusId left join `payment` f on a.orderId = f.orderId left join `paymentStatus` g on f.paymentStatusId = g.paymentStatusId order by a.orderId"
        rowNums = None
        rows = None
        try:
            rowNums, rows = db.query_database(conn, sql, None, "select")
        except (Exception) as error:
            print("Error while inserting data to MYSQL", error)
            exit()
        finally:
            return rowNums, rows

    def getWorkordersFilters(self,orderId,clientName,serviceName,workerName,startDate,endDate,wStatus,invoice,pStatus):
        db = dbc.DbAccess
        conn = db.createConn(db)

        print("inside gerworkerFilters method")
        print("orderId:",orderId)
        print("cname:",clientName)
        print("sname:",serviceName)
        print("wName:",workerName)
        print("startdate",startDate)
        print("enddate",endDate)
        print("wstatus",wStatus)
        print("invoice:",invoice)
        print("pstatis",pStatus)

        val = (orderId,orderId,clientName,clientName,serviceName,serviceName,workerName,workerName,startDate,startDate,endDate,endDate,wStatus,wStatus,invoice,invoice,pStatus,pStatus)
        try:
            #rowNums, rows = db.query_database(conn, sql, val, "select")
            with conn.cursor() as cursor:
                sql = "select a.orderId ,CONCAT(b.lastName,',',b.firstName) as clientName ,d.serviceType as serviceName ,CONCAT(c.lastName,',',c.firstName) as workerName ,a.startDate ,a.endDate ,e.status as orderStatus ,f.invoice ,g.paymentStatus from `order` a left join `user` b on a.clientId = b.userId left join `user` c on a.workerId = c.userId left join `service` d on a.serviceId = d.serviceId left join `orderStatus` e on a.orderStatusId = e.orderStatusId left join `payment` f on a.orderId = f.orderId left join `paymentStatus` g on f.paymentStatusId = g.paymentStatusId where (%s IS NULL OR a.orderId = %s) AND (%s IS NULL OR CONCAT(b.lastName,',',b.firstName) = %s) AND (%s IS NULL OR d.serviceType = %s) AND (%s IS NULL OR CONCAT(c.lastName,',',c.firstName) = %s) AND (%s IS NULL OR a.startDate = %s) AND (%s IS NULL OR a.endDate = %s) AND (%s IS NULL OR e.status = %s) AND (%s IS NULL OR f.invoice = %s) AND (%s IS NULL OR g.paymentStatus = %s) order by a.orderId"
                cursor.execute(sql,(val))
                rows = cursor.fetchall()
                rowNums = cursor.rowcount

        except (Exception) as error:
            print("Error while inserting data to MYSQL", error)
            exit()
        finally:
            return rowNums, rows

    def createWorkorder(self, serviceType, clientName, workerName ,orderstatus, startDate):
        db = dbc.DbAccess
        conn = db.createConn(db)
        sqlserviceId = "select serviceId from `sie557-2021-fp`.`service` where serviceType = %s"
        sqlclientId = "select userId from `sie557-2021-fp`.`user` where CONCAT(lastName,',',firstName) = %s"
        sqlWorkerId = "select userId from `sie557-2021-fp`.`user` where CONCAT(lastName,',',firstName) = %s"
        sqlorderStatusId = "select orderStatusId from `sie557-2021-fp`.`orderStatus` where status = %s"
        sqlStartDate = "select CURDATE()"

        sqlInsert = "INSERT INTO `order`(`serviceId`, `workerId`, `clientId`, `orderStatusId`, `startDate`, `endDate`) VALUES (%s, %s, %s, %s, %s, %s)"
        val = ()
        try:
            with conn.cursor() as cursor:
                # Create a new record as a test example
                cursor.execute(sqlserviceId, serviceType)
                (rowserviceId,) = cursor.fetchone()
                print("serviceId:", rowserviceId)
                cursor.execute(sqlclientId, clientName)
                (rowclientId,) = cursor.fetchone()
                print("clientId:", rowclientId)
                cursor.execute(sqlWorkerId, workerName)
                (rowWorkerId,) = cursor.fetchone()
                print("rowWorkerId:", rowWorkerId)
                cursor.execute(sqlorderStatusId, orderstatus)
                (rowOrderStatusId,) = cursor.fetchone()
                print("rowOrderStatusId:", rowOrderStatusId)
                if startDate == None or startDate =="None" or startDate == "":
                    cursor.execute(sqlStartDate)
                    (rowCurrentDate,) = cursor.fetchone()
                else:
                    rowCurrentDate = startDate
                print("rowCurrentDate:", rowCurrentDate)
                val = (rowserviceId, rowWorkerId, rowclientId, rowOrderStatusId, rowCurrentDate, None)
                cursor.execute(sqlInsert, (val))
                conn.commit()

        except (Exception) as error:
            print("Error while inserting workorder", error)
            exit()
        finally:
            cursor.close()
            db.closeConn(db, conn)
            return ("Successfully requested workorder for client:" + clientName)

    def updateWorkorder(self, orderId, serviceType, clientName, workerName ,orderstatus, startDate, enddate):
    #def updateWorkorder(self, orderId,orderstatus,enddate):
        db = dbc.DbAccess
        conn = db.createConn(db)
        print("Inside update workorde method:")
        print("OrderId",orderId)
        print("ServiceType",serviceType)
        print("ClientName",clientName)
        print("WorkerName",workerName)
        print("Orderstatus",orderstatus)
        print("startDate",startDate)
        print("enddate:",enddate)
        sqlserviceId = "select serviceId from `sie557-2021-fp`.`service` where serviceType = %s"
        sqlclientId = "select userId from `sie557-2021-fp`.`user` where CONCAT(lastName,',',firstName) = %s"
        sqlWorkerId = "select userId from `sie557-2021-fp`.`user` where CONCAT(lastName,',',firstName) = %s"
        sqlorderStatusId = "select orderStatusId from `sie557-2021-fp`.`orderStatus` where status = %s"
        sqlStartDate = "select CCURDATE()"

        sqlUpdate = "UPDATE `sie557-2021-fp`.`order` SET serviceId = %s, workerId = % s, clientId = %s, orderStatusId = %s, startDate = %s, endDate = %s where orderId = %s"


        try:
            with conn.cursor() as cursor:
                #Create a new record as a test example
                cursor.execute(sqlserviceId, serviceType)
                (rowserviceId,) = cursor.fetchone()
                print("serviceId:", rowserviceId)
                cursor.execute(sqlclientId, clientName)
                (rowclientId,) = cursor.fetchone()
                print("clientId:", rowclientId)
                cursor.execute(sqlWorkerId, workerName)
                (rowWorkerId,) = cursor.fetchone()
                print("rowWorkerId:", rowWorkerId)
                cursor.execute(sqlorderStatusId, orderstatus)
                (rowOrderStatusId,) = cursor.fetchone()
                print("rowOrderStatusId:", rowOrderStatusId)
                if startDate == None or startDate =="":
                    cursor.execute(sqlStartDate)
                    (rowCurrentDate,) = cursor.fetchone()
                else:
                    rowCurrentDate = startDate
                    print("rowCurrentDate:", rowCurrentDate)
                if enddate == "None":
                    enddate = None

                val = (rowserviceId, rowWorkerId, rowclientId, rowOrderStatusId, rowCurrentDate, enddate, orderId)
                cursor.execute(sqlUpdate, (val))
                conn.commit()

                #cursor.execute(sqlUpdate,(val))
                #conn.commit()

        except (Exception) as error:
            print("Error while updating workorder", error)
            exit()
        finally:
            cursor.close()
            db.closeConn(db, conn)
            return ("Successfully updated workorder for client:" + clientName)


class ServiceOperation(object):
    def getServices(self):
        db = dbc.DbAccess
        conn = db.createConn(db)
        sql = "SELECT * FROM `sie557-2021-fp`.`service`"
        rowNums = None
        rows = None
        try:
            rowNums,rows = db.query_database(conn,sql,None,"select")
        except (Exception) as error:
            print("Error while inserting data to MYSQL", error)
            exit()
        finally:
            return rowNums,rows

    def addServices(self,serviceName,rate):
        db = dbc.DbAccess
        conn = db.createConn(db)
        sql = "insert into `sie557-2021-fp`.`service` (`serviceType`,`rate`) VALUES(%s,%s)"
        val=(serviceName,rate)
        rowNums = None
        rows = None
        try:
            #rowNums,rows = db.query_database(conn,sql,val)
            cursor = conn.cursor()
            cursor.execute(sql,val)
            conn.commit()

        except (Exception) as error:
            print("Error while inserting data to MYSQL", error)
            exit()

        finally:
            return ("Successfully inserted record for ",serviceName )
            cursor.close()
            db.closeConn(db, conn)

    def updateServices(self,id,serviceName=None,rate=None):
        db = dbc.DbAccess
        conn = db.createConn(db)
        val = (serviceName, rate, id)
        rowNums = None
        rows = None
        if serviceName == "" and rate == "":
            return ("Service name and Rate both can't be empty")
        else:
            sql = "UPDATE `sie557-2021-fp`.`service` SET serviceType = %s, rate = %s where serviceId = %s"

            try:
                #rowNums,rows = db.query_database(conn,sql,val,"update")
                cursor = conn.cursor()
                cursor.execute(sql,val)
                conn.commit()

            except (Exception) as error:
                print("Error while inserting data to MYSQL", error)
                exit()

            finally:
                return ("Successfully updated record for ",serviceName)
                cursor.close()
                db.closeConn(db, conn)

class PaymentOperation(object):
    def getPaymentStatus(self):
        db = dbc.DbAccess
        conn = db.createConn(db)
        sql = "SELECT DISTINCT paymentStatus FROM `sie557-2021-fp`.`paymentstatus`"
        rowNums = None
        rows = None
        try:
            rowNums,rows = db.query_database(conn,sql,None,"select")
        except (Exception) as error:
            print("Error while selecting data to MYSQL", error)
            exit()
        finally:
            return rowNums,rows

    def calcUpdateInvoice(self,orderId,pymtAmt,pymtStatus=None):
        db = dbc.DbAccess
        conn = db.createConn(db)
        sqlFindOrderId = "SELECT IF(EXISTS (SELECT * FROM `sie557-2021-fp`.`payment` WHERE orderId = %s), 1, 0)"
        sqlInsert = "insert into `sie557-2021-fp`.`payment` (orderId,workDuration,invoice,paymentStatusId,paymentDate) values(%s, %s, %s, %s, %s)"
        sqlUpdate = "update `sie557-2021-fp`.`payment` SET workDuration = %s, invoice = %s, paymentStatusId = %s, paymentDate = %s where orderId = %s"
        sqlFindWorkDuration = "SELECT DATEDIFF(endDate,startDate) FROM `order` WHERE orderId = %s"
        sqlGetServiceRate = "SELECT a.rate from `sie557-2021-fp`.`service` a  inner join `sie557-2021-fp`.`order` b on a.serviceId = b.serviceId  where b.orderId = %s"
        sqlPaymentDate = "select CURDATE()"
        sqlGetPaymentStatusId = "SELECT paymentStatusId FROM `sie557-2021-fp`.`paymentstatus` WHERE paymentStatus = %s"
        self.val = ()
        rowNums = None
        rows = None
        self.typeOfUpdate = None
        try:
            # rowNums,rows = db.query_database(conn,sql,val)

            # find out type of update

            cursor = conn.cursor()
            cursor.execute(sqlFindOrderId,orderId)
            (resultOrderId,) = cursor.fetchone()
            if resultOrderId == 1:
                self.typeOfUpdate = "update"
            else:
                self.typeOfUpdate = "insert"
            print("ResultOrderId: ",resultOrderId)
            print("Type of update: ", self.typeOfUpdate)

            #find out work duration
            cursor.execute(sqlFindWorkDuration, orderId)
            (workingDays,) = cursor.fetchone()
            workDuration = workingDays * 8
            print("working days",workingDays)
            print("working duration",workDuration)

            #get rate
            cursor.execute(sqlGetServiceRate,orderId)
            (rate,) = cursor.fetchone()
            print("Rate for workorder:",rate)

            #calculate invoice
            invoice = (workDuration * rate)
            print("calculated invoice: ",invoice)

            #getPaymentStatusId
            if pymtStatus == "None" or pymtStatus == None or pymtStatus == "":
                (pymtStatusId,) = (2,)
            else:
                cursor.execute(sqlGetPaymentStatusId, pymtStatus)
                (pymtStatusId,) = cursor.fetchone()

            #getPayment Date
            cursor.execute(sqlPaymentDate)
            (paymentDate,) = cursor.fetchone()
            print("Last updated date for payment: ",paymentDate)

            if self.typeOfUpdate == "insert":
                self.val = (orderId,workDuration,invoice,pymtStatusId,paymentDate)
                cursor.execute(sqlInsert,(self.val))
                conn.commit()
            else:
                self.val = (workDuration,invoice,pymtStatusId,paymentDate,orderId)
                cursor.execute(sqlUpdate,(self.val))
                conn.commit()

        except (Exception) as error:
            print("Error while inserting data to MYSQL", error)
            exit()

        finally:
            return ("Successfully calculated/updated invoice for workroder:", orderId)
            cursor.close()
            db.closeConn(db, conn)


#if __name__ == '__main__':
    #op = ServiceOperation
    #op.createUser(op,"N","P","email","nmp","jjv","Worker","any","Irving","TX",75061)






