from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.spatial import distance

import matplotlib.pyplot as plt

def Distancesqr(a):
  return a * a
  

def weightadj(Wold,m,diff):
 
 Wnew= Wold + m*diff
 
  
 return Wnew

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
a=np.array([[1,2,1,2,3,1],[1,1,2,1,3,4],[1,1,1,4,4,2],[1,1,2,3,4,3],[1,1,6,2,4,6],[1,1,4,2,4,1],[12,13,15,11,14,13],[19,12,13,12,16,11],[15,13,19,13,12,11],[17,19,18,11,13,13]])
W=np.array([[0.1,0.2,0.1,0.2,0.1,0.3],[0.1,0.4,0.2,0.1,0.3,0.4],[0.5,0.8,0.1,0.4,0.4,0.2],[0.7,0.5,0.2,0.3,0.4,0.3],[8,5,6,2,0.4,0.6],[0.4,0.6,0.4,0.2,0.4,0.1],[5,0.4,0.5,0.1,0.94,0.3],[0.6,0.2,6,0.2,0.5,0.7],[0.12,0.9,0.30,0.2,0.1,0.3],[0.1,0.25,0.35,0.8,0.8,0.9]])

i=0;
dmin=9999999999998;
win=1000;
m=1; 
y=0

print "*******************Squared distance between weights before self Organization************************ "
for i in range (0,10):
 
    for j in range (0,10):
	  s=f=0;
	  f=distance.euclidean(W[i],W[j])
	  s= Distancesqr(f)
	  print "W",i,j, " squared euclidean distance = " , s;

i=0;
dmin=9999999999998;
win=1000;
m=1; 
y=0

for Z in range (0,5):
  
  m=m-0.19
  print m 
  i=0
  y=0
  
   
  for y in range (0,10):
	difference=[]
	Wnew=[]
	dist=[]
    
     
	for x in range (0,10):
	  diff = a[y] - W[i];
	  difference.append(diff);
	   
	  dst = distance.euclidean(a[y],W[i]); 
	  dist.append(dst);
	  
	  if dmin > dst:
		dmin=dst
		win=i
      
	  i=i+1;

      
	W[win]=weightadj(W[win],m,difference[win])
	
	if win < 9 and m > 0.42:
	 
	 W[win+1]=weightadj(W[win+1],m,difference[win+1])
	if win > 0 and m > 0.42: 
	 W[win-1]=weightadj(W[win-1],m,difference[win-1])
	if win < 8 and m > 0.61:
	 W[win+2]=weightadj(W[win+2],m,difference[win+2])
	if win > 1 and m > 0.61:
	 W[win-2]=weightadj(W[win-2],m,difference[win-2])	
    

	i=0 
	y=y+1
  
  Z=Z+1 
  y=0
  i=0


print "*******************Squared distance between weights after self Organization************************ "


for i in range (0,10):
 
    for j in range (0,10):
	  s=f=0;
	  f=distance.euclidean(W[i],W[j])
	  s= Distancesqr(f)
	  print "W",i,j, " squared euclidean distance = " , s;

 


   


 
