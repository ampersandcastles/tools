import zipfile
import os
import sys
import tempfile
from pathlib import Path
import shutil

def filter_and_repack_zip(zip_path):
    temp_dir = tempfile.TemporaryDirectory()
    new_zip_path = os.path.join(temp_dir.name, 'new_archive.zip')

    with zipfile.ZipFile(zip_path, 'r') as original_zip:
        with zipfile.ZipFile(new_zip_path, 'w') as new_zip:
            for file in original_zip.namelist():
                if "(USA" in file or "(USA, Europe)" in file:
                    new_zip.writestr(file, original_zip.read(file))
                else:
                    print(f"Removing {file} from {zip_path}")

    # Remove the original file and move the new file to the original location
    os.remove(zip_path)
    shutil.move(new_zip_path, zip_path)

def process_directory(directory_path):
    for zip_file in Path(directory_path).glob('*.zip'):
        print(f"Processing {zip_file}")
        filter_and_repack_zip(zip_file)
    print("All ZIP files processed.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_directory_or_zip>")
        sys.exit(1)
    
    path = sys.argv[1]
    if os.path.isdir(path):
        process_directory(path)
    elif os.path.isfile(path) and path.endswith('.zip'):
        print(f"Processing {path}")
        filter_and_repack_zip(path)
    else:
        print("The path is not a directory or a ZIP file.")
