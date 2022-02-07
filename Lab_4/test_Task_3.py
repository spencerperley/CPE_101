from Task_3 import *

def test_middle():
    assert middle([1,2,3,4,5]) == [2,3,4]
    assert middle([1,2]) == [1,2]
    assert middle([]) == []
    
test_middle()
print("Pass")