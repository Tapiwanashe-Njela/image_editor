#Import modules
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QListWidget, QMessageBox, QComboBox, QLabel, QSizePolicy, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QFont, QPixmap#allows us to load images into PyQt
from PIL import Image, ImageFilter, ImageEnhance

class PictureQt(QWidget):
    def __init__(self):
        print("PictureQt class initialising")
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
        self.original_image_button = QPushButton("Original Image")
        self.contrast_button = QPushButton("Contrast")
        self.blur_button = QPushButton("Blur")
        self.exit_button = QPushButton("Exit")


        #create dropdown box and add items to it
        self.filter_combo_box = QComboBox()
        self.filter_combo_box.addItem("Original") #to revert to original file
        self.filter_combo_box.addItem("Left")
        self.filter_combo_box.addItem("Right")
        self.filter_combo_box.addItem("Mirror")
        self.filter_combo_box.addItem("Sharpen")
        self.filter_combo_box.addItem("B/W")
        self.filter_combo_box.addItem("original_image")
        self.filter_combo_box.addItem("Contrast")
        self.filter_combo_box.addItem("Blur")
        
        self.image_placeholder_label = QLabel("Image will appear here")


        # Connect signals
        self.exit_button.clicked.connect(self.close)
        self.select_folder_button.clicked.connect(self.get_working_directory)
        self.file_list.currentRowChanged.connect(self.display_image) #when we click another item in the list(i.e changing the row)
        self.bw_button.clicked.connect(main.black_and_white)
        self.left_button.clicked.connect(main.left)
        self.right_button.clicked.connect(main.right)
        self.original_image_button.clicked.connect(main.original_image)
        self.mirror_button.clicked.connect(main.mirror)
        self.sharpness_button.clicked.connect(main.sharpness)
        self.contrast_button.clicked.connect(main.contrast)
        self.blur_button.clicked.connect(main.blur)


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
        column1.addWidget(self.original_image_button)
        column1.addWidget(self.contrast_button)
        column1.addWidget(self.blur_button)
        column1.addWidget(self.exit_button)


        #add widgets to column 1
        column2.addWidget(self.image_placeholder_label)

        #concat the layouts
        master_layout.addLayout(column1, 20) #adjust the stretch% of column 1
        master_layout.addLayout(column2, 80) #adjust the stretch% of column 2

        #set the master; in this case it is the master_row
        self.setLayout(master_layout)
    

        #Disable buttons before picture selection
        self.disable_buttons() 

    
    #ALL functionalitty
    def disable_buttons(self):
        print("disable-buttons")
        self.left_button.setEnabled(False)
        self.right_button.setEnabled(False)
        self.mirror_button.setEnabled(False)
        self.sharpness_button.setEnabled(False)
        self.bw_button.setEnabled(False)
        self.original_image_button.setEnabled(False)
        self.contrast_button.setEnabled(False)
        self.blur_button.setEnabled(False)


    def enable_buttons(self):
        print("enable_buttons")
        self.left_button.setEnabled(True)
        self.right_button.setEnabled(True)
        self.mirror_button.setEnabled(True)
        self.sharpness_button.setEnabled(True)
        self.bw_button.setEnabled(True)
        self.original_image_button.setEnabled(True)
        self.contrast_button.setEnabled(True)
        self.blur_button.setEnabled(True)


    #Fliter files and extensions
    def filter(self, files, extensions):
        print("filter")
        results = []
        #loop through every file in folders
        for file in files:
            for ext in extensions:
                if file.endswith(ext):
                    results.append(file)
        return results #return the appended list


    #Choose current working directory
    def get_working_directory(self): #scan all dirs for files
        print("get_working_directory")
        global working_directory #To also define outside
        working_directory = QFileDialog.getExistingDirectory() #get the user's working directory

        # Check if a valid directory is selected
        if not working_directory:  # If the user cancels the dialog, working_directory will be an empty string.
            print("No directory selected, returning...")
            return
    
        extensions = ["jpg","jpeg","png","svg"]
        file_names = self.filter(os.listdir(working_directory), extensions) #listdir is like ls command
        
        #load the files in the file_list widget but first ensure emptiness by clearing
        self.file_list.clear()

        if not file_names:  # No images found in the directory.
            QMessageBox.information(self, "No Images", "The selected folder contains no supported image files.")
        else:
            for file in file_names:
                self.file_list.addItem(file)
        
        #loop through file names, adding each instance to file_list widget
        for file in file_names:
            self.file_list.addItem(file)


    #function to always display the image we click from our file list; connects with row change event
    def display_image(self):
        print("display_image")
        if main_window.file_list.currentRow() >= 0: #check if we have values in the file list
            file_name = main_window.file_list.currentItem().text()#get the text value of the item that we click in the filelist
            main.load_image(file_name)
            main.show_image(os.path.join(working_directory, main.file_name)) 
            self.enable_buttons() #enable button functionality after image click


    #handle exiting without Saving Changes
    def closeEvent(self, event):
        if main.is_image_selected and main.is_image_modified: #only run if image has been selected and modified
            
            reply = QMessageBox.question(self, "Exit", "Do you want to save your changes before exiting?", 
                                        QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

            if reply == QMessageBox.Yes:
                main.save_image()
                event.accept()
            elif reply == QMessageBox.No:
                # Only delete if the image was saved
                if main.is_image_saved:
                    saved_image_path = os.path.join(working_directory, main.save_folder, main.file_name)
                    try:
                        if os.path.exists(saved_image_path):
                            os.remove(saved_image_path)
                            print(f"Deleted saved image: {saved_image_path}")
                        else:
                            print("No saved image to delete.")
                    except Exception as e:
                        QMessageBox.warning(self, "Error", f"Failed to delete image: {e}")
                event.accept()
            else:
                event.ignore()

class Editor(): #this class provides the functionality of our app.
    def __init__(self):
        print("Editor class initialising")
        self.image = None 
        self.original = None #holds the original image to allow us to revert changes
        self.file_name = None  
        self.save_folder = "edits/" #new folder with the path as an extension to the current file path of the working dir
        self.is_image_saved = False  # Track if the image was saved
        self.is_image_selected = False  # Track if an image has been selected
        self.is_image_modified = False   # Track if the image has been modified

    #check to Ensure an Image is Selected in every image manipulation method
    def ensure_image_loaded(self):
        if not self.image:
            QMessageBox.warning(main_window, "No Image", "Please select an image first.")
            return False
        return True

    #methods to show, load and edit the images
    #load an image; load the filename so that we can use that filename to load into our program as image
    def load_image(self, filename):
        print("load_image")
        self.file_name = filename #override None to whatever we pass in as the second argument
        full_path = os.path.join(working_directory, filename)

        #handle Invalid Image Files or Corrupt Files
        try:
            self.image = Image.open(full_path)
            self.original = self.image.copy()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Unable to open image: {e}")
            self.image = None
            self.original = None
        
        self.image = Image.open(full_path) #Open the image as a file
        self.original = self.image.copy() #save a copy before edits for backup purposes


    def save_image(self): #to save to our self.save_folder under edits/
        print("save_image")
        path = os.path.join(working_directory, self.save_folder) #path to our save folder

        #Handle Save Folder Creation Errors
        try: 
            if not (os.path.exists(path)): #run if path doesn't exist already
                os.mkdir(path) #create a directory if path doesn't exist
        except OSError as e:
            QMessageBox.critical(main_window, "Error", f"Failed to create save folder: {e}")
            return
        
        full_path = os.path.join(path, self.file_name) #to get full path of the new path

        try:
            self.image.save(full_path) #save new path
            self.is_image_saved = True  # Mark that the image has been saved
        except Exception as e:
            QMessageBox.critical(main_window, "Error", f"Failed to save image: {e}")
    

    def show_image(self, path):
        print("show_image")
        main_window.image_placeholder_label.hide() #hide the label from the screen; to be replaced by the picture
        image = QPixmap(path) #Obj creation allowing us to load images into PyQt; takes in a path to the image and converts
        width, height = main_window.image_placeholder_label.width(), main_window.image_placeholder_label.height() #get LxW dims of label to be replaced
        image = image.scaled(width, height, Qt.KeepAspectRatio) #scale up the image to the LxW; + prevent it from being distorted using Qt
        main_window.image_placeholder_label.setPixmap(image) #set an image to a Qt widget 
        main_window.image_placeholder_label.setAlignment(Qt.AlignCenter) #set alignment of the label to be replaced to the center
        main_window.image_placeholder_label.show() #then show to screen after


    def black_and_white(self):
        if not self.ensure_image_loaded():
            return
        print("black and white")
        self.image = self.image.convert("L")
        self.is_image_modified = True  # Mark as modified
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.file_name)
        main_window.image_placeholder_label.hide()
        self.show_image(image_path)


    def left(self):
        if not self.ensure_image_loaded():
            return
        print("left")
        self.image = self.image.transpose(Image.ROTATE_90)
        #the next lines will be repeated
        self.is_image_modified = True  # Mark as modified
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.file_name)
        main_window.image_placeholder_label.hide()
        self.show_image(image_path)


    def right(self):
        if not self.ensure_image_loaded():
            return
        print("right")
        self.image = self.image.transpose(Image.ROTATE_270)
        #the next lines will be repeated
        self.is_image_modified = True  # Mark as modified
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.file_name)
        main_window.image_placeholder_label.hide()
        self.show_image(image_path)


    def original_image(self):
        if not self.ensure_image_loaded():
            return
        print("original_image")
        self.image = self.original.copy()
        #the next lines will be repeated
        self.is_image_modified = True  # Mark as modifiedd
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.file_name)
        main_window.image_placeholder_label.hide()
        self.show_image(image_path)


    def mirror(self):
        if not self.ensure_image_loaded():
            return
        print("mirror")
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        #the next lines will be repeated
        self.is_image_modified = True  # Mark as modified
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.file_name)
        main_window.image_placeholder_label.hide()
        self.show_image(image_path)


    def sharpness(self):
        if not self.ensure_image_loaded():
            return
        print("sharpness")
        self.image = self.image.filter(ImageFilter.SHARPEN) 
        #the next lines will be repeated
        self.is_image_modified = True  # Mark as modified
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.file_name)
        main_window.image_placeholder_label.hide()
        self.show_image(image_path)


    def contrast(self):
        if not self.ensure_image_loaded():
            return
        print("contrast")
        self.image = ImageEnhance.Contrast(self.image).enhance(1.2)
        #the next lines will be repeated
        self.is_image_modified = True  # Mark as modified
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.file_name)
        main_window.image_placeholder_label.hide()
        self.show_image(image_path)


    def blur(self):
        if not self.ensure_image_loaded():
            return
        print("blur")
        self.image = self.image.filter(ImageFilter.BLUR) 
        #the next lines will be repeated
        self.is_image_modified = True  # Mark as modified
        self.save_image()
        image_path = os.path.join(working_directory, self.save_folder, self.file_name)
        main_window.image_placeholder_label.hide()
        self.show_image(image_path)


    #functionality of the filter box
    #we want to use lamda functions for all selections in the dropdown box, except for Original 
    #lamda functions are runtime functions; created to run at the time of creation only
    #apply_filter is a method that encapsulates all the lamda functions in the drop box
    #filter_name arg saves the text value of the selection made in the filter box 
    def apply_filter(self, filter_name):
        print("apply_filter")
        if filter_name == "Original":
            self.image = self.original.copy()
        else:
            print()


#entrypoint; show and run the app
if __name__ == "__main__":
    print("running")
    app = QApplication([]) #allows us to create and execute our app; takes in an empty list ALWAYS
    main = Editor() #obj of Editor class
    main_window = PictureQt() #object to create a new form (window) that we will be editing
    main_window.show() #display the main window form
    app.exec_() #run the app

 
#current -> https://youtu.be/f_9NBdSAo-g?t=11617