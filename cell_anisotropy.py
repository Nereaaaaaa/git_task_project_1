print("Welcome to Celltropy, a program to calculate cell anisotropy")
length = float(input("Please enter the measure of length of your target of interest (in micrometers; one decimal): "))
width = float(input("Please enter the measure of width of your target of interest (in micrometers; one decimal): "))
anisotropy = width/length
print(f"The anisotropy measure of your target of interest is: {anisotropy}")