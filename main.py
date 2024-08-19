#Import modules
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QListWidget, QComboBox, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QFont, QPixmap
from PIL import Image, ImageFilter, ImageEnhance

class PictureQt(QWidget):
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

        # Connect signals
        self.select_folder_button.clicked.connect(self.get_working_directory)


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
        master_layout.addLayout(column1, 20) #adjust the stretch% of column 1
        master_layout.addLayout(column2, 80) #adjust the stretch% of column 2

        #set the master; in this case it is the master_row
        self.setLayout(master_layout)



    #ALL functionality
    #working_directoy = QFileDialog.getExistingDirectory()



    #Fliter files and extensions
    def filter(self, files, extensions):
        results = []
        #loop through every file in folders
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    results.append(file)
        return results #return the appended list


    #Choose current working directory
    def get_working_directory(self): #scan all dirs for files
        global working_directory #since it is defined outside
        working_directory = QFileDialog.getExistingDirectory() #get the user's working directory
        extensions = ["jpg","jpeg","png","svg"]
        file_names = self.filter(os.listdir(working_directory), extensions) #list dr is like ls command
        #load the files in the file_list widget but first ensure emptiness by clearing
        self.file_list.clear()
        #loop through file names, adding each instance to file_list widget
        for file in file_names:
            self.file_list.addItem(file)

class Editor(): #this class programs all of our buttons
    def __init__(self):
        self.image = None 
        self.original = None #holds the original image to allow us to revert changes 
        self.file_name = None  
        self.save_folder = "edits/" #new folder with the path as an extension to the current file path of the working dir 

    #methods to show, load and edit the images
    #load an image; load the filename so that we can use that filename to load into our program as image
    def load_image(self, filename):
        self.file_name = filename #override None to whatever we pass in as the second argument
        full_path = os.path.join(working_directory, filename)
        self.image = Image.open(full_path) #Open the image as a file
        self.original = self.image.copy() #save a copy for backup purposes
        
#entrypoint; show and run the app
if __name__ == "__main__":
    app = QApplication([]) #allows us to create and execute our app; takes in an empty list ALWAYS
    main_window = PictureQt() #object to create a new form (window) that we will be editing
    main_window.show() #display the main window form
    app.exec_() #run the app

 
#current -> https://youtu.be/f_9NBdSAo-g?t=10592