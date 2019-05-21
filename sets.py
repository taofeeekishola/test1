#Sets can not have repeated items
#well definined collections of objects
#creating sets
'''
x = set('A python set')
#print(x)
print(type(x))

#passed a list to the inbuilt set function
y = set(['Python','C++','Java','JavaScript','PHP'])
print(y)

#when a tuple contains repeated items is passed to the set() function
states = set(('Lagos','Benin','Onistisha','Kaduna','Benin','Bayeslsa'))
states.add('Rivers')
print(states)

#we cannot include mutable objects during set creation
#classes = set('Js1',['Js2','Js3','SS1'],'ss2','ss3')

#frozen sets: they are immutable
food = frozenset(['Egg','Jam','Bread',True])
print(food)
#print(food.add('water'))

#using the curly braces
states = {'Lagos','Benin','Onistisha','Kaduna','Benin','Bayeslsa'}
print(states)
'''
'''
#Set Operations
#add():to add an item to a set
colors = {'Red','Green','Blue'}
print(colors.add('Green'))
print(colors)

#clear():used to clear a whole set
states = {'Lagos','Benin','Onistisha','Kaduna','Benin','Bayeslsa'}
#print(states.clear())
print(states)

#remove():for removing a single item from a set
print(states.remove('Benin'))
print(states)
'''
'''
#copy
more_states = {'Ogun','Imo','Nasawara','Kaduna','Adamawa'}
more_states_backup = more_states.copy()
print(more_states_backup)
'''
'''
#differences
A = {'Tomi','Daniel','Ejito','Salah'}
B = {'Daniel','Mohammed','Bolaji','Kayode'}
#print(A-B)
print(A.difference(B))
#print(B-A)
print(B.difference(A))
'''
'''
#difference_update()#this is used to relace the set it is operating on
x = {'a','b','c','d','e','f','g'}
y = {'c','f','b'}
z = {'e','d','t','o'}
print((x-y-z))
x.difference_update(y)
print(x)
'''
#discard():removes an item and if it doesn't exist it doesnt give an error
x = {'a','b','c','d','e','f','g'}
x.discard('o')
print(x)

#intersection
x = {'a','b','c','d','e'}
y = {'c','d','e','f','g'}
print(x & (y))
print(x.union(y))

#disjoint method
print(x.isdisjoint(y))

#subset
x = {'a','b','c','d','e'}
y = {'c','d'}
print(x < y)# is 'x' a subset of 'y'
print(x.issubset(y))
print(y < x)#is 'y' a subset of 'x'
print(y.issubset(x))
print('SuperSet')
print(x.issuperset(y))
print(len(x))
print(max(x))