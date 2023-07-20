x = 2
print(x)
y="hello"
print(y)
z=x**2 + 5*x
print(z)
my_first_list = ['apple', 1, 'banana', 2]
my_fruit_list = ['apple', 'banana']
my_int_list = [1, 2, 3]
my_first_list[0]
my_fruit_list[1]
my_int_list[2]
cal_lookup = {'apple': 95, 'banana': 105, 'orange': 45}
cal_lookup['banana']
for f in my_fruit_list:
    print(f)

def sq_int(x):
    y = x**2
    return y

sq_int(5)
sq_int(40)

y=5
x=4

def describe_evenness(x):
    if is_even(x):
        print("It's even!")
    elif is_odd(x):
        print("It's odd!")
    else:
        print("It's neither even nor odd!")

describe_evenness(y)

for x in my_first_list:
    if x in my_fruit_list:
        print(cal_lookup[x])
    elif x in my_int_list:
        print(x**2)
    else:
        print("Neither a fruit nor a number!")

for key in cal_lookup:
    print(cal_lookup[key])


def dictionary_squared(dict):
    for key in dict:
        print(f'The square of {dict[key]} is {dict[key]**2}')

dictionary_squared(cal_lookup)
