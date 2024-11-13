import numpy as np 
np1 = np.array([0,1,2,3,4,5])

#create a view 
np2 = np1.view()

print(f'original np1  - {np1}')
print(f'original np2  - {np2}')

np1[0] = 41

print(f'changed np1  - {np1}')
print(f'original np2  - {np2}')

#create a copy 
print(" ")

np5 = np.array([0,1,2,3,4,5])

np3 = np1.copy()

print(f'original np5  - {np5}')
print(f'original np3  - {np3}')

np5[0] = 41

print(f'changed np5  - {np5}')
print(f'original np3  - {np3}')
