list1 = ['Mathematics','Language', 2000, False, 'Health Education']
# #displaying the nth term
# print(list1[2])

# print(type(list1))

# #updating a list
# list1[4]= True
# print(list1)

# #deleting items from a list
# del list1[2]
# print(list1)

# #multiplication and conncatination
# list2 = list1 + ['Agric',10.7]
# print(list2)
# print(['Agric',10.7] * 3)


# #lenght of List1
# print(len(list1))

# #membership
# print('Agric' in list2)

# #iterable
# print('Start Iteration')
# for x in list1:
#     print(x)


# for x in list1:
#     if(list1.index(x) <=2):
#         print(x)

'''
list1 = ['Mathematics','Language','Science1', 2000, False, 'Health Education']
for x in list1:
    print(x, end=' ')
'''
'''
print('Start from here')
for x in list1:
    if(list1.index(x) <=4):
        print(x, end=' and ')
    else:
        print(x)
'''
#Indexing
'''
print(list1[-2])
print(list1)
print('Slicing Starts')
print(list1[2:])
print(list1[:2])
print(list1[1:4])
'''

# #Max
# list2 = ['Monday','Tuesday','Thursday','Friday','Wednesday']
# print(max(list2))
# print(min(list2))

# #convert a turple to list
# tuple1 = (234,'C++',False,'Python')
# print(tuple1)
# list3 = list(tuple1)
# print(list3)

#append
# list3 = [234,'C++',False,'Python']
# list4 = list3.append('C#')
# list5 = list3 + ['c#']
# print('For concatiation:', list5)
# print('for appending',list4)

#count
# list6 = [234,'C++',False,'Python','C++','c#']
# print(list6.count('C++'))

# print([234,'C++',False,'Python','C++','c#'].count('Python'))
# print([234,'C++',False,'Python','C++','c#'].count('Python'))

# '''
# #extending a range into a list
# print(range(5))
# for i in range(5):
#     print(i, end=" ")
# '''
# list7 = list(('a','b','c','d'))
# print(list7)
# new = list7.extend(range(5))
# print(list7)
# print(new)

#index
# name = ['Bolaji','Aisha','Daniel','David','Aisha','Taofeek']
# print('First occurance of Aisha', name.index('Aisha'))

#pop() ;returns and removes the last item
# subject = ['Maths','English','Science','Language','Culture','Religion']
# print(subject.pop())
# print(subject.pop())
# print(subject)

'''
#remove(); removes the item but returns None
subject = ['Maths','English','Science','Language','Culture','Religion']
holder1 = subject.pop()
holder2 = subject.remove('Science')#takes a complusory argument
print(holder1)
print(holder2)
'''
'''
#reverse(); reverses the list and returns none
subject = ['Maths','English','Science','Language','Culture','Religion']
holder3 = subject.reverse()
print(holder3)
print(subject)
'''
'''
#sort(); arranges the item in the list in alphabetical order
subject = ['Maths','English','Science','Language','culture','Religion']
print(subject.sort())
print(subject)
'''


#Dictionaries
states_pop = {'Lagos':3567234,'Kano':46742871,'Abuja':1672367,'Port-Harcot':3123907,'Kaduna':2784123}
# print(states_pop['Kano'])

# #replace
# states_pop['Ogun'] = 123786;
# print(states_pop)
'''
#defining an empty dictionary
names = {}
names['first'] = 'Seun Bala'
print(names)
'''

'''
#the values can reocure
name = {'First':'Senn Bala','Second':'John Udeh','First':'Mark Thaindi','Forth':'Senn Bala'}
print(name['First'])
'''
'''
en_yor = {'One':'Ookan','Two':'Eeji','Three':'Eeta','Four':'Eerin','Five':'Aarun'}
#print(en_yor['One'])

yor_ibo = {'Ookan':'Otu','Eeji':'Abo','Eeta':'Ato','Eerin':'Ano','Aarun':'Ise'}
#print(yor_ibo['Eeta'])

#classwork: eng ibo translation of one and two

print(yor_ibo[en_yor['One']])
'''
#Rules for dictionaries
#You cant use mutable types as key
'''
dico = {'abc':[1,2,3]}
print(dico)

#Operations on Dictionaries
#len(d), del(k),k in d, k not in d
print('abc' in dico )
del dico['abc']
print(dico)
'''
'''
morse = {'A':'qw','B':'qwer','C':'qwerty','D':'qwertyui','E':'qwertuiop',
'1':'as','2':'asdf','3':'asdfghj','4':'asdfghjkl','5':'asdfghjklxz'}

from datastructure import morse
print(len(morse))
'''
'''
#pop()
en_yor = {'one':'Ookan','Two':'Eeji','Three':'Eeta','Four':'Eerin','Five':'Aarun'}
yor_ibo = {'Ookan':'Otu','Eeji':'Abo','Eeta':'Ato','Eerin':'Ano','Aarun':'Ise'}
#okay = input('Enter and English word: ')
#okay_2 = okay.lower()
#print('This is the Igbo translation',yor_ibo[en_yor['one']])

#30 APRIL 2019
#if a pair cannot be popped, a key error is raised
#POP IS USED TO PICK ANY VALUE WITH A KEY
#print(en_yor.pop('six'))
(en_yor.pop('six','eefa'))
'''
'''
#popitem()
#This removes the last key pair value
capitals1 = {'Nigeria':'Abuja','Ghana':'Accra','Togo':'Lome','South Africa':'Johannaseburg','Mali':'Bamako'}

print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
print(capitals.popitem())
#print(capitals.popitem())
print(capitals)
'''
'''
#how we can prevent the errors from passing non-existens keys using the membership operator
capitals = {'Nigeria':'Abuja','Ghana':'Accra','Togo':'Lome','South Africa':'Johannaseburg','Mali':'Bamako'}
if 'Rivers' in capitals:
    print(capitals['Rivers'])


#alternative, get()
capitals = {'Nigeria':'Abuja','Ghana':'Accra','Togo':'Lome','South Africa':'Johannaseburg','Mali':'Bamako'}
print(capitals.get('Nigeria'))


#Methods in Dictionaries
#copy();
capitals1 = {'Nigeria':'Abuja','Ghana':'Accra','Togo':'Lome','South Africa':'Johannaseburg','Mali':'Bamako'}
capitals2 = {'United Kingdom':'London','Russia':'Moscow','Sweden':'Stockholm'}
updating_dic = capitals1.update(capitals2)
print(updating_dic)
print(capitals1)
'''
#iterating over a dictionary:
#print all items in the updated capitals dictionacry
# capitals1 = {'Nigeria':'Abuja','Ghana':'Accra','Togo':'Lome','South Africa':'Johannaseburg','Mali':'Bamako'}
# for x,y in capitals1.items():
#     print(x,': ',y)

#conversion between Lists and Dictionaries:
capitals1 = {'Nigeria':'Abuja','Ghana':'Accra','Togo':'Lome','South Africa':'Johannaseburg','Mali':'Bamako'}
list1 = [capitals1]
print(list1)
print(type(list1))
print(list1[0])
