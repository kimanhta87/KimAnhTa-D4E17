months_number = int(input('please input number of months: '))

sheep = [5,7,300,90,24,50,75]
print('hello,my name is Hiep and these are my sheep sizes', sheep)


for i in range (1, months_number+1):

    new_list = [ sheep_size+50 for sheep_size in sheep ]

    print('MONTH', i ,':')
    print('One month has passed, now here is my flock', new_list)

    new_list.sort()
    print('Now my biggest sheep has size', new_list[-1] , 'lets shear it')

    default_size = 8

    sheep[-1] = default_size

    new_list.sort()

    print('after shearing, here is my flock')
    print(new_list)

