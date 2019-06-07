
# Write a Python function to multiply all the numbers in a list called 'MultiplyElementsInList'.
# START

def MultiplyElementsInList(list):  
    total = 1
    for x in list:
        total *= x  
    return total  
print(MultiplyElementsInList((1, 2, 3,)))    


# END
# -------------------------------------
# DO NOT TOUCH ANY CODE BELOW THIS LINE
print("Test 1 Passed: " + str(MultiplyElementsInList([1, 2, 3]) == 6))
print("Test 2 Passed: " + str(MultiplyElementsInList([0, 2, 3]) == 0))
print("Test 3 Passed: " + str(MultiplyElementsInList([2, 2, 2]) == 8))
print("Test 4 Passed: " + str(MultiplyElementsInList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]) == 30414093201713378043612608166064768844377641568960512000000000000))


#def Calculate(num1, num2):
#    return num1 + num2

#def print5 (count)
#    for i in range(0, count):
#        print("Hello World")
#        print(Calculate(i, Calculate(5, 6)))


#my_list = [1, 2, 3, 4, 5]
#my_new_list = [i * 5 for i in my_list]

#print(my_new_list)