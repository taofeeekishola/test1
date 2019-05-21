#While Loop is used to test if a condition returns true, more than once
'''
lessThan5 = 0
while lessThan5 < 5:
    print('Still < 5')
    lessThan5 += 1
    if lessThan5 == 3:
        break
    print('Thank you') 
print('Finished')
'''
'''
lessThan5 = 0
while lessThan5 < 5:
    print('Still < 5')
    lessThan5 += 1
    if lessThan5 == 3:
        continue
    print('I am waiting')    
'''
'''
countries = ['Nigeria','Ghana',True,1000,'America']
for country in countries:
    print(country) 
'''
'''
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vowel = ['a','e','i','o','u']
for a in alpha:
    if a in vowel:
        print(a,'is a vowel')
    else:
        print(a,'is a Consonant')
'''

