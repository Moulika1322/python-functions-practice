# Functions Demonstration
# 1️ Basic function definition and call
def moulika():
    print("Moulika ROUTHU")
    print("Kirankumar ROUTHU")

moulika()  # calling the function
print("ROUTHU APPALANAIDU")
moulika()
print("ROUTHU PADMAVATHI")

# 2️ Function with parameter
def sayhello(name):
    print("HELLO", name)
    print("NICE TO MEET YOU")

sayhello('KIRANKUMAR')
print("Some block of code......")
user_name = 'MOULIKA'
sayhello(user_name)

# 3️ Function to add two numbers
def add(fn, sn):
    sum_value = fn + sn
    print('ans', sum_value)

add(22, 13)

# 4️ Function to add multiple numbers using *args
def getsum(*x):
    sum_value = 0
    for m in x:
        sum_value += m
    print("sum:", sum_value)
    print("Third element in the list:", x[2])

getsum(22, 13, 45, 50, 23)

# 5️ Function with default parameter
def hello(name, age, country='INDIA'):
    print("hello", name)
    print("age:", age)
    print("I AM FROM", country)

hello(age=2, name='pregna')
hello('moulika', 20, 'USA')

# 6️ Function returning multiple values (sum and a static value)
def add_multiple(*nums):
    result = 0
    value = 45
    for m in nums:
        result += m
    return result, value

addition = add_multiple(12, 13, 14, 15, 16)
print("Returned values (sum, static value):", addition)
