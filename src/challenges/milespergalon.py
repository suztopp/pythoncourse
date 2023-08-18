import random

gallons_of_gas = random.randint(10, 25)
full_tank_miles = random.randint(200, 400)

# miles driven/gallons used

mpg = full_tank_miles // gallons_of_gas
print("MPG = ", mpg)

