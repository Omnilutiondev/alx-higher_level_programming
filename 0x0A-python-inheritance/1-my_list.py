#!/usr/bin/python3
'''Function for MyList class.'''


class MyList(list):
    '''A custom MyList class.'''
    def print_sorted(self):
        '''The para for printing sorted list.'''
        print(sorted(self))
