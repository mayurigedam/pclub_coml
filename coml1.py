import numpy as np
import math
from scipy.interpolate import lagrange
e1,e2,e3,e4={},{},{},{}
for i in range(2,11,1):
	x=np.linspace(-1,1,num=i)
	y1=np.sin(x)
	y2=np.sin(abs(x))
	y3=np.sin(x*np.sqrt(abs(x)))
	y4=1/(1+(x**2))

	e1[i]=np.max(abs(lagrange(x,y1)(x)-x))
	e2[i]=np.max(abs(lagrange(x,y2)(x)-x))
	e3[i]=np.max(abs(lagrange(x,y3)(x)-x))
	e4[i]=np.max(abs(lagrange(x,y4)(x)-x))
for i in range(2,11,1):
	if(i==2):
		e1[i]=(e1[i],0)
		e2[i]=(e2[i],0)
		e3[i]=(e3[i],0)
		e4[i]=(e4[i],0)

	else:
		e1[i]=(e1[i],math.log(e1[i]/e1[i-1][0])/math.log(i/(i-1)))
		e2[i]=(e2[i],math.log(e2[i]/e2[i-1][0])/math.log(i/(i-1)))
		e3[i]=(e3[i],math.log(e3[i]/e3[i-1][0])/math.log(i/(i-1)))
		e4[i]=(e4[i],math.log(e4[i]/e4[i-1][0])/math.log(i/(i-1)))
for i in range(2,11,1):
	print (str(i)+"|"+str(e1[i][0])+"\t"+str(e1[i][1])+"|"+str(e2[i][0])+"\t"+str(e2[i][1])+"|"+str(e3[i][0])+"\t"+str(e3[i][1])+"|"+str(e4[i][0])+"\t"+str(e4[i][1]))