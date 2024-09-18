#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return list(map(lambda px: replace if px == search else px, my_list))
