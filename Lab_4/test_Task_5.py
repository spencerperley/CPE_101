from Task_5 import *

def testSubstring():
    
    assert findSubstring("abc","gvuvabckjh")
    assert findSubstring("abc","hgiygavuhbkjbbnnicuh")
    assert not(findSubstring("abc", "hgciygavuhbkjbbnniuh"))
    
testSubstring()
print("Pass")
