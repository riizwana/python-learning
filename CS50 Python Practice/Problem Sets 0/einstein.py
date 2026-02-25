# Firstly, I understand we need to ask the user for an interger in discretion of it being in kg
mass = int(input("What is mass in terms of kilograms?"))

# I am going to assume that this number is a constant for the mass to be times'd from
c = 300000000

# Now after getting the user's input and declaring c as a constant to be timed with, we can return it with * c
# * here would mean times as a % modular operator
E = mass * c * c

# Now we have to print out that result
print(E)
