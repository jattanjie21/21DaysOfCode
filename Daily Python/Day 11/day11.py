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
One problem often encountered when working with file data is the representation of a new line or line ending. The line ending has its roots from back in the Morse Code era, when a specific pro-sign was used to communicate the end of a transmission or the end of a line.

Later, this was standardized for teleprinters by both the International Organization for Standardization (ISO) and the American Standards Association (ASA). ASA standard states that line endings should use the sequence of the Carriage Return (CR or \r) and the Line Feed (LF or \n) characters (CR+LF or \r\n). The ISO standard however allowed for either the CR+LF characters or just the LF character.

Windows uses the CR+LF characters to indicate a new line, while Unix and the newer Mac versions use just the LF character. This can cause some complications when you’re processing files on an operating system that is different than the file’s source. Here’s a quick example. Let’s say that we examine the file dog_breeds.txt that was created on a Windows system:

Pug\r\n
Jack Russell Terrier\r\n
English Springer Spaniel\r\n
German Shepherd\r\n
Staffordshire Bull Terrier\r\n
Cavalier King Charles Spaniel\r\n
Golden Retriever\r\n
West Highland White Terrier\r\n
Boxer\r\n
Border Terrier\r\n
This same output will be interpreted on a Unix device differently:

Pug\r
\n
Jack Russell Terrier\r
\n
English Springer Spaniel\r
\n
German Shepherd\r
\n
Staffordshire Bull Terrier\r
\n
Cavalier King Charles Spaniel\r
\n
Golden Retriever\r
\n
West Highland White Terrier\r
\n
Boxer\r
\n
Border Terrier\r
\n
This can make iterating over each line problematic, and you may need to account for situations like this.


 Remove ads
Character Encodings
Another common problem that you may face is the encoding of the byte data. An encoding is a translation from byte data to human readable characters. This is typically done by assigning a numerical value to represent a character. The two most common encodings are the ASCII and UNICODE Formats. ASCII can only store 128 characters, while Unicode can contain up to 1,114,112 characters.

ASCII is actually a subset of Unicode (UTF-8), meaning that ASCII and Unicode share the same numerical to character values. It’s important to note that parsing a file with the incorrect character encoding can lead to failures or misrepresentation of the character. For example, if a file was created using the UTF-8 encoding, and you try to parse it using the ASCII encoding, if there is a character that is outside of those 128 values, then an error will be thrown.

Opening and Closing a File in Python
When you want to work with a file, the first thing to do is to open it. This is done by invoking the open() built-in function. open() has a single required argument that is the path to the file. open() has a single return, the file object:

file = open('dog_breeds.txt')
After you open a file, the next thing to learn is how to close it.

Warning: You should always make sure that an open file is properly closed.

It’s important to remember that it’s your responsibility to close the file. In most cases, upon termination of an application or script, a file will be closed eventually. However, there is no guarantee when exactly that will happen. This can lead to unwanted behavior including resource leaks. It’s also a best practice within Python (Pythonic) to make sure that your code behaves in a way that is well defined and reduces any unwanted behavior.

When you’re manipulating a file, there are two ways that you can use to ensure that a file is closed properly, even when encountering an error. The first way to close a file is to use the try-finally block:

reader = open('dog_breeds.txt')
try:
    # Further file processing goes here
finally:
    reader.close()
If you’re unfamiliar with what the try-finally block is, check out Python Exceptions: An Introduction.

The second way to close a file is to use the with statement:

with open('dog_breeds.txt') as reader:
    # Further file processing goes here
The with statement automatically takes care of closing the file once it leaves the with block, even in cases of error. I highly recommend that you use the with statement as much as possible, as it allows for cleaner code and makes handling any unexpected errors easier for you.

Most likely, you’ll also want to use the second positional argument, mode. This argument is a string that contains multiple characters to represent how you want to open the file. The default and most common is 'r', which represents opening the file in read-only mode as a text file:

with open('dog_breeds.txt', 'r') as reader:
    # Further file processing goes here
Other options for modes are fully documented online, but the most commonly used ones are the following:

Character	Meaning
'r'	Open for reading (default)
'w'	Open for writing, truncating (overwriting) the file first
'rb' or 'wb'	Open in binary mode (read/write using byte data)
Let’s go back and talk a little about file objects. A file object is:

“an object exposing a file-oriented API (with methods such as read() or write()) to an underlying resource.” (Source)

There are three different categories of file objects:

Text files
Buffered binary files
Raw binary files
Each of these file types are defined in the io module. Here’s a quick rundown of how everything lines up.


 Remove ads
Text File Types
A text file is the most common file that you’ll encounter. Here are some examples of how these files are opened:

open('abc.txt')

open('abc.txt', 'r')

open('abc.txt', 'w')
With these types of files, open() will return a TextIOWrapper file object:

>>> file = open('dog_breeds.txt')
>>> type(file)
<class '_io.TextIOWrapper'>
This is the default file object returned by open().

Buffered Binary File Types
A buffered binary file type is used for reading and writing binary files. Here are some examples of how these files are opened:

open('abc.txt', 'rb')

open('abc.txt', 'wb')
With these types of files, open() will return either a BufferedReader or BufferedWriter file object:

>>> file = open('dog_breeds.txt', 'rb')
>>> type(file)
<class '_io.BufferedReader'>
>>> file = open('dog_breeds.txt', 'wb')
>>> type(file)
<class '_io.BufferedWriter'>
Raw File Types
A raw file type is:

“generally used as a low-level building-block for binary and text streams.” (Source)

It is therefore not typically used.

Here’s an example of how these files are opened:

open('abc.txt', 'rb', buffering=0)
With these types of files, open() will return a FileIO file object:

>>> file = open('dog_breeds.txt', 'rb', buffering=0)
>>> type(file)
<class '_io.FileIO'>
Reading and Writing Opened Files
Once you’ve opened up a file, you’ll want to read or write to the file. First off, let’s cover reading a file. There are multiple methods that can be called on a file object to help you out:

Method	What It Does
.read(size=-1)	This reads from the file based on the number of size bytes. If no argument is passed or None or -1 is passed, then the entire file is read.
.readline(size=-1)	This reads at most size number of characters from the line. This continues to the end of the line and then wraps back around. If no argument is passed or None or -1 is passed, then the entire line (or rest of the line) is read.
.readlines()	This reads the remaining lines from the file object and returns them as a list.
Using the same dog_breeds.txt file you used above, let’s go through some examples of how to use these methods. Here’s an example of how to open and read the entire file using .read():

>>> with open('dog_breeds.txt', 'r') as reader:
>>>     # Read & print the entire file
>>>     print(reader.read())
Pug
Jack Russell Terrier
English Springer Spaniel
German Shepherd
Staffordshire Bull Terrier
Cavalier King Charles Spaniel
Golden Retriever
West Highland White Terrier
Boxer
Border Terrier
Here’s an example of how to read 5 bytes of a line each time using the Python .readline() method:

>>> with open('dog_breeds.txt', 'r') as reader:
>>>     # Read & print the first 5 characters of the line 5 times
>>>     print(reader.readline(5))
>>>     # Notice that line is greater than the 5 chars and continues
>>>     # down the line, reading 5 chars each time until the end of the
>>>     # line and then "wraps" around
>>>     print(reader.readline(5))
>>>     print(reader.readline(5))
>>>     print(reader.readline(5))
>>>     print(reader.readline(5))
Pug

Jack
Russe
ll Te
rrier
Here’s an example of how to read the entire file as a list using the Python .readlines() method:

>>> f = open('dog_breeds.txt')
>>> f.readlines()  # Returns a list object
['Pug\n', 'Jack Russell Terrier\n', 'English Springer Spaniel\n', 'German Shepherd\n', 'Staffordshire Bull Terrier\n', 'Cavalier King Charles Spaniel\n', 'Golden Retriever\n', 'West Highland White Terrier\n', 'Boxer\n', 'Border Terrier\n']
The above example can also be done by using list() to create a list out of the file object:

>>> f = open('dog_breeds.txt')
>>> list(f)
['Pug\n', 'Jack Russell Terrier\n', 'English Springer Spaniel\n', 'German Shepherd\n', 'Staffordshire Bull Terrier\n', 'Cavalier King Charles Spaniel\n', 'Golden Retriever\n', 'West Highland White Terrier\n', 'Boxer\n', 'Border Terrier\n']
Iterating Over Each Line in the File
A common thing to do while reading a file is to iterate over each line. Here’s an example of how to use the Python .readline() method to perform that iteration:

>>> with open('dog_breeds.txt', 'r') as reader:
>>>     # Read and print the entire file line by line
>>>     line = reader.readline()
>>>     while line != '':  # The EOF char is an empty string
>>>         print(line, end='')
>>>         line = reader.readline()
Pug
Jack Russell Terrier
English Springer Spaniel
German Shepherd
Staffordshire Bull Terrier
Cavalier King Charles Spaniel
Golden Retriever
West Highland White Terrier
Boxer
Border Terrier
Another way you could iterate over each line in the file is to use the Python .readlines() method of the file object. Remember, .readlines() returns a list where each element in the list represents a line in the file:

>>> with open('dog_breeds.txt', 'r') as reader:
>>>     for line in reader.readlines():
>>>         print(line, end='')
Pug
Jack Russell Terrier
English Springer Spaniel
German Shepherd
Staffordshire Bull Terrier
Cavalier King Charles Spaniel
Golden Retriever
West Highland White Terrier
Boxer
Border Terrier
However, the above examples can be further simplified by iterating over the file object itself:

>>> with open('dog_breeds.txt', 'r') as reader:
>>>     # Read and print the entire file line by line
>>>     for line in reader:
>>>         print(line, end='')
Pug
Jack Russell Terrier
English Springer Spaniel
German Shepherd
Staffordshire Bull Terrier
Cavalier King Charles Spaniel
Golden Retriever
West Highland White Terrier
Boxer
Border Terrier

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