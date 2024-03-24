# The user will automatically get the diameter of the cell in the microscope image.
print("Welcome to your Image Assistant!")

# Formula to calculate the area of a circle (a cell in a 2D image is assumed to have a circular shape):
pi = 3.14159265358979
diameter = float(input("What is the diameter of the cell (measured in micrometers; add decimals)? "))  # Added 'float'function so the user can input numbers with decimals.
radius = diameter / 2
area = round((pi * radius * radius), 2)  # Fixed the formula (it was missing '* radius')

print(f"The area of your target of interest is: {area} square micrometers.")  # Area is expressed in square units, so I added 'square' to the string.


# Identification of the type of cell based on the diameter of the target identified:
if diameter > 40: 
  print("Your target of interest is most likely to be debris and is not a cell.")
elif diameter >= 30:
  print("Your target of interest is a SKBR3 cell.")
elif diameter >= 20: 
  print("Your target of interes is a HeLa cell.")
elif diameter >= 10:
  print("Your target of interest is a HaCaT cell.")
elif diameter >= 1:
  print("Your target of interest is a NSCLC cell.")
else:
  print("Your target of interest is most likely to be a fragment of a cell, a platelet, or debris. Your target is not a cell.")
# The order of the elif statements was not correct; the second and third one were interchanged. I change it to ensure the correct categorisation of the target.
# I added 'debris' to the print string of the 'else' statement, since it is possible that the user identifies a non-biological material too.