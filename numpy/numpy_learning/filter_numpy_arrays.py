import numpy as np 

np1 = np.array([1,2,3,4,5,6,7,8,9,10])

x = ([True,True,False,False,False,False,False,False,False,False])

print(np1)
print(np1[x])

filtered = []
for thing in np1:
    if thing %2 == 0:
        filtered.append(True)
    else:
         
        filtered.append(False)

print(np1) 
print(filtered)
new = np1[filtered]
print(np1[filtered])       

#alternate shortcut


print(" ")
sfilterd = np1 %2 ==0
print(" ")

print(np1)
print(" ")


print(sfilterd)

print(" ")
print(np1[sfilterd])
