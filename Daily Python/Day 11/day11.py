😷Stuck at home? Enjoy free courses, on us →

Reading and Writing Files in Python (Guide)
Reading and Writing Files in Python (Guide)
by James Mertz 14 Comments  intermediate python

Tweet Share Email
Table of Contents

What Is a File?
File Paths
Line Endings
Character Encodings
Opening and Closing a File in Python
Text File Types
Buffered Binary File Types
Raw File Types
Reading and Writing Opened Files
Iterating Over Each Line in the File
Working With Bytes
A Full Example: dos2unix.py
Tips and Tricks
__file__
Appending to a File
Working With Two Files at the Same Time
Creating Your Own Context Manager
Don’t Re-Invent the Snake
You’re a File Wizard Harry!

 Watch Now This tutorial has a related video course created by the Real Python team. Watch it together with the written tutorial to deepen your understanding: Reading and Writing Files in Python

One of the most common tasks that you can do with Python is reading and writing files. Whether it’s writing to a simple text file, reading a complicated server log, or even analyzing raw byte data, all of these situations require reading or writing a file.

In this tutorial, you’ll learn:

What makes up a file and why that’s important in Python
The basics of reading and writing files in Python
Some basic scenarios of reading and writing files
This tutorial is mainly for beginner to intermediate Pythonistas, but there are some tips in here that more advanced programmers may appreciate as well.

Free Bonus: Click here to get our free Python Cheat Sheet that shows you the basics of Python 3, like working with data types, dictionaries, lists, and Python functions.

 Take the Quiz: Test your knowledge with our interactive “Reading and Writing Files in Python” quiz. Upon completion you will receive a score so you can track your learning progress over time:



 Remove ads
What Is a File?
Before we can go into how to work with files in Python, it’s important to understand what exactly a file is and how modern operating systems handle some of their aspects.

At its core, a file is a contiguous set of bytes used to store data. This data is organized in a specific format and can be anything as simple as a text file or as complicated as a program executable. In the end, these byte files are then translated into binary 1 and 0 for easier processing by the computer.

Files on most modern file systems are composed of three main parts:

Header: metadata about the contents of the file (file name, size, type, and so on)
Data: contents of the file as written by the creator or editor
End of file (EOF): special character that indicates the end of the file
The file format with the header on top, data contents in the middle and the footer on the bottom.

What this data represents depends on the format specification used, which is typically represented by an extension. For example, a file that has an extension of .gif most likely conforms to the Graphics Interchange Format specification. There are hundreds, if not thousands, of file extensions out there. For this tutorial, you’ll only deal with .txt or .csv file extensions.

File Paths
When you access a file on an operating system, a file path is required. The file path is a string that represents the location of a file. It’s broken up into three major parts:

Folder Path: the file folder location on the file system where subsequent folders are separated by a forward slash / (Unix) or backslash \ (Windows)
File Name: the actual name of the file
Extension: the end of the file path pre-pended with a period (.) used to indicate the file type
Here’s a quick example. Let’s say you have a file located within a file structure like this:

/
│
├── path/
|   │
│   ├── to/
│   │   └── cats.gif
│   │
│   └── dog_breeds.txt
|
└── animals.csv
Let’s say you wanted to access the cats.gif file, and your current location was in the same folder as path. In order to access the file, you need to go through the path folder and then the to folder, finally arriving at the cats.gif file. The Folder Path is path/to/. The File Name is cats. The File Extension is .gif. So the full path is path/to/cats.gif.

Now let’s say that your current location or current working directory (cwd) is in the to folder of our example folder structure. Instead of referring to the cats.gif by the full path of path/to/cats.gif, the file can be simply referenced by the file name and extension cats.gif.

/
│
├── path/
|   │
|   ├── to/  ← Your current working directory (cwd) is here
|   │   └── cats.gif  ← Accessing this file
|   │
|   └── dog_breeds.txt
|
└── animals.csv
But what about dog_breeds.txt? How would you access that without using the full path? You can use the special characters double-dot (..) to move one directory up. This means that ../dog_breeds.txt will reference the dog_breeds.txt file from the directory of to:

/
│
├── path/  ← Referencing this parent folder
|   │
|   ├── to/  ← Current working directory (cwd)
|   │   └── cats.gif
|   │
|   └── dog_breeds.txt  ← Accessing this file
|
└── animals.csv
The double-dot (..) can be chained together to traverse multiple directories above the current directory. For example, to access animals.csv from the to folder, you would use ../../animals.csv.

Line Endings

"""
A simple script and library to convert files or strings from dos like
line endings with Unix like line endings.
"""

import argparse
import os


def str2unix(input_str: str) -> str:
    r"""
    Converts the string from \r\n line endings to \n

    Parameters
    ----------
    input_str
        The string whose line endings will be converted

    Returns
    -------
        The converted string
    """
    r_str = input_str.replace('\r\n', '\n')
    return r_str


def dos2unix(source_file: str, dest_file: str):
    """
    Converts a file that contains Dos like line endings into Unix like

    Parameters
    ----------
    source_file
        The path to the source file to be converted
    dest_file
        The path to the converted file for output
    """
    # NOTE: Could add file existence checking and file overwriting
    # protection
    with open(source_file, 'r') as reader:
        dos_content = reader.read()

    unix_content = str2unix(dos_content)

    with open(dest_file, 'w') as writer:
        writer.write(unix_content)


if __name__ == "__main__":
    # Create our Argument parser and set its description
    parser = argparse.ArgumentParser(
        description="Script that converts a DOS like file to an Unix like file",
    )

    # Add the arguments:
    #   - source_file: the source file we want to convert
    #   - dest_file: the destination where the output should go

    # Note: the use of the argument type of argparse.FileType could
    # streamline some things
    parser.add_argument(
        'source_file',
        help='The location of the source '
    )

    parser.add_argument(
        '--dest_file',
        help='Location of dest file (default: source_file appended with `_unix`',
        default=None
    )

    # Parse the args (argparse automatically grabs the values from
    # sys.argv)
    args = parser.parse_args()

    s_file = args.source_file
    d_file = args.dest_file

    # If the destination file wasn't passed, then assume we want to
    # create a new file based on the old one
    if d_file is None:
        file_path, file_extension = os.path.splitext(s_file)
        d_file = f'{file_path}_unix{file_extension}'

    dos2unix(s_file, d_file)