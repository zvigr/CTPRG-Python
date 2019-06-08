print ('hi')

x = 4
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
    
import sys
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

'''
try:
    linux_interaction()
except AssertionError as error:
    #"pass" would do nothing
    print(error)
    print('The linux_interaction() function was not executed')


try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')
'''
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)


'''
Warning: Catching Exception hides all errors…even those which are completely unexpected. This is why you should avoid bare except clauses in your Python programs. Instead, you’ll want to refer to specific exception classes you want to catch and handle. You can learn more about why this is a good idea in this tutorial.
'''