import sys
import zipfile
import os
from pathlib import Path

def unzip_files(directory_path):
    for zip_file in Path(directory_path).glob('*.zip'):
        folder_name = zip_file.stem  # Get the file name without the .zip extension
        output_dir = zip_file.parent / folder_name  # Path for the output directory
        os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(output_dir)
            print(f"Extracted {zip_file.name} to {output_dir}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_directory_with_zip_files>")
        sys.exit(1)

    directory_path = sys.argv[1]
    unzip_files(directory_path)
