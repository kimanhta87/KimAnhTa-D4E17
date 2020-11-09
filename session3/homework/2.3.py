sheep = [5,7,300,90,24,50,75]
print('hello,my name is Hiep and these are my sheep sizes', sheep)

sheep.sort()
print('Now my biggest sheep has size', sheep[-1] , 'lets shear it')

default_size = 8

sheep[-1] = default_size

sheep.sort()

print('after shearing, here is my flock')
print(sheep)


