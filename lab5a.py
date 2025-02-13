#!/usr/bin/env python3
# Author Name: Edison Leung
# Author ID: eleung41 147724231
# Date Created: 2025/02/12


def read_file_string(file_name):
    """Reads the entire file content as a string."""
    f = open(file_name)  # Opens (file_name)
    file_content = f.read()    # Reads the content
    f.close()                  # Closes the file (important!)
    return file_content

def read_file_list(file_name):
    """Reads the file content as a list of lines (without newlines)."""
    f = open(file_name, 'r')  # Opens (file_name)
    read_data_list = f.read().splitlines()  # Efficiently split into lines
    f.close()                  # Closes the file
    return read_data_list


if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
