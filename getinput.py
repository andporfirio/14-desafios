from __future__ import absolute_import, division, print_function

def getinput(prompt=''):
    try:
        line = raw_input(prompt)
    except NameError:
        line = input(prompt)
    return line
