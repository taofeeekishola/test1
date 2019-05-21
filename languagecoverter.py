print('Programm for Coverting Ibo, Yoruba and English')

print('Enter 1 for Igbo conversion')
print('Enter 2 for Yoruba conversion')
print('Enter 3 for English conversion')

numb = float(input('Enter number: '))

if (numb == 1):
    eng_yor = {'One':'Ookan','Two':'Eeji','Three':'Eeta','Four':'Eerin','Five':'Aarun'}
    yor_ibo = {'Ookan':'Otu','Eeji':'Abo','Eeta':'Ato','Eerin':'Ano','Aarun':'Ise'}

    eng = input('Enter English: ')
    print('Yoruba: ',eng_yor[eng])
    print('Igbo: ',yor_ibo[eng_yor[eng]])
elif (numb == 2):
    yor_eng = {'Ookan':'One','Eeji':'Two','Eeta':'Three','Eerin':'Four','Aarun':'Five'}
    eng_ibo = {'One':'Otu','Two':'Abo','Three':'Ato','Four':'Ano','Five':'Ise'}

    yor = input('Enter Yoruba: ')
    print('English: ',yor_eng[yor])
    print('Igbo: ',eng_ibo[yor_eng[yor]])
elif (numb == 3):
    ibo_eng = {'Otu':'One','Abo':'Two','Ato':'Three','Ano':'Four','Ise':'Five'}
    eng_yor = {'One':'Ookan','Two':'Eeji','Three':'Eeta','Four':'Eerin','Five':'Aarun'}

    ibo = input('Enter Ibgo: ')
    print('English: ',ibo_eng[ibo])
    print('Yoruba: ',eng_yor[ibo_eng[ibo]])
# else:
#     print('Please Pick between 1 and 3')
