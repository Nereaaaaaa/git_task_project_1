# I created a code to calculate the area of a cell and to identify the type of cell from a 2D image.
# The user will automatically get the diameter of the cell in the microscope image.

# Formula to calculate the area of a circle (a cell in a 2D image is assumed to have a circular shape):
pi = 3.14159265358979
diameter = float(input("What is the diameter of the cell (measured in micrometers; add decimals)? "))
radius = diameter / 2
area = round((pi * radius), 2)
# Logical error 1: the formula to calculate the area should be 'pi * radius * radius' instead of 'pi * radius'.

print(f"The area of your target of interest is: {area} micrometers.") 
# Logical error 2: the sentence should include 'square micrometers' instead of 'micrometers'.


# Identification of the type of cell based on the diameter of the target identified:
if diameter > 40: 
  print("Your target of interest is most likely to be debris and is not a cell.")
elif diameter >= 20:
  print("Your target of interest is a SKBR3 cell.")
elif diameter >= 30: 
  print("Your target of interes is a HeLa cell.")
elif diameter >= 10:
  print("Your target of interest is a HaCaT cell.")
elif diameter >= 1:
  print("Your target of interest is a NSCLC cell.")
else:
  print("Your target of interest is most likely to be a fragment of a cell or a platelet and not a cell.")
# Logical error 3: the order of the elif statements is not correct; the second and third one should be interchanged to ensure the correct categorisation of the target. 
# Logical error 4: if the diameter of the target of interest is less than 1, then the target identified could be 'debris, a fragment of a cell or a platelet and not a cell', not just 'a fragment of a cell or a platelet and not a cell'.