#QUESTION
""">>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings. 
>>> print a
['this', 'is', 'a', 'string']

>>> a = "-".join(a)
>>> print a
this-is-a-string """


#CODE
def split_and_join(line):
    # write your code here
    return '-'.join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
