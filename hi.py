'''Write a function called 'GetElementAt' that takes a list and index as a parameter and returns the element at the index, 
or None if the index is out of bounds. You can not use an if statement in your function (use a try except instead).
eg: GetElementAt([1,2,3,4,5,6,7], 4) -> 5
eg: GetElementAt([1, 2, 3], 3) -> None'''
'''
def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

x = 2
y = 3
print_max(y, x)


def GetElementAt(myList):
    index = myList[1]
    print = (myList, index)

myList = [0, 1, 2]
GetElementAt(myList, 1)

'''