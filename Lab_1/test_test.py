from test import *

from Lab_1.test import change_index_1_to_1

def test_is_one():
    b = [1,4,5]
    change_index_1_to_1(b)
    assert (b[1]) == 1 ; "faild"
    