# File: tools/numbers/simp.py

class State:
    simp_called = False

def add(x, y):
    State.simp_called = True
    return x + y

def subtract(x, y):
    State.simp_called = True
    return x - y
