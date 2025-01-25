import math 
#prompt insert of cylinder diameter 
diameter = float(input("Enter the diameter of the cylinder: "))
#prompt insert of cylinder height
height = float(input("Enter the height of the cylinder: "))
pi = round(math.pi,2)
#Calculate the radius of the cylinder's circular end.
radius = diameter/2
#Calculate the volume of the cylinder.
volume = pi * radius ** 2 * height
print(f'The volume of the cylinder is: {volume:.2f}')