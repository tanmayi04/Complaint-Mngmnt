import unittest
import sqlite3
from tkinter import Tk
from tkinter.messagebox import showinfo
from tkinter.ttk import Button, Entry, Label, Radiobutton, Style, Text

from db import DBConnect
from main import SaveData, ShowList

class TestComplaintManagementSystem(unittest.TestCase):
    def setUp(self):
        # Create a test database
        self.conn = sqlite3.connect(':memory:')
        self.conn.execute('create table Comp(ID integer primary key autoincrement, Name varchar(255), Gender varchar(255), Comment text)')
        self.conn.commit()

        # Patch DBConnect to use the test database
        DBConnect._db = self.conn

        # Create Tkinter root window
        self.root = Tk()
        self.root.withdraw()  # Hide the root window

    def tearDown(self):
        # Close the test database connection
        self.conn.close()

    def test_SaveData(self):
        # Test SaveData function
        fullname = Entry(self.root)
        fullname.insert(0, "John Doe")

        SpanGender = "male"

        comment = Text(self.root)
        comment.insert("1.0", "This is a test complaint.")

        # Call SaveData function
        SaveData(fullname, SpanGender, comment)

        # Verify that the complaint was added to the database
        cursor = self.conn.execute('select * from Comp')
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['Name'], "John Doe")
        self.assertEqual(rows[0]['Gender'], "male")
        self.assertEqual(rows[0]['Comment'], "This is a test complaint.")

    def test_ShowList(self):
        # Test ShowList function
        # For simplicity, just verify that the function runs without error
        ShowList()

if __name__ == '__main__':
    unittest.main()
