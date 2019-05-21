try:
    x = int(input('Please Enter a number '))
    result = x/2
    print(result)
except ValueError as err:
    print(err)
    