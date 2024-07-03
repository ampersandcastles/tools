# Tools Collection

This repository contains a small collection of Python utilities aimed at making file handling tasks easier. These tools were created to ensure they are not lost and can be readily available for use or modification as needed. Below is a brief overview of each script included in this collection:

### 1. `sizegetter.py`
A script designed to retrieve and display the file size of specified files. It's useful for quickly checking the size of files without navigating through file properties manually.

### 2. `unzipdir.py`
This utility helps in extracting the contents of zip files. It's particularly handy when dealing with multiple zip files or when automating the extraction process in batch operations.

### 3. `zipremove.py`
A convenient tool for removing specified files from zip archives. This can be useful for cleaning up archives without the need to decompress and recompress them.

### 4. `zipsize`
This is a small bash script that should be piped through ```unzip -l file.zip``` I wanted a way to see a different size of files in the archive.


### 5. `packet.py`
A small packet I use for testing. ```scapy``` needed.

### 6. `cpp-project-gen.py`
A small script to generate a c++ project structure.

### 7. `lsblk.py`
This is not a direct clone of lsblk.c, this is a minimal reinterpretation for use on FreeBSD. It works in the sense that it functions. Maybe it'll get added to.

## Installation
No installation is necessary for these scripts. They are standalone Python scripts that can be run from the command line. Ensure you have Python installed on your system, navigate to the directory containing these scripts, and execute them with Python. For example:

```python3 unzipdir.py```

## Usage
Each script can be executed from the command line, with potential arguments depending on the script's design. Refer to each script's source code for detailed usage instructions.

