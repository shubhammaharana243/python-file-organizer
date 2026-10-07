# 📁 Smart File Organizer

A simple and practical **Python-based File Organizer** that automatically organizes files into categorized folders based on their file extensions.

Instead of manually sorting hundreds of files, this tool can organize them into categories such as **Images, Documents, Videos, Music, Archives, Code, and Applications**.

It also includes a **file search feature** and an **Undo Organization** option to restore files to their original locations.

---

## ✨ Features

- 📂 **Automatic File Organization**
  - Sorts files into folders according to their extensions.

- 🔎 **File Search**
  - Search for files by name across the selected folder and its subfolders.

- ↩️ **Undo Organization**
  - Restore organized files back to their original locations.

- 🛡️ **Duplicate File Name Handling**
  - Prevents files from being overwritten by automatically generating unique filenames such as:
    `photo_1.jpg`, `photo_2.jpg`, etc.

- 📊 **Organization Summary**
  - Shows the number of files organized and categories created.

- 🧹 **Automatic Empty Folder Removal**
  - Empty category folders are removed when an organization is undone.

- ⚡ **Simple CLI Interface**
  - Easy-to-use terminal-based menu.

- 🎬 **Loading Animation**
  - Provides a simple visual animation during organization and search operations.

---

## 🗂️ Supported Categories

| Category | Example Extensions |
|---|---|
| 🖼️ Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`, `.svg`, `.bmp`, `.ico`, `.tiff` |
| 📄 Documents | `.pdf`, `.doc`, `.docx`, `.txt`, `.rtf`, `.odt`, `.xls`, `.xlsx`, `.csv`, `.ppt`, `.pptx` |
| 🎬 Videos | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`, `.webm`, `.m4v`, `.3gp` |
| 🎵 Music | `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.m4a`, `.wma`, `.opus` |
| 📦 Archives | `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`, `.xz` |
| 💻 Code | `.py`, `.js`, `.html`, `.css`, `.java`, `.c`, `.cpp`, `.php`, `.sql`, `.json`, `.xml`, `.yaml`, `.ts`, `.tsx`, `.jsx` |
| ⚙️ Applications | `.exe`, `.msi`, `.appx`, `.apk`, `.deb`, `.rpm` |

Files with unsupported extensions are placed into an **Others** category.

---

## 🖥️ How It Works

The program provides three main options:

```text
========================================
       SMART FILE ORGANIZER
========================================

[1]  Organize Files
[2]  Search File
[3]  Exit
```

### 1️⃣ Organize Files

Enter the path of the folder you want to organize.

The program:

1. Scans the selected folder.
2. Checks each file's extension.
3. Determines its category.
4. Creates the required category folder.
5. Moves the file into that folder.
6. Handles duplicate filenames automatically.
7. Keeps a history of the changes so the operation can be undone.

The organizer uses Python's `pathlib` and `shutil` for file handling and movement.

---

### 2️⃣ Search Files

You can search for a file by entering part or all of its filename.

The search scans the selected directory recursively, including its subfolders.

Example:

```text
Enter filename to search: project

Search Results:

[1] project.py -> C:\Users\...\Code\project.py
[2] project.pdf -> C:\Users\...\Documents\project.pdf
```

The search is case-insensitive and uses recursive file searching.

---

### 3️⃣ Undo Organization

After organizing files, the program asks whether you want to undo the operation.

```text
Want to undo? (Y/N)
```

If you choose **Y**, the files are moved back to their original locations.

Empty category folders are also removed automatically.

---

## 🧠 Project Structure

The project follows a simple class-based structure:

```text
File Organizer
│
├── FileClassifier
│   └── Determines the category of a file
│
├── FileOrganizer
│   ├── Organizes files
│   ├── Handles duplicate names
│   └── Stores operation history
│
├── FileUndo
│   └── Restores files to original locations
│
├── FileSearcher
│   └── Searches files recursively
│
└── CLI Functions
    ├── Menu
    ├── Organization interface
    ├── Search interface
    └── Undo interface
```

---

## 🛠️ Technologies Used

- **Python 3**
- `pathlib` — File and directory path handling
- `shutil` — Moving files
- `time` — Animation timing
- `random` — Randomized loading animation

---

## 🚀 Getting Started

### Prerequisites

Make sure Python 3 is installed on your computer.

Check your Python version:

```bash
python --version
```

### Clone the Repository

```bash
git clone https://github.com/shubhammaharana243/python-file-organizer.git
```

Move into the project directory:

```bash
cd python-file-organizer
```

### Run the Program

```bash
python main.py
```

> Replace `main.py` with the actual Python filename if your file has a different name.

---

## ⚠️ Important

**Use this program on a test folder first.**

The organizer actually moves files from their original location into category folders. Although an undo feature is available, it is always safer to test the program with non-important files before using it on personal data.

---

## 📸 Demo

Add screenshots or a screen recording of the project here:

```text
Before → Organize → Categorized Folders → Search → Undo
```

You can also add your demo video/GIF here later.

---

## 🎯 Project Goal

The main goal of this project is to create a practical Python application that demonstrates:

- Object-Oriented Programming
- File and directory handling
- Automation
- File searching
- Exception-safe file organization concepts
- Data structures
- Modular program design

---

## 🔮 Future Improvements

Possible improvements for future versions:

- 🖥️ Graphical User Interface (GUI)
- ⚙️ Custom category configuration
- 📋 Detailed activity logs
- 🔄 Automatic folder monitoring
- 📅 Optional date-based organization
- ⚡ Batch processing
- 🎨 Modern desktop interface

---

## 👨‍💻 Author

**Shubham Maharana**

GitHub:  
https://github.com/shubhammaharana243

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!
