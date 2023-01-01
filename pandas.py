#What is a Series and how is it different from a 1-D array, a list and a dictionary? 

import pandas as pd
import numpy as np
ser=pd.Series([11,22,33,44])
print(ser)




#Series from array
import pandas as pd
import numpy as np
ar=np.array([35,40,60,80])
ser=pd.series(ar,index=[2,7,8,10])





