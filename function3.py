#Write a program to solve a classic puzzle:
# We count 35 heads and 94 legs among the 
# chickens and rabbits in a farm. 
# How many rabbits and how many chickens do we have?
# create function: solve(numheads, numlegs):

def solve(numheads, numlegs):
    for chicken in range (numheads+1):
        rabbits = numheads-chicken
        if(2*chicken+4*rabbits)==numlegs:
            return chicken, rabbits
    return "NO solution"
print(solve(35,94))

#output (23, 12)