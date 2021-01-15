# To explain briefly, returning function returns a value, which can be used further, while void functions do not.
# Let’s proceed to examples to understand this better:
# returning function


def get_surname(name):
     return name + 'a'
# void function


def print_surname(name):
     print(name+ 'a')


# In the first case we need to add print function to receive the answer
print(get_surname('Yoqubov'))

# In the second case we just call the function, because it does not return, but just prints it
print_surname('Yoqubov')

# Further, in the following case we give a variable a value
surname = get_surname('Yoqubov')
print(surname)

# here we get ‘Yoqubova’

Surname2 = print_surname('Yoqubov')
print(Surname2)

# Here, however, we will get ‘none’ because the function did not return any value, so the variable
# Thus, we can conclude that when we need the function to return the value that can be used further,
# we use the first type, while we need the function to just do short use of the information without returning
# we use the second option.
