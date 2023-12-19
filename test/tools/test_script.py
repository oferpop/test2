# test_script.py

from tools.numbers.simp import add, subtract
from tools.numbers.comp import sumofdigits, ispal
from tools.col import myzip

def run_tests():
    try:
        # Attempt to call a comp function before a simp function
        print("Trying to call sumofdigits before calling any simp function:")
        print(sumofdigits(123))  # This should raise an exception

    except Exception as e:
        print("Caught an exception:", e)

    # Now calling a simp function
    print("\nCalling a simp function:")
    print("Adding 5 and 3:", add(5, 3))

    # Now the comp function should work
    print("\nNow calling comp functions after calling a simp function:")
    print("Sum of digits in 234:", sumofdigits(234))
    print("Is 1221 a palindrome?", ispal(1221))

    # Testing myzip function
    print("\nTesting myzip function:")
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    print("Zipping", list1, "and", list2, ":", list(myzip(list1, list2)))

if __name__ == "__main__":
    run_tests()
