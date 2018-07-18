# UDF Imports
from is_unique import is_unique
from is_unique import is_unique_faster

# Needed Imports
import time
from random import choice
from string import lowercase
from timeit import default_timer as timer

# Test is_unique.py functionality
def test_unique():
    start_time = timer()
    val_1 = is_unique("Hello")  # False Case
    val_2 = is_unique("That isn't possible")  # False Case
    val_3 = is_unique("Safe word")  # Success Case
    val_4 = is_unique("There once was a man who wore a hat.")  # Long False Case
    end_time = timer()
    print(str.format("isUnique: {} {} {} {} {}", val_1,
                    val_2, val_3, val_4, end_time - start_time))

    assert val_1 == False
    assert val_2 == False
    assert val_3 == True
    assert val_4 == False 

    start_time = timer()
    val_1 = is_unique_faster("Hello")  # False Case
    val_2 = is_unique_faster("That isn't possible")  # False Case
    val_3 = is_unique_faster("Safe word")  # Success Case
    val_4 = is_unique_faster("There once was a man who wore a hat.")  # Long Case
    end_time = timer()
    print(str.format("isUniqueFaster: {} {} {} {} {}",
                    val_1, val_2, val_3, val_4, end_time - start_time))
    
    assert val_1 == False
    assert val_2 == False
    assert val_3 == True
    assert val_4 == False 

# def test_answer():
    