import os

directory_path = 'C:/Users/zenab/OneDrive/'  # Change this to ur desired file path
old_name = "main.py" # Name of file to be renamed
new_name = "test.py" # Change to ur liking

old_file = os.path.join(directory_path, old_name)
new_file = os.path.join(directory_path, new_name)

if(os.path.exists(old_file)):
    if(os.path.isfile(old_file)):
        try:
            os.rename(old_file, new_file)
            print(f"Renamed '{old_name}' to '{new_name}' in '{directory_path}'")
        except PermissionError:
            print("Permission denied. Cannot rename the file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print(f"'{old_file}' exists but is not a file.")
else:
    print("File not found")
