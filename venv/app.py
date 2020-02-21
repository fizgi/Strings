""" A study focuses on string methods, slices,
    working with files, and automated testing

    author: Fatih IZGI
    date: 21-Feb-2020
    version: python 3.8.1
"""

from typing import List, Iterator, IO


def reverse(string: str) -> str:
    """ Takes a string as an argument and
        returns a new string which is the reverse of the argument
    """

    reversed_string: str = ""
    lenght: int = len(string)

    for index in range(lenght-1, -1, -1):  # loop backwards
        reversed_string += string[index]  # add each letter to the new string

    return reversed_string  # return the reversed string


def substring(target: str, string: str) -> int:
    """ A substring function that is similar to Python’s string.find(target) method that returns
        the offset from the beginning of  string "string" where target occurs in "string"
    """

    string_lenght: int = len(string)
    target_lenght: int = len(target)

    for index in range(string_lenght - target_lenght + 1):
        current: str = string[index:index+target_lenght]  # create a new substring
                                                          # which will be compared with the target
        if current == target:  # if equal
            return index  # return the current index

    return -1  # could not find any substring


def find_second(target: str, string: str) -> int:
    """ Return the offset of the second occurrence of target in string.
        Return -1 if target does not occur twice in string
    """
    index: int = string.find(target)  # find first
    index = string.find(target, index+1)  # find second

    return index  # return the second found index or -1


def get_lines(path: str) -> Iterator[str]:
    """ Opens a file for reading and yields one line from the file at a time """

    lines: List[str] = []  # add lines to a list to work on

    try:  # opening the file
        file_path: IO = open(path, "r")
    except FileNotFoundError:
        print(f"Can't open {path}")
    else:
        with file_path:
            for line in file_path:
                lines.append(line)

    delete_list: List[int] = []  # lines starting with '#' will be deleted

    index: int = 0

    while index < len(lines):
        while lines[index].endswith("\\\n"):  # combining all the continuous lines
            lines[index] = lines[index].strip("\\\n") + lines[index + 1]    # add the next line
                                                                            # to the current line
            lines.pop(index + 1)  # remove the added(next) line

        if lines[index].endswith("\n"):  #remove the next line '\n'
            lines[index] = lines[index][:lines[index].find("\n")]

        if lines[index].startswith("#"):    # if the itself line is a comment
            delete_list.append(index)       # add it's index to the removed list

        if lines[index].find("#") != -1:                            # if there is an inline comments
            lines[index] = lines[index][:lines[index].find("#")]    # remove comment

        index += 1

    for i in delete_list[::-1]:
        lines.pop(i)  # finally, delete the comment lines

    for line in lines:
        yield line
