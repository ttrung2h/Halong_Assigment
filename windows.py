import sys
from PySide6 import QtCore, QtWidgets, QtGui


class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()

        self.setWindowTitle("Login Window")
        self.setGeometry(300, 300, 300, 150)

        self.username_label = QtWidgets.QLabel("Username:")
        self.password_label = QtWidgets.QLabel("Password:")
        self.username_input = QtWidgets.QLineEdit()
        self.password_input = QtWidgets.QLineEdit()
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button = QtWidgets.QPushButton("Login")
        self.error_label = QtWidgets.QLabel("")
        self.error_label.setStyleSheet("color: red")

        layout = QtWidgets.QVBoxLayout(self)
        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow(self.username_label, self.username_input)
        form_layout.addRow(self.password_label, self.password_input)
        layout.addLayout(form_layout)
        layout.addWidget(self.login_button)
        layout.addWidget(self.error_label)

        self.login_button.clicked.connect(self.on_login_button_clicked)

    def on_login_button_clicked(self):
        #Get data from input bar
        username = self.username_input.text()
        password = self.password_input.text()

    

# class StaffWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super(StaffWindow, self).__init__()

#         self.setWindowTitle("Staff Management Window")
#         self.setGeometry(200, 200, 400, 200)  

#         self.layout = QtWidgets.QVBoxLayout(self)
#         # label = QtWidgets.QLabel("Staff Window Content", alignment=QtCore.Qt.AlignCenter)
#         # self.layout.addWidget(label)

#         self.create_buttons()    
#         self.connect_buttons()
#     def create_buttons(self):
#         self.back_button = QtWidgets.QPushButton("Back", self)
#         self.layout.addWidget(self.back_button, alignment=QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

#     def connect_buttons(self):
#         self.back_button.clicked.connect(self.on_clicked_back_button)
    
#     def on_clicked_back_button(self):
#         self.main_window = MainWindow()
#         self.destroy()
#         self.main_window.show()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Qt for Python Window with Buttons")
        self.setGeometry(100, 100, 400, 200)  
        self.text = QtWidgets.QLabel("Hello World",alignment=QtCore.Qt.AlignCenter)
        # Create a central widget and set it as the main window's central widget
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        # Layout setting
        self.layout = QtWidgets.QVBoxLayout(central_widget)
        self.layout.addWidget(self.text)
   
        #Create buttons
        self.create_buttons()
        
        #Connect function of button
        self.connect_button()
   
   
    def create_buttons(self):
        # Create three buttons and add them to the layout
        self.staff_button = QtWidgets.QPushButton("Staff management", self)
        self.product_button = QtWidgets.QPushButton("Exportation", self)
        self.storage_button = QtWidgets.QPushButton("Storage manage", self)
        self.list_buttons = [self.staff_button,self.product_button,self.storage_button]

        for button in self.list_buttons:
            self.layout.addWidget(button)

    def connect_button(self):
        self.staff_button.clicked.connect(self.on_clicked_staff_button)
        self.product_button.clicked.connect(self.on_clicked_product_button)
        self.storage_button.clicked.connect(self.on_clicked_storage_button)
    
    def on_clicked_staff_button(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.destroy()
    
    def on_clicked_product_button(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.destroy()
    
    def on_clicked_storage_button(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.destroy()
    
