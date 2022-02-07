from Task_1 import *
import unittest

def testAllOperators():
    assert(calculate(2,2,"*") == 4)
    assert(calculate(2,2,"-") == 0)
    assert(calculate(2,2,"+") == 4)
    assert(calculate(2,2,"/") == 1)

def testInvalidOperator():
    assert(calculate(2,2,"kjgbnfasod") == None)

testAllOperators()
testInvalidOperator()
print("Pass")