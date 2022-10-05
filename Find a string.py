#QUESTION
#To count the number of times sub string occurring in the main given string.
#ABCDCDC
#CDC

#2

#CODE
def count_substring(string, sub_string):
    len_of_string = len(string)
    len_of_sub_string = len(sub_string)
    c = 0
    for i in range(len_of_string):
        if (sub_string == string[i:i+len_of_sub_string]):
            c+=1
    return c 

if __name__ == '__main__':
