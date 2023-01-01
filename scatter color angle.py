#Scatter
import numpy as np
import matplotlib.pyplot as plt
x=np.array([35,50,100,60])
#Labels
mylbl=('Apple','Orange','cherry','Banana')
#Explode 
ex=[0.2,0,0,0]
plt.pie(x,labels=mylbl, startangle=90 ,explode=ex,shadow='True')
plt.legend(title='fruits')
#colors
clr=['black','yellow','red','white']
plt.show()
