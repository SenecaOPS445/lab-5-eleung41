#!/usr/bin/env python3
# Author Name: Edison Leung
# Author ID: eleung41 147724231
# Date Created: 2025/02/12

def read_file_string(file_name):
    """Reads the entire file content as a string."""
    f = open(file_name, 'r')  # Opens (file_name)
    file_content = f.read()  # Reads the content
    f.close()  # Closes the file (important!)
    return file_content

def read_file_list(file_name):
    """Reads the file content as a list of lines (without newlines)."""
    f = open(file_name, 'r')  # Opens (file_name)
    read_data_list = f.read().splitlines()  # Efficiently split into lines
    f.close()  # Closes the file
    return read_data_list

def append_file_string(file_name, string_of_lines):
    """Appends a string to the end of a file."""
    f = open(file_name, 'a')  # Open in append mode ('a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):
    """Writes a list of lines to a file, each item on a new line."""
    f = open(file_name, 'w')  # Open in write mode ('w')
    for line in list_of_lines:
        f.write(line + '\n')  # Add newline after each line
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """Copies a file and adds line numbers to each line in the new file."""
    f_read = open(file_name_read, 'r')
    f_write = open(file_name_write, 'w')

    line_number = 1
    line = f_read.readline()  # Read the first line

    while line != "":  # Loop until end of file
        f_write.write(str(line_number) + ":" + line)  # Write with line number
        line_number += 1
        line = f_read.readline()  # Read the next line

    f_read.close()
    f_write.close()



if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
