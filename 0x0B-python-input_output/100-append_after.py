#!/usr/bin/python3
"""this function inserts a line of text to a file,
after each line containing a specific str
"""


def append_after(filename="", search_string="", new_string=""):
    """adds "new_string" after a line containing
    "search_string" in "filename"
    """
    with open(filename, 'r', encoding='utf-8') as f:
        line_li = []
        while True:
            line = f.readline()
            if line == "":
                break
            line_li.append(line)
            if search_string in line:
                line_li.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(line_li)
