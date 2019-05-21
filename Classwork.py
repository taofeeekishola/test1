#1)
print('Question 1')
name = 0
count = 0
while name <= 100:
    name += 1
    while count < 100:
        count += 1
        print(f"{count} Ishola Taofeek")



#2)
print('Question 2')
num = 1
while num < 20:
    num += 1
    print(f"{num}---{num**2}")

#3!)
print('Question 3a')
gap = ' '
numbers = [15, 2, 2, 15]
for number in numbers:
    if number == 15:
        print('x' * number)
    elif number == 2:
        print(f"x {gap*11} x")
        
#3!!)
print('Question 3b')
for number in range(7):
    print('x' * number)

#3!)
print('Question 3c')
gap = ' '
numbers = [1,2,4,3,]
for number in numbers:
    if number == 1:
        print(f"{gap*5} x {gap*5}")
    elif number == 4:
        print(f"{gap*2} xxxxxxxx {gap*2}")
    elif number == 2:
        print(f"{gap*4}x{gap*4}x")
    elif number == 3:
         print(f"{gap*2}x{gap*8}x")

#4)
def factorial(n):   
    if n == 1:
        return 1
    else:
        s = n * factorial(n-1)
        return (f"The {n-1}th factorial is {s}")

print(factorial(5))
print('Thank you')

#5)
def last(number):
    if number == 3:
        return 3
    else:
        a = 3 ** number
        (f"The number is {a}")
        return (f"The number is {a}")
number = float(input('Enter a number:'))
print(last(number))