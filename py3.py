# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically 
# called 'SortWordsAlphabetically'.
# START

def SortWordsAlphabetically():
    items=[n for n in input().split('-')]
    items.sort()
print('-'.join(items))

# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(SortWordsAlphabetically("Bob-does-not-like-frank") == 'bob-does-frank-like-not'))
print("Test 2 Passed: " + str(SortWordsAlphabetically("why-am-i-doing-this-this-is-terrible") == "am-doing-i-is-terrible-this-this-why"))
print("Test 3 Passed: " + str(SortWordsAlphabetically("frank-kill-zoe-did") == "did-frank-kill-zoe"))