#by using numpy create array
import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))
arr=np.array([[1,2,3],[4,5,6]])
print(arr[0][2])
arr=np.array([[1,2,3]])
print(arr[0])
a=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a.ndim)

#ndmin=n dimension
a=np.array(([2,4,6,8]),ndmin=4)
print(a)
print(a.ndim)



#matplotlib-data visualization
#2d graphics-line graph,scatler,multiplot/subplot,bar graph,histragrams,pie chart

import matplotlib.pyplot as plt
import numpy as np
xpts=np.array([0,5,10,15,20])
ypts=np.array([5,10,6,12,5])
#default xpts,ypts.starting  
plt.plot(ypts)
plt.show()
