# Bar Graph vertical
import numpy as np
import matplotlib.pyplot as plt
x1=np.array(['A','B','C','D'])
y1=np.array([3,6,2,4])
plt.bar(x1,y1,width=0.2,color='red')
plt.show()


#Bar Graph Horizental
import numpy as np
import matplotlib.pyplot as plt
x1=np.array([3,6,2,4])
y1=np.array(['A','B','C','D'])
plt.barh(y1,x1,height=0.5,color='red')
plt.show()
