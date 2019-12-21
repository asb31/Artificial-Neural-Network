import numpy as np
from scipy.spatial import distance

import matplotlib.pyplot as plt

def weightadj(Wold,m,diff):
 #
 Wnew= Wold + m*diff
 
  
 return Wnew
 

a=np.array([[2,4],[3,2],[2.5,3],[2.4,1],[0.2,0.5],[0.12,0.15],[13,15],[12.5,16],[13.5,17],[16,17],[15.5,14],[5,7],[4,8],[14,15],[17,15]])
b=(4,5)
W=np.array([[0.2,0.3],[0.24,0.35],[0.15,0.25],[0.66,0.37],[0.73,0.529],[0.6,0.3],[0.1,0.24],[0.1,0.25],[0.23,0.15],[0.25,0.27]]) #weights
g=plt.figure(1)
plt.title('Input Vectors')
plt.plot(a.T[0:1, :], a.T[1:2, :], 'ko',marker = 'x')
plt.xlim(0,20)
plt.ylim(0,20)
g.show()
f=plt.figure(2)
plt.plot(W.T[0:1, :], W.T[1:2, :], 'ko',marker = 'o')
plt.title('Initial Weights')
plt.xlim(0,20)
plt.ylim(0,20)
f.show()



i=0;
dmin=9999999999998;
win=1000;
m=1; 
y=0

for Z in range (0,5):
  
  m=m-0.19
   
  i=0
  y=0
  #plt.plot(W.T[0:1, :], W.T[1:2, :], 'ko')
  #plt.title('iteration++') 
  #plt.show() 
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
b=plt.figure(3) 
plt.plot(W.T[0:1, :], W.T[1:2, :], 'ko')
plt.xlim(0,20)
plt.ylim(0,20)
plt.title('Weights after self-organisation')
b=plt.show()




   
 
 
 
