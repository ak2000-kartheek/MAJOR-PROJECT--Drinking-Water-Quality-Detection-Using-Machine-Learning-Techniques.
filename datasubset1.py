#This plot is generated by considering a subset of 500 rows, and the last two columns from the dataset.
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(6)
import math
X = np.genfromtxt('qualitysubset.csv', delimiter=',', dtype=np.int32)
X1 = X[:,:-1]  #First n columns(except last colun) are assigned to X1
X2 = X[:, -1]  #Last coulmn is assigned to X2
cnt1 = (X1[:,0]== 0).sum() #Number of '0's in first column
cnt2 = (X1[:,0]== 1).sum() #Number of '1's in first column
cnt3 = (X2 == 0).sum() #Number of '0's in last column
cnt4 = (X2 == 1).sum() #Number of '1's in last column
cnt5 = (X2 == 2).sum() #Number of '2's in last column

x = ['NoFlourides', 'Flourides','Good', 'Poor','very Poor']
y = [cnt1,cnt2,cnt3,cnt4,cnt5]

fig, ax = plt.subplots()    
width = 0.75 # the width of the bars 
ind = np.arange(len(y))  # the x locations for the groups
ax.barh(ind, y, width, color="blue")
ax.set_yticks(ind+width/2)
ax.set_yticklabels(x, minor=False)
for i, v in enumerate(y):
    ax.text(v + 3, i + .25, str(v), color='blue', fontweight='bold')
plt.title('Flourides vs. Water Quality')
plt.xlabel('x')
plt.ylabel('y')      
plt.show()
#plt.savefig(os.path.join('test.png'), dpi=300, format='png', bbox_inches='tight') # use format='svg' or 'pdf' for vectorial pictures