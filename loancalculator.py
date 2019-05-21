print("Welcome To Laon MFBank")

rate = float(input("What is your company's rate? "))
rate_fraction = rate/100
print("Your Company's Rate is %f" %rate_fraction)

principal = float(input("Please enter the amount you want: "))
print("You requested %f" %principal)

if (0 < rate <= 5 and principal < 200000):
    time = float(input("How many Years "))
    print('You want to take a loan for %f ' %time)
    total_rate = (principal * rate_fraction * time)/100
    print('Your Total Rate is %f' %total_rate)
    total_repay = principal + total_rate
    print('The Total amount that you will pay is %f' %total_repay)
    month_repay = (total_repay)/(time*12)
    print('This is how much you will pay monthly %f' %month_repay)

elif (0 < rate <= 5 and principal > 200000):
     print("The maximum Loan you can collect  200000")

elif (6 <= rate <= 10 and principal < 500000):
    time = float(input("How many Years "))
    print('You want to take a loan for %f ' %time)
    total_rate = (principal * rate_fraction * time)/100
    print('Your Total Rate is %f' %total_rate)
    total_repay = principal + total_rate
    print('The Total amount that you will pay is %f' %total_repay)
    month_repay = (total_repay)/(time*12)
    print('This is how much you will pay monthly %f' %month_repay)

elif (6 <= rate <= 10 and principal > 500000):
     print("The maximum Loan you can collect is 500000" )

elif (11 <= rate <= 20 and principal < 1000000):
    time = float(input("How many Years "))
    print('You want to take a loan for %f ' %time)
    total_rate = (principal * rate_fraction * time)/100
    print('Your Total Rate is %f' %total_rate)
    total_repay = principal + total_rate
    print('The Total amount that you will pay is %f' %total_repay)
    month_repay = (total_repay)/(time*12)
    print('This is how much you will pay monthly %f' %month_repay)
    
elif (11 <= rate <= 20 and principal > 1000000):
    print("The maximum Loan you can collect is 1000000 ")
else :
    time = float(input("How many Years "))
    print('You want to take a loan for %f ' %time)
    total_rate = (principal * rate_fraction * time)/100
    print('Your Total Rate is %f' %total_rate)
    total_repay = principal + total_rate
    print('The Total amount that you will pay is %f' %total_repay)
    month_repay = (total_repay)/(time*12)
    print('This is how much you will pay monthly %f' %month_repay)
    


