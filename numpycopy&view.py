import numpy as np 
arr=np.array([1,2,3,4,5])
x=arr.copy()
arr[0]=90
print(arr)
print(x)

import numpy as np 
arr=np.array([1,2,3,4,5])
d=arr.view()
arr[2]=50
print(arr)
print(d)

import numpy as np 
arr=np.array([1,2,3,4,5])
t=arr.view()
t[1]=40
print(arr)
print(t)

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
x=arr.reshape(2,4,2)
print(arr)
print(x)


import numpy as np 
arr=np.array([1,2,3,4,5])
x=arr.copy()
y=arr.view()
print(x.base)
print(y.base)

                                      ####shape######
import numpy as np 
arr=np.array([1,2,3,4])
print(arr)
print(arr.shape)

import numpy as np 
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr)
print(arr.shape)

import numpy as np 
arr=np.array([1,2,3,4,5],ndmin=5)
print(arr)
print(arr.shape)

import numpy as np 
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
mom=arr.reshape(3,4)
print(arr)
print(mom)

import numpy as np 
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
boy=arr.reshape(-1)
print(arr)
print(boy)

import numpy as np 
arr=np.array([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32])
pot=arr.reshape(2,4,-1)
print(arr)
print(pot)

