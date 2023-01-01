import pandas as pd
s=pd.Series([11,22,33,44],index=['A','B','C','D'])
print(s)


#series from array
import numpy as np
a=np.array([11,22,33,44])
s=pd.Series(a,index=['A','B','C','b'])
print(s)
d={'a':100,'b':20,'c':30}
w=pd.Series(d)
print(w)


#dataframe
a=pd.DataFrame()
print(a)


# one colume
q=np.array([10,20,30,40])
s=pd.DataFrame(q)
print(s)

#multiple colume
q=np.array([10,20,30,40])
q1=np.array([10,20,30,40])
q3=np.array([10,20,30,40])
p=pd.DataFrame([q,q1,q3])
print(p)



q=pd.Series([10,20,30],index=['maths','science','Eng'])
q1=pd.Series([10,20,30],index=['maths','science','Eng'])

p=pd.DataFrame([q,q1],index=['term1','term2'])
print(p)
