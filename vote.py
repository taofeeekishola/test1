print('ELECTORAL BODY OF NIGERIA')

Con_States = float(input('How many states are in conclusive: '))

if(Con_States > 5):
    print('With more than 5 states having Elections not colclusive the Election has been calcelled')
else:
    B_Vote = float(input('Enter the number of votes Buhari has: '))
    A_Vote = float(input('Enter the number of votes Atiku has: '))

    if (B_Vote > A_Vote):
        print('Buhari has won the Election with more votes')
    elif (A_Vote > B_Vote):
        print('Atiku has won the Election with more votes')
    elif (A_Vote == B_Vote):
        print('They both have equal number of Votes')
        print('We need to know who won more states.')
        States_Buhari = float(input('Enter the number of states Buhari won: '))
        States_Atiku = float(input('Enter the number of states Atiku won: '))
    
        if (States_Atiku > States_Buhari):
            print('Atiku has won the Election with more states won')
        else:
            print('Buhari has won more Election with more states won')


    