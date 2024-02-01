import os
import sys

def calculate_id(file_name):
    hex_string = file_name[:8]
    identifier = int(hex_string, 16)
    
    return identifier

def read_sav_files(directory):
    sav_files = [f for f in os.listdir(directory) if f.endswith('.sav')]
    
    if not sav_files:
        print("No .sav files found in the directory.")
        return
    
    for file in sav_files:
        file_path = os.path.join(directory, file)
        identifier = calculate_id(file)
        print(f"File name: {file}, Calculated ID: {identifier}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py /path/to/your/folder")
        sys.exit(1)

    directory_path = sys.argv[1]
    if not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        sys.exit(1)

    read_sav_files(directory_path)
