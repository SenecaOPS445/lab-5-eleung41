#!/usr/bin/env python3
# Author Name: Edison Leung
# Author ID: eleung41 147724231
# Date Created: 2025/02/13

def add(number1, number2):
    """Add two numbers together, return the result, if error return string 'error: could not add numbers'"""
    try:
        return number1 + number2  # Try the addition directly
    except TypeError:
        try:
            return int(number1) + int(number2) # Try converting to int then add
        except:
            return 'error: could not add numbers' # if it fails return error msg
    except:
        return 'error: could not add numbers' # if it fails return error msg


def read_file(filename):
    """Read a file, return a list of all lines, if error return string 'error: could not read file'"""
    try:
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()
        return lines
    except FileNotFoundError:
        return 'error: could not read file'
    except:
        return 'error: could not read file'


if __name__ == '__main__':
    print(add(10, 5))  # works
    print(add('10', 5))  # works
    print(add('abc', 5))  # exception
    print(read_file('seneca2.txt'))  # works
    print(read_file('file10000.txt'))  # exception
