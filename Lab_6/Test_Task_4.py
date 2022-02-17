from Task_4 import *

def TestGroupsOfThree():
    assert groups_of_3([1,2,3,4,5,6,7,8,9]) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
    assert groups_of_3([1,2,3,4,5,6,7,8]) == [[1, 2, 3], [4, 5, 6], [7, 8]] 
    
TestGroupsOfThree()
print("Pass")