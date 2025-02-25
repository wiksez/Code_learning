weight = 41.5
cost = 0
cost_of_premium = 125.0

# Ground shipping

if weight <= 2:
    cost = weight * 1.5 + 20
elif weight <= 6:
    cost = weight * 3 + 20
elif weight <= 10:
    cost = weight * 4 + 20
else:
    cost = weight * 4.75 + 20
print("Ground Shipping price:", cost)
print("Ground Shipping Premium price:", cost_of_premium)
# Drone shipping

if weight <= 2:
    cost = weight * 4.5
elif weight <= 6:
    cost = weight *  9.0
elif weight <= 10:
    cost = weight * 12.0
else:
    cost = weight * 14.25

print("Drone Shipping price:", cost)