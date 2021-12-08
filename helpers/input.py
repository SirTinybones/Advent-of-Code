def raw(filename:str):
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    with open(filename) as f:
        return f.read()

def string(filename:str):
    """Return the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rsplit('\n')

def lines(filename:str):
    """Return a list where each line in the input file is an element of the list"""
    with open(filename) as f:
        return f.readlines()

def ints(filename:str):
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    with open(filename) as f:
        return [int(i) for i in f.read().split(",")]