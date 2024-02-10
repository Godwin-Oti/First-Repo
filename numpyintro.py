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

                                           ###NUMPY INDEXING

import numpy as np 
arr=np.array([1,2,3,4,5])
print(arr.dtype)

import numpy as np 
arr=np.array(["Ben", "West","Dret"])
print(arr.dtype) 

import numpy as np 
arr=np.array([1,2,3,4], dtype= "S")
print(arr)
print(arr.dtype)

import numpy as np 
arr=np.array([1,2,3,4], dtype= "i4")
print(arr)
print(arr.dtype)

import numpy as np 
arr=np.array([1.2,2.1,3.2,4.3])
varr=arr.astype(int)
print(varr)
print(varr.dtype)

import numpy as np  
arr=np.array([1,2,3,4,5])
varr=arr.astype("f")
print(varr)
print(varr.dtype)

import numpy as np 
arr=np.array([1,0,2,0,3,0,4])
x=arr.astype(bool)
c=arr.astype("b")
print(x)
print(x.dtype)
print(c)
print(c.dtype)

                                           ###NUMPY DATATPYE

import numpy as np 
arr=np.array([1,2,3,4,5])
print(arr.dtype)

import numpy as np 
arr=np.array(["Ben", "West","Dret"])
print(arr.dtype) 

import numpy as np 
arr=np.array([1,2,3,4], dtype= "S")
print(arr)
print(arr.dtype)

import numpy as np 
arr=np.array([1,2,3,4], dtype= "i4")
print(arr)
print(arr.dtype)

import numpy as np 
arr=np.array([1.2,2.1,3.2,4.3])
varr=arr.astype(int)
print(varr)
print(varr.dtype)

import numpy as np  
arr=np.array([1,2,3,4,5])
varr=arr.astype("f")
print(varr)
print(varr.dtype)

import numpy as np 
arr=np.array([1,0,2,0,3,0,4])
x=arr.astype(bool)
c=arr.astype("b")
print(x)
print(x.dtype)
print(c)
print(c.dtype)

                                 ##COPY AND VIEW
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


                                        ### SLICING IN NUMPY
import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr[1:4])

import numpy as np
arr=np.array([1,2,3,4,5,6,7])
print(arr[:5])

import numpy as np
arr=np.array([2,4,6,8,10,12,14])
print(arr[1:5:2])

import numpy as np 
arr=np.array([1,2,3,4,5,6,7,8,9])
print(arr[::3])

import numpy as np 
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr[1,1:3])

import numpy as np 
arr=np.array([[2,4,6,8],[1,2,3,4]])
print(arr[0:2,3])

import numpy as np 
arr=np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
print(arr[0:2,1:5 ])

                                        ###  ITERATION IN ARRAY
import numpy as np 
arr=np.array([1,2,3,4]) #1-D array
for x in arr:
  print(x)

import numpy as np 
arr=np.array([[1,2,3,4],[5,6,7,8]]) #2-D array
for x in arr: 
  print(x)

import numpy as np 
arr=np.array([[1,2,3],[4,5,6]]) #loopnig through each value in a D
for x in arr:
  for y in x:
    print(y)

import numpy as np 
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
  for y in x:
    for z in y:
      print(z)

import numpy as np 
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in np.nditer(arr):
  print(x)

import numpy as np 
arr=np.array([1,2,3,4,5])
for x in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
  print(x) 

import numpy as np 
arr=np.array([[1,2,3],[4,5,6]])
for x in np.nditer(arr [:, ::2]):
  print(x)

import numpy as np 
arr=np.array([1,2,3,4])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

import numpy as np
arr=np.array([[[1,2,3],[4,5,6]]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)



