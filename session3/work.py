list_quan_ao = ['not sweater' , 'pant' , 'hoodie', 'new clothes']
len_list_quan_ao = len(list_quan_ao)
for i in list_quan_ao: 
    print(list_quan_ao.index(i)+1, end= '')   #have to number them later
    print('',i)
welcome_question = input('welcome to our shop, what do you want? (C R U D)')


if welcome_question == C:
    list_quan_ao.append(input('what would you like to add'))
        print(list_quan_ao)
    elif welcome_question == R:
        list_quan_ao.remove(input('what would you like to remove'))
        print(list_quan_ao)
    elif welcome_question == U:
        list_quan_ao.[index]
        print(list_quan_ao)

else:  #this is for D
    list_quan_ao.pop(0)
        print(list_quan_ao)
