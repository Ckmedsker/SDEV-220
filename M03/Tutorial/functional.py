def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def do_math(action, x ,y):
    return action(x,y)

print(add(3,4))
print(subtract(3,4))
print(multiply(3,4))
print(divide(3,4))
print(do_math(add,3,4))

my_list = [1,2,3,4]

doubled_list = [2*val for val in my_list]
print(doubled_list)