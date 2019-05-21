'''
#1)
name = 0
count = 0
while name <= 100:
    name += 1
    while count < 100:
        count += 1
        print(f"{count} Ishola Taofeek")
'''

'''
#2)
num = 0
while num < 20:
    num += 1
    print(f"{num}---{num**2}")
'''

#3!!)
# for number in range(7):
#     print('x' * number)

#3!!!)
gap = ' '
numbers = [15, 2, 2, 15]
for number in numbers:
    if number == 15:
        print(f"x {number}")
    elif number == 2:
        print(f"* {gap*7} *")

#3!)
# gap = ' '
# print(f"{gap*5} x {gap*5}")
