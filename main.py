#Import modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QComboBox, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QFont

class ImageEditor(QWidget):
    def __init__(self):
        super().__init__()

        #main app,create objects and settings as properties
        self.setWindowTitle("Photo Editor") #set window title 
        self.resize(900,800) #set window size

        #create all app objects(widgets)
        self.select_folder_button = QPushButton("Select Folder")
        self.file_list = QListWidget()

        self.left_button = QPushButton("Left")
        self.right_button = QPushButton("Right")
        self.mirror_button = QPushButton("Mirror")
        self.sharpness_button = QPushButton("Sharpness")
        self.bw_button = QPushButton("B/W")
        self.color_button = QPushButton("Color")
        self.contrast_button = QPushButton("Contrast")
        self.blur_button = QPushButton("Blur")

        #create dropdown box and add items to it
        self.filter_combo_box = QComboBox()
        self.filter_combo_box.addItem("Original") #to revert to original file
        self.filter_combo_box.addItem("Left")
        self.filter_combo_box.addItem("Right")
        self.filter_combo_box.addItem("Mirror")
        self.filter_combo_box.addItem("Sharpen")
        self.filter_combo_box.addItem("B/W")
        self.filter_combo_box.addItem("Color")
        self.filter_combo_box.addItem("Contrast")
        self.filter_combo_box.addItem("Blur")
        
        self.image_placeholder_label = QLabel("Image will appear here")

        #all design here
        master_layout = QHBoxLayout()
        column1 = QVBoxLayout()
        column2 = QVBoxLayout()

        #add widgets to column 1
        column1.addWidget(self.select_folder_button)
        column1.addWidget(self.file_list)
        column1.addWidget(self.filter_combo_box)
        column1.addWidget(self.left_button)
        column1.addWidget(self.right_button)
        column1.addWidget(self.mirror_button)
        column1.addWidget(self.sharpness_button)
        column1.addWidget(self.bw_button)
        column1.addWidget(self.color_button)
        column1.addWidget(self.contrast_button)
        column1.addWidget(self.blur_button)

        #add widgets to column 1
        column2.addWidget(self.image_placeholder_label)

        #concat the layouts
        master_layout.addLayout(column1, 20) #adjust the stretch of column 1
        master_layout.addLayout(column2, 80) #adjust the stretch of column 2

        #set the master; in this case it is the master_row
        self.setLayout(master_layout)



#entrypoint; show and run the app
if __name__ == "__main__":
    app = QApplication([]) #allows us to create and execute our app; takes in an empty list ALWAYS
    main_window = ImageEditor() #object to create a new form (window) that we will be editing
    main_window.show() #display the main window form
    app.exec_() #run the app


#current -> https://youtu.be/f_9NBdSAo-g?t=7689