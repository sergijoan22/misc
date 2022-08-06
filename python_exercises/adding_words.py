'''
# Adding Words

You need to write a function that takes multiple words as its argument and returns a concatenated version of those words separated by dashes (-).
The function should be able to take a varying number of words as the argument.

## Example:

**Sample Input**
this
is
great

**Sample Output**
this-is-great

'''

def concatenate(*args):
    string = ''
    for word in args:
        string += str(word)
        string += '-'
    else:
        string = string[:-1]
    return string

print(concatenate("I", "love", "Python", "!"))
