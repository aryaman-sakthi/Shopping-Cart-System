import datetime
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QApplication, QCompleter, QComboBox, QMessageBox, QDialog
import mysql.connector

from db import DB
from control import Ui_ShoppingCartSystem

class MainWindow:
    def __init__(self):
        # Initializing main app window
        self.main_win = QMainWindow()
        self.main_win.setFixedSize(1020, 750)

        # Adding ui file
        self.ui = Ui_ShoppingCartSystem()
        self.ui.setupUi(self.main_win)
        
        # DataBase Connection
        self.con = DB()
        self.cur = self.con.dbcursor
        
        
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        
        self.ui.b1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.item_page)) 
        self.ui.go_back.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.item_page))
        self.ui.home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))
        self.ui.order_b.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cart_page))
        self.ui.go_to_cart.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cart_page))
        self.ui.go_to_cart_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cart_page))
        self.ui.bill_b.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.bill_page))
        self.ui.go_bill.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.bill_page))
        self.ui.customer_b.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.customer_page))
        self.ui.inventory_b.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.inventory_page))
        self.ui.details_b.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.details_page))
        self.ui.show.clicked.connect(self.loadDataFromatt)
        self.ui.send.clicked.connect(self.Add_to_cart)
        self.ui.cart_show.clicked.connect(self.loadOrders)
        self.ui.bill_show.clicked.connect(self.loadBills)
        self.ui.generatebill.clicked.connect(self.generateBill)
        self.ui.login_b.clicked.connect(self.login)
        self.ui.add_customer.clicked.connect(self.add_customer)
        self.ui.customer_load.clicked.connect(self.loadCustomers)
        self.ui.inventory_load.clicked.connect(self.loadInventory)
        self.ui.restock_b.clicked.connect(self.restock)
        self.ui.details_load.clicked.connect(self.loadDetails)
        self.ui.exit_b.clicked.connect(self.exit)
    
    
    
    def exit(self):
         quit()
    
    def error_msg(self):
        msg = QMessageBox()  
        msg.setWindowTitle("Error")      
        msg.setText("Incorrect or Missing Value")   
        msg.setIcon(QMessageBox.Critical)
        x=msg.exec_()
        
            
    def login(self):
        id = self.ui.l_id.text()
        password = self.ui.l_password.text()
        id = str(id)
        password = str(password)
        if (id=="117" and password=="arya"):      
            self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        
        
    def loadDataFromatt(self): 
            query = "SELECT * FROM Items" 
            self.cur.execute(query)
            result=self.cur.fetchall()
            self.ui.item_table.setRowCount(len(result)) 
            for row_number, row_data in enumerate(result): 
                self.ui.item_table.insertRow(row_number) 
                for column_number, data in enumerate(row_data): 
                    self.ui.item_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    
    def loadInventory(self): 
            query = "select I_ID,Name,Quantity from items natural join inventory" 
            self.cur.execute(query)
            result=self.cur.fetchall()
            self.ui.inventory_table.setRowCount(len(result)) 
            for row_number, row_data in enumerate(result): 
                self.ui.inventory_table.insertRow(row_number) 
                for column_number, data in enumerate(row_data): 
                    self.ui.inventory_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    
    
    def loadDetails(self):
        try: 
            dets = self.ui.details_id.text()
            
            query = ("call item_details(%s)"%dets)
            self.cur.execute(query)
            result=self.cur.fetchall()
            self.ui.details_table.setRowCount(len(result)) 
            for row_number, row_data in enumerate(result): 
                self.ui.details_table.insertRow(row_number) 
                for column_number, data in enumerate(row_data): 
                    self.ui.details_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
            
            self.cur.close()
            self.con = DB()
            self.cur = self.con.dbcursor
        
        except mysql.connector.errors.DatabaseError:
            self.error_msg()
        
                    
    def restock_popup(self):
        msg = QMessageBox()  
        msg.setWindowTitle("Success")      
        msg.setText("Item Restocked Successfully")   
        x=msg.exec_()
                        
    def restock(self):
        try:
            try:
                i_id = self.ui.inventory_id.text()
                quantity = self.ui.restock.text()
                quantity = int(quantity)
                query = ("update inventory set Quantity = %d where I_ID = %s"%(quantity,i_id))
                self.cur.execute(query)
                self.restock_popup()
            
            except mysql.connector.errors.DatabaseError:
                self.error_msg()
        except ValueError:
            self.error_msg()
        
                    
    def loadOrders(self):
        query = "SELECT * FROM Cart"
        self.cur.execute(query)
        result=self.cur.fetchall()
        self.ui.cart_table.setRowCount(len(result))
        for row_number, row_data in enumerate(result): 
            self.ui.cart_table.insertRow(row_number)
            for column_number, data in enumerate(row_data): 
                    self.ui.cart_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    
    def loadBills(self):
        query = "select B_ID,C_ID,C_name,Total_Price,Order_Date from Bill natural join Customers"
        self.cur.execute(query)
        result=self.cur.fetchall()
        self.ui.bill_table.setRowCount(len(result))
        for row_number, row_data in enumerate(result): 
            self.ui.bill_table.insertRow(row_number)
            for column_number, data in enumerate(row_data): 
                    self.ui.bill_table.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                    
    def loadCustomers(self):
        query= "SELECT * FROM  CUSTOMERS"
        self.cur.execute(query)
        result=self.cur.fetchall()
        self.ui.customer_table.setRowCount(len(result))
        for row_number, row_data in enumerate(result):
            self.ui.customer_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui.customer_table.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
    
                    
    def cart_popup(self):
        msg = QMessageBox()  
        msg.setWindowTitle("Success")      
        msg.setText("Item Added to Cart Successfully")   
        x=msg.exec_()
    
        
    def Add_to_cart(self):
        try:
            s = self.ui.qute.text()
            l = self.ui.order.text()
            q = self.ui.quantity.text()
            args = (l,s,q)
            self.cur.callproc("addtocart",args)
            self.cart_popup()
        
        except mysql.connector.errors.DatabaseError:
            self.error_msg()
            
        
              
     
        
    def customer_popup(self):
        msg = QMessageBox()  
        msg.setWindowTitle("Success")      
        msg.setText("Customer Registered Successfully")   
        x=msg.exec_() 
          
    def add_customer(self):
        try:
            id = self.ui.C_id.text()
            name = self.ui.C_name.text()
            phone = self.ui.C_phone.text()
            address = self.ui.C_address.text()
            
            query = "INSERT INTO Customers values (%s,'%s',%s,'%s')"%(id,name,phone,address)
            
            self.cur.execute(query)
            
            self.customer_popup()
        
        except mysql.connector.errors.DatabaseError:
            self.error_msg()
            
    
          
    def bill_popup(self):
        msg = QMessageBox()  
        msg.setWindowTitle("Success")      
        msg.setText("Bill Generated Successfully")   
        x=msg.exec_()    
        
    def generateBill(self):
        try:
            b = self.ui.bill.text()
            o = self.ui.ord.text()
            args = (b,o)
            self.cur.callproc('generate_bill',args) 
            
            self.bill_popup()
        
        except mysql.connector.errors.DatabaseError:
            self.error_msg() 
        
        
        
        
    def showbill(self):
        query2 = "SELECT * FROM Bill" 
        self.cur.execute(query2)
        result=self.cur.fetchall()
        self.ui.billtable.setRowCount(len(result)) 
        for row_number, row_data in enumerate(result): 
                self.ui.billtable.insertRow(row_number) 
                for column_number, data in enumerate(row_data): 
                    self.ui.billtable.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        main_win = MainWindow()
        main_win.main_win.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)


