"""
Author: Rodrigo Arguello
"""
print("This program assumes all items have the same chance of being randomly selected.")
n = int(input("How many items are available? "))
probability = 1
m = n - 1
c = 1
while(1 - probability < 0.5):
    probability *= (m/n)
    m -= 1
    c += 1
print("You'd need",c,"items to ensure randomly picking another item has a >50% of a collision.")
while(1 - probability < 0.75):
    probability *= (m/n)
    m -= 1
    c += 1
print("You'd need",c,"items to ensure randomly picking another item has a >75% of a collision.")
while(1 - probability < 0.999):
    probability *= (m/n)
    m -= 1
    c += 1
print("You'd need",c,"items to ensure randomly picking another item has a >99.9% of a collision.")
