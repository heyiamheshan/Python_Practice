import numpy as np

weights=np.array([0.5,0.4,0.07,0.03])
marks =np.array([[70,60,50,40],[40,50,20,10],[90,80,90,70]])

final =marks*weights
print("Final marks:\n",final)