from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance

import matplotlib.pyplot as plt

def weightadj(Wold,m,diff):
 
 Wnew= Wold + m*diff
 
  
 return Wnew

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
a=np.array([[1,2,1,3],[2,1,3,4],[1,4,4,2],[2,3,4,3],[6,2,4,6],[4,2,4,1],[15,11,14,13],[19,12,16,11],[19,13,12,11],[18,11,13,13],[17,13,11,14],[18,11,14,11],[10,10,1,11],[11,11,12,12],[13,12,11,11]])
x=[1,2,1,2,6,4,15,19,19,18,17,18,10,11,13]
y=[2,1,4,3,2,2,11,12,13,11,13,11,10,11,12]
z=[1,3,4,4,4,4,14,16,12,13,11,14,1,12,11]
c=[3,4,2,3,6,1,13,11,11,13,14,11,11,12,11]
W=np.array([[0.1,0.2,0.1,0.3],[0.2,0.1,0.3,0.4],[0.1,0.4,0.4,0.2],[0.2,0.3,0.4,0.3],[0.6,2,0.4,0.6],[0.4,0.2,0.4,0.1],[5,0.1,0.94,0.3],[0.6,0.2,6,0.2],[0.9,0.30,0.2,0.1],[0.1,0.25,0.35,0.8]])
ax.scatter(x, y, z, c=c, cmap=plt.hot())
plt.title('Input Vectors')
plt.show()
i=0;
dmin=9999999999998;
win=1000;
m=1; 
y=0;
print "Initial W0",W[0]
print "Initial W1",W[1]
print "Initial W2",W[2]
print "Initial W3",W[3]
print "Initial W4",W[4]
print "Initial W5",W[5]
print "Initial W6",W[6]
print "Initial W7",W[7]
print "Initial W8",W[8]
print "Initial W9",W[9] 
#print W
for Z in range (0,5):
  
  m=m-0.19
   
  i=0
  y=0
   
  for y in range (0,15):
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
	if win > 0 and m > 0.61:
	 W[win-2]=weightadj(W[win-2],m,difference[win-2])	
    

	i=0 
	y=y+1
  
  Z=Z+1 
  y=0
  i=0


print "new W0",W[0]
print "new W1",W[1]
print "new W2",W[2]
print "new W3",W[3]
print "new W4",W[4]
print "new W5",W[5]
print "new W6",W[6]
print "new W7",W[7]
print "new W8",W[8]
print "new W9",W[9] 


 
x = []
y = []
z = []
c = []
for j in range (0,10):

   x1=W[j,0]
   x.append(x1)
   y1=W[j,1]
   y.append(y1)
   z1=W[j,2]
   z.append(z1)
   c1=W[j,3]
   c.append(c1)
   
   
   j=j+1



fig1 = plt.figure()
bx = fig1.add_subplot(111, projection='3d')
bx.scatter(x, y, z, c=c, cmap=plt.hot())
plt.title('Weights after self-organization')
plt.show()



   


 
