# 📦 User Image Editor

**User Image Editor** 🖼️ — a user-friendly Python application built with PyQt5 and Pillow (PIL) for basic image editing tasks.

## 📝 Features

- **📂 Browse and Select:** Easily navigate your file system to select an image.
- **🔄 Real-time Previews:** See the effects of your edits instantly.
- **✨ Image Transformations:**
  - Rotate left and right
  - Flip horizontally (mirror)
- **🎨 Image Enhancements:**
  - Convert to black and white
  - Adjust sharpness
  - Modify contrast
  - Apply blur
- **💾 Save Edits:** Store your modified images in a dedicated `edits` folder.

## 🚀 Getting Started

### 1️⃣ Prerequisites

Make sure you have the following installed:

- 🐍 Python 3
- 🖼️ Pillow (PIL):
  ```
  pip install pillow
  ```
- 🎨 PyQt5:
  ```
  pip install pyqt5
  ```

### 2️⃣ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/user_image_editor.git
cd user_image_editor
```

Run the application:

```bash
python main.py
```

### 3️⃣ Usage

- **Select Folder:** Click "Select Folder" to choose the directory containing your images.
- **Choose Image:** Select an image from the file list.
- **Apply Edits:** Use the buttons to apply desired image transformations and enhancements.
- **View Results:** Your edited image will be displayed in real-time.
- **Exit:** Click "Exit" to close the application.

## 📂 File Structure

- `main.py`: Core application logic, UI setup, and image editing functions.
- `pil_playground.py`: (Optional) A file for experimenting with Pillow (PIL) image editing techniques.
- `edits/`: Folder automatically created to store your edited images.

## 🧑‍💻 Example

1. Select an image of a cute kitten. 🐱
2. Apply a blur to create a dreamy effect. ✨
3. Rotate the image to find the perfect angle. 🔄
4. Save your masterpiece! 💾

## ⚠️ Notes

- The application currently supports common image formats like JPG, JPEG, PNG, and SVG.
- Ensure that you have write permissions in the directory where the application is running to allow for the creation of the `edits` folder.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ❤️ Contributions

Feel free to submit pull requests or raise issues. Contributions are always welcome! Some ideas:

- Implement additional image editing features (e.g., cropping, resizing, color adjustments).
- Enhance the user interface with more advanced controls and options.
- Add support for more image file formats.

---
## 👤 Author

Sean Njela 
GitHub: https://github.com/sean-njela
