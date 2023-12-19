# app.py

from tools.numbers.simp import add, subtract, State
from tools.numbers.comp import sumofdigits, ispal
from tools.col import myzip

def test_simp_functions():
    assert add(5, 3) == 8
    assert subtract(10, 5) == 5
    print("All simp tests passed.")

def test_comp_functions():
    # Ensure comp functions raise an exception if simp functions haven't been called
    try:
        sumofdigits(234)
        assert False, "Exception not raised for sumofdigits without simp function call"
    except Exception:
        pass

    try:
        ispal(1221)
        assert False, "Exception not raised for ispal without simp function call"
    except Exception:
        pass

    # Now call a simp function and test comp functions
    add(1, 1)  # This sets State.simp_called to True
    assert sumofdigits(234) == 9
    assert ispal(1221) == True
    assert ispal(1234) == False
    print("All comp tests passed.")

def test_col_functions():
    assert myzip([1, 2, 3], ['a', 'b', 'c']) == [(1, 'a'), (2, 'b'), (3, 'c')]
    print("All col tests passed.")

def main():
    # Test functions
    test_simp_functions()
    test_comp_functions()
    test_col_functions()

    # Demonstration of functionality
    print("Adding 5 and 3:", add(5, 3))
    print("Subtracting 5 from 10:", subtract(10, 5))
    print("Sum of digits in 234:", sumofdigits(234))
    print("Is 1221 a palindrome?", ispal(1221))
    print("Is 1234 a palindrome?", ispal(1234))
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    print("Zipping", list1, "and", list2, ":", list(myzip(list1, list2)))

if __name__ == "__main__":
    main()
