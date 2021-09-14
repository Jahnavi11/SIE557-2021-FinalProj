# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from tkinter import *
from tkinter import ttk
from Model import DbConnect as dbc
from View import tkDesign as desg

# Press the green button in the gutter to run the script.
def run():
    global glbLastName
    global glbFirstName
    glbLastName = ""
    glbFirstName = ""
    # db = dbc.DbAccess
    # conn = db.createConn(db)
    # db.closeConn(db,conn)
    root = Tk()
    root.title("Handyman Workorder System")
    root.geometry("850x750")
    # lblLoggedInUser = Label(root, text="Welcome " + glbLastName + " ," + glbFirstName).pack()
    mainNoteBook = ttk.Notebook(root)
    desg.UserTabDesign(root, mainNoteBook)
    # design.actualDesign(root)
    root.mainloop()
if __name__ == '__main__':
    run()







