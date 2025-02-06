#Write a function that computes the volume 
# of a sphere given its radius.

import math

def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)

# Example usage
r = float(input("Enter the radius of the sphere: "))
print(sphere_volume(r))

# 9- output 3053.6280592892786