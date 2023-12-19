# File: tools/numbers/comp.py

from tools.numbers.simp import State

def sumofdigits(num):
    if not State.simp_called:
        raise Exception("A function from simp must be called before comp functions.")
    return sum(map(int, str(num)))

def ispal(num):
    if not State.simp_called:
        raise Exception("A function from simp must be called before comp functions.")
    num_str = str(num)
    return num_str == num_str[::-1]
