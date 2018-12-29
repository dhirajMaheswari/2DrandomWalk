'''
This code simulates the random walk (or walk of a drunk man) in two dimensions.
It considers that each step is 1 unit long (which can be obviously changed to be random,
depending on how drunk the man is). It makes use of the randomly drawn integers to determine
the next step.
'''


import numpy as np
import matplotlib.pyplot as plt
import random 
  
# defining the number of steps 
n = 1000
  
#creating two array for containing x and y coordinate 
#of size equals to the number of size and filled up with 0's 
x = np.zeros(n) 
y = np.zeros(n) 
  
# filling the coordinates with random variables 
for i in range(1, n): 
    val = random.randint(1, 4) 
    if val == 1: 
        # move forward by one step relative to prev position
        # (try modifying this with random length steps) 
        x[i] = x[i - 1] + 1 
        y[i] = y[i - 1] 
    elif val == 2: 
        x[i] = x[i - 1] - 1  # move backward
        y[i] = y[i - 1] 
    elif val == 3: 
        x[i] = x[i - 1] 
        y[i] = y[i - 1] + 1
    else: 
        x[i] = x[i - 1] 
        y[i] = y[i - 1] - 1
      
  
# plotting stuff: 
plt.rc('text', usetex=True) # for LaTeX

plt.title("Random walk with "+ str(n) + " steps")
plt.xlabel(r'\textbf{$\vec{x}$} direction', fontsize = 16, color = 'blue') # some TeX rendering in labels
plt.ylabel(r'\textbf{$\vec{y}$} direction', fontsize=16, color='blue')

#plt.scatter(x, y, color='red',marker='*') 
plt.plot(x, y, color='red',marker='*') 
plt.text(x[0],y[0], 'start')


plt.text(x[n-1], y[n-1], 'end')
#plt.grid()
plt.show()
