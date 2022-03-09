from task_4 import *


def testA():
    assert linear_Search_uniq([1,3,5,4,5,3,4,3,3],3) == [1, 5, 4, 5, 4]
    assert linear_Search_uniq([1,2,3],2) == [1,3]
def testB():
    a = [9,8,7,6,5,4,3,2,1]
    
    b = [21.654,42.342,6.243]
    ss(a)
    ss(b)
    assert a == [1,2,3,4,5,6,7,8,9]
    assert b == [6.243,21.654,42.342]
    
    
testB()

testA()

print("pass")