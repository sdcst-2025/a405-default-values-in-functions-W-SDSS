#!python3

"""
Create a function called title that creates a single line of output to display the word
"Title" with a box around it.  
The function will have 1 optional input:
symbol : string.  The symbolt to use as the border. Default symbol is "="

The return value is the output string with escaped line breaks.

example assertion:
assert title("*") == "*********\n* Title *\n*********"
assert title() == "=========\n= Title =\n========="
(2 points)

"""

def title(symbol="="):
    word = " Title "
    border = symbol*9
    return border+"\n"+symbol+word+symbol+"\n"+border

assert title("*") == "*********\n* Title *\n*********"
assert title() == "=========\n= Title =\n========="

#dekitaaa





