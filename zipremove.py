import zipfile
import os
import sys
import tempfile

def filter_and_repack_zip(zip_path):
    # Temporary directory to hold the contents we want to keep
    temp_dir = tempfile.TemporaryDirectory()
    new_zip_path = os.path.join(temp_dir.name, 'new_archive.zip')

    with zipfile.ZipFile(zip_path, 'r') as original_zip:
        with zipfile.ZipFile(new_zip_path, 'w') as new_zip:
            for file in original_zip.namelist():
                # Conditions for keeping the file
                if "(USA" in file or "(USA, Europe)" in file:
                    new_zip.writestr(file, original_zip.read(file))

    # Replace the original zip file with the new one
    os.replace(new_zip_path, zip_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <zip_file_path>")
        sys.exit(1)
    
    zip_file_path = sys.argv[1]
    filter_and_repack_zip(zip_file_path)
    print(f"Processed {zip_file_path}")
