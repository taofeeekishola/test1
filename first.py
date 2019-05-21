#Strings in python
name= "Ishola Taofeek"
print(name[7])

'''
#Python Strings are immutable. Meaning they cant be changed once assigned.
name[7]="C
'''
'''
#Python Strings can be converted
num = "55"
int(num)
print(type(num))
'''

'''
#Object Referencing
x="blue"
y="green"
z=x
#print(x,y,z)

'''

'''
#We can rebind variable
z=y
print(x,y,z)

x=z
print(x,y,z)
'''

'''
Collection Data Types
1. Lists: -mutable
'''
#days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
#days[0]='Aje'
#print(days)

#words = ['book',False, 'Wednesday', 234]
#words[2] = True
#print(words)

#2. Tuples - unmutable
#countries = ("Nigeria", "England", "Togo", "Australia")
#countries[2] = "Lagos"

#print(countries)

#python sequence types are sized - they can be passed to the Len() function
#print(len("Bolaji"))
#print(len(["Monday", "Tuesday", False, 501]))

#more elements can be added to a list using .append
true="God is Good"
x = ["Zebra", 49 , -987, "Monkey", true]
x.append("more")
print(x)

