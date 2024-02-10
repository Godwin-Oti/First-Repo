#k="Hello world"
#print(k)

import numpy
arr=numpy.array([1,2,3,4,5])
print(arr)

import numpy as np 
x=np.array([9,8,7,6,5,4,3,2,1])
print(x)

import numpy as np
print(np.__version__)

import numpy as np 
arr= np.array([1,2,3,4])
print(arr)
print(type(arr))

import numpy as np 
arr=np.array((1,2,3,4,5))
print(arr)

import numpy as np
arr=np.array(42) # 0-D array
print(arr)

import numpy as np 
arr=np.array([1,2,3,4,5,6,7]) #uni-dimensional or 1-D array
print(arr)

import numpy as np
arr= np.array([[1,2,3,4],[5,6,7,8]]) #2-D array 
print(arr)

import numpy as np 
arr=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]) # 3-D  array
print(arr)


import numpy as np
a=np.array(90)
b=np.array([1,2,3,4])
c=np.array([[1,2,3],[4,5,6]])
d=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[3,4,5]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

import numpy as np 
arr=np.array([1,2,3,4],ndmin=5)
print(arr)
print("The number of array is increased to: ", arr.ndim)
