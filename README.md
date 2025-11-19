# File Renamer Script 🔤

A simple yet effective Python script designed to automate the renaming of files within a specified directory. This tool streamlines the process of renaming files, providing error handling for common issues like missing files or permission restrictions. It's perfect for automating file management tasks in various workflows.

## 🚀 Features

- **Automated File Renaming:** Simplifies the process of renaming files with a single script.
- **Configurable Parameters:** Easily set the directory path, old file name, and new file name.
- **Error Handling:** Gracefully handles `PermissionError` and other exceptions during renaming.
- **File Existence Check:** Verifies that the file exists before attempting to rename it.
- **File Type Check:** Ensures that the path is a file and not a directory before renaming.
- **Platform-Independent:** Uses `os.path.join` for cross-platform path handling.
- **Clear Output Messages:** Provides informative messages about the success or failure of the renaming operation.

## 🛠️ Tech Stack

- **Programming Language:** Python 🐍
- **Core Library:** `os` (for file system interactions)

## 📦 Installation

### Prerequisites

- Python 3.6 or higher installed on your system.

### Installation

1.  Clone the repository (if applicable):

    ```bash
    git clone [your_repo_url]
    cd [your_repo_directory]
    ```

2.  No additional packages are required as it uses the built-in `os` module.

## 💻 Usage

1.  **Update the script:** Open `renamer.py` and modify the following variables:

    -   `directory_path`: Set this to the directory containing the file you want to rename.
    -   `old_name`: Set this to the current name of the file.
    -   `new_name`: Set this to the desired new name for the file.

    ```python
    directory_path = "/path/to/your/directory"
    old_name = "old_file_name.txt"
    new_name = "new_file_name.txt"
    ```

2.  **Run the script:**

    ```bash
    python renamer.py
    ```

3.  **Check the output:** The script will print a message indicating whether the renaming was successful, if the file was not found, or if an error occurred.

## 📂 Project Structure

```
.
├── renamer.py    # The main Python script for renaming files
└── README.md     # Documentation for the project
```

## 📸 Screenshots

<img src="screenshot\Screenshot 2025-11-19 194718.png" alt="Screenshot of the script running" width="700"/>

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## 📬 Contact

If you have any questions or suggestions, feel free to reach out:

zenabadnan10@gmail.com

## 💖 Thanks Message

Thank you for checking out this simple file renaming script! We hope it helps streamline your file management tasks.

