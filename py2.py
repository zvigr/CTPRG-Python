
# Write a Python function that checks whether a passed string is palindrome or not called 'IsPalindrome' that returns either True or False.
# START

def IsPalindrome():
    my_str = 'aIbohPhoBiA'

# making it suitable for caseless comparison
    my_str = my_str.casefold()

# reversing the string
    rev_str = reversed(my_str)

    # check if the string is equal to its reverse
    if list(my_str) == list(rev_str):
        print("It is palindrome")
    else:
        print("It is not palindrome")

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(IsPalindrome("GlenElg") == True))
print("Test 2 Passed: " + str(IsPalindrome("Nurses Run") == True))
print("Test 3 Passed: " + str(IsPalindrome("Nurses") == False))
print("Test 4 Passed: " + str(IsPalindrome("frank") == False))