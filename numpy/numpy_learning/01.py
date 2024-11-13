import numpy as np  
np1 = np.array([0,1,2,3,4,5,6,7,8,9])
print(np1)
print(np1.shape)

np2 = np.arange(0,10,2)
print(np2)

np4 = np.zeros(10)
print(np4)

# multi dimmmenstional zeros
np5 = np.zeros((2,10))
print(np5)


np6 = np.full((10),6)
print(np6)

#multi dimensional full 
np7 = np.full((2,10),6)
print(np7)


# convert list to np
my_list = [1,2,3,4,5]
np8 = np.array(my_list)
print(np8)



