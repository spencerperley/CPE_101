from Task_3 import *

def testFilterPalendrome():
    assert filter_pallendromes(["abdba","abcde","ddddd"]) == ["abdba","ddddd"]
    assert filter_pallendromes(["abdka","abcde","dddkd"]) == []
    
testFilterPalendrome()
print("Pass")