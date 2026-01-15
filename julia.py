import numpy as np
import matplotlib.pyplot as plt

# Image size
width,height=800,800
max_iter=100
c=complex(-0.4,0.6)

# Create image
image=np.zeros((height,width))

for x in range(width):
    for y in range(height):
        # Map pixel to complex plane
        zx=(x-width/2)*4/width
        zy=(y-height/2)*4/height
        z=complex(zx,zy)
        count=0
        while abs(z)<=2 and count<max_iter:
            z=z*z+c
            count+=1

        image[y,x]=count

plt.figure(figsize=(6,6))
plt.imshow(image,cmap="hot")
plt.axis("off")
plt.show()
