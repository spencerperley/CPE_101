from Task_2 import *

def testCalcAverage():
    assert calcAvererage([1,3]) == 2
    assert calcAvererage([1,0,2]) == 1
    
testCalcAverage()
print("Pass")