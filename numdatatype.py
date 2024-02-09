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