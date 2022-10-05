"""In the activity selection problem, the task is to find the maximum number of activities a person can do by selecting only one activity at a time, and the other activity can only be selected, when the earlier selected one gets finished.
All the activities have a start and finish time of their own. At the very first, sort the activities in the increasing order of their finish time. After this, select the activity at the start, and then check all the other activities as per the finish time of the previously selected activity. The previously selected activity finishes after the second activity, then the second activity cannot be selected.
Code :-"""
"""Prints a maximum set of activities that can be done by a
single person, one at a time"""
# n --> Total number of activities
# s[]--> An array that contains start time of all activities
# f[] --> An array that contains finish time of all activities
 
def printMaxActivities(s , f):
    n = len(f)
    print ("The following activities are selected:")
 
    # The first activity is always selected
    i = 0
    print (i,end=' ')
 
    # Consider rest of the activities
    for j in range(n):
 
        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if s[j] >= f[i]:
            print (j,end=' ')
            i = j
 
# Driver program to test above function
s = [1 , 3 , 0 , 5 , 8 , 5]
f = [2 , 4 , 6 , 7 , 9 , 9]
printMaxActivities(s , f)
