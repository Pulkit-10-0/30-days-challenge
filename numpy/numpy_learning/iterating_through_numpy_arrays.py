import numpy as np 

#1-D

np1 = np.array([1,2,3,4,5,6,7,8,9,10])

for x in np1:
    print(x)


print(" ")


# 2-D
print(" ")

np2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
for x in np2:
    for y in x:
        print(y)


print(" ")

# 3-D
print(" ")

np3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in np3:
    for y in x:
        for z in y:
            print(z)

#alternate method 

#use np.nditer()
print(" ")

np4 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in np.nditer(np4):
    print(x)