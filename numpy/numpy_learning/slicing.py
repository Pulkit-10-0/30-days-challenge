import numpy as np 

#slicing numpy array

np1 = np.array([1,2,3,4,5,6,7,8,9,])

#return 2,3,4,5,
print(np1[1:5])


#return from something till the end 

print(np1[3:])

#return negative slices

print(np1[-3:-1])

#steps 

print(np1[1:5:2])

#reverse

print(np1[::-1])

#steps on compelte array
print(np1[::2])


#slice a 2d array 

np2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
#pulling a single item
print(np2[1,2])

#slice 2d array
print(np2[0:1, 1:3])

#slice from both rows 
print(np2[0:2,1:3])

