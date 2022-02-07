from Task_2 import *

def test_cumulative():
    assert cumulative([1,2,3]) == [1,3,6]
    assert cumulative([0,0,0,0,0,0]) == [0,0,0,0,0,0]
    assert cumulative([]) == []
    assert cumulative([1]) == [1]
    
test_cumulative()
print("Pass")