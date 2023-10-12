import os
import glob

# Specify the folder path where your .txt files are located
folder_path = "/path/to/your/folder"

# Use glob to get a list of .txt files in the folder
txt_files = glob.glob(os.path.join(folder_path, "*.txt"))

# Iterate over the list of .txt files
for txt_file in txt_files:
    # Open and read the contents of each .txt file
    with open(txt_file, 'r') as file:
        file_contents = file.read()
    
    # Process the file contents as needed
    # You can add your processing logic here

    # Print the file name and its contents as an example
    print("File:", txt_file)
    print("Contents:")
    print(file_contents)
    print("\n")

# You can add your specific processing logic for each .txt file in the loop
