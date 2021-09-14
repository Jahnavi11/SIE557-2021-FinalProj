
import pymysql
import Model.db_config_file as db_config_file
class DatabaseError(Exception):
    pass

class DbAccess(object):
    def __init__(self,conn):
        self.conn=conn

    def createConn(self):
        try:
            conn = pymysql.connect(host=db_config_file.DB_SERVER,
                                   user=db_config_file.DB_USER,
                                   password=db_config_file.DB_PASS,
                                   database=db_config_file.DB,
                                   port=db_config_file.DB_PORT)

        except (Exception) as error:
            print("Error while fetching data from MYSQL", error)
            exit()
        finally:
            print("successfully connected to database")
            return conn
            #conn.close()

    def query_database(conn, sql, values, type):
        rowNums = None
        rows = None
        if type == "select":
            try:
                cursor = conn.cursor()
                if(values == None):
                    cursor.execute(sql)
                else:
                     cursor.execute(sql,values)
                rows = cursor.fetchall()
                num_of_rows = cursor.rowcount

            except pymysql.InternalError as e:
                raise DatabaseError
            except pymysql.OperationalError as e:
                raise DatabaseError
            except pymysql.ProgrammingError as e:
                raise DatabaseError
            except pymysql.DataError as e:
                raise DatabaseError
            except pymysql.IntegrityError as e:
                raise DatabaseError
            except pymysql.NotSupportedError as e:
                raise DatabaseError
            finally:
                cursor.close()
                conn.close()
                return rowNums, rows
        else:
            try:
                cursor = conn.cursor()
                cursor.execute(sql,values)
                cursor.commit()
                rows = cursor.fetchall()
                num_of_rows = cursor.rowcount


            except pymysql.InternalError as e:
                raise DatabaseError
            except pymysql.OperationalError as e:
                raise DatabaseError
            except pymysql.ProgrammingError as e:
                raise DatabaseError
            except pymysql.DataError as e:
                raise DatabaseError
            except pymysql.IntegrityError as e:
                raise DatabaseError
            except pymysql.NotSupportedError as e:
                raise DatabaseError
            finally:
                cursor.close()
                conn.close()
                return rowNums, rows


    def closeConn(self,conn):
        try:
            conn = conn
            conn.close()
        except (Exception) as error:
            print("Error while clossing connection with MYSQL", error)
            exit()
        finally:
            print("successfully closed to database")
