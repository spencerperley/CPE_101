from Task_1 import *

def test_chop():
    assert chop([1,2,3,4,5]) == [1,5]
    assert chop([1,2]) == [1,2]
    
test_chop()
print("Pass")