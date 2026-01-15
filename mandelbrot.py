import numpy as np
import matplotlib.pyplot as plt

width,height=800,800
max_iter=100

image=np.zeros((width,height))

for x in range(width):
    for y in range(height):
        a=(x-width/2)*4/width
        b=(y-height/2)*4/height
        c=complex(a,b)
        z=0
        count=0
        while abs(z)<=2 and count<=max_iter:
            z=z**2+c
            count+=1
        image[x,y]=count

plt.figure(figsize=[6,6])
plt.imshow(image,cmap="twilight")
plt.axis("off")
plt.show()
        
