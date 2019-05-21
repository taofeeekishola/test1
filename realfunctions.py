#simple prints the arguments passed into it
'''
def printer(arg):
    print('Please enter and argument')
    print(arg)
printer('Hello Class')

#converts celcus to Farenheit
def faren(T_in_celsius):
    return T_in_celsius * 9/5 + 32
print(faren(20))

faren_list = []
celsius_list = [20,5,10.6,7,9]
for x in celsius_list:
    faren_list.append(faren(x))
print(faren_list)
'''
'''
def averager():
    num = []
    sum = 0
    while len(num) <= 4:
        num1 = float(input('Enter a number '))
        num.append(num1)
    print(num)
    for item in num:
        sum += item
    av = float(sum/len(num))
    print(av)

averager()
'''
'''
#keyword parameters
def sum(a,b,c=0,d=0):
    return a-b+c-d
print(sum(12,4))
'''
'''
#variable scopping: by def, variables defined in a function are local to that
def f():
    s = 'pearl'
    print(s)
s = 'python'
print(s)
f()
'''
'''
def f():
    global s
    print(s)
    s = 'dog'
    print(s)
s = 'cat'
f()
print(s)
'''
'''
#Arbitiary number of parameters
def arithmetic_mean(first, *values):
    return(first + sum(values)) / (1 + len(values))

print(arithmetic_mean(45,32,89,78))
'''
'''
#sum of a gp when ratio is a whole number
def sum_gp(first,second,*series):
    r = second/first
    n = 2 +(len(series))
    top = first * ((r**n)-1)
    bottom = r-1
    return top/bottom


def sum_of_gp():
    first_term = float(input('Enter the first term: '))
    common_ratio = float(input('Enter the common ratio: '))
    n = float(input('Enter the number of terms: '))
    top = first_term * ((common_ratio**n)-1) 
    bottom = common_ratio -1
    return top/bottom

print(sum_of_gp())
'''
# def ave(first,*number):
#     add = first + sum(number)
#     ave1 = add / (1 + len(number))
#     return ave1

# print(ave(45,56,3,23,8,98,4))

#recursive functions

def factorial(n):
   
    if n == 1:
        return 1
    else:
    
        s = n * factorial(n-1)
       
        print(f"The {n-1}th factorial is {s}")
        return s

print(factorial(5))

