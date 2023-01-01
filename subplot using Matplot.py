#subplot(multiple Graph)
#Plot 1

import numpy as np
import matplotlib.pyplot as plt
y1=np.array([1,5,10,15,20])
plt.subplot(1,2,1)
plt.title('graph1')
plt.plot(y1)

#Plot 2

y2=np.array([20,25,30,35,40])
plt.subplot(1,2,2)
plt.title('graph2')
plt.plot(y2)
plt.show()
