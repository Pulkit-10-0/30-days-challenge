import numpy as np 

np1 = np.array([1,2,3,4,5,6,7,8,9,10])

x = np.where(np1 ==3)
print(x)


#retunr even items 

y = np.where(np1%2 == 0)
print(y)
 