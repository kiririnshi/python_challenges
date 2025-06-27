import math

ab = input("Enter AB")
bc = input("Enter BC")

ab = int(ab)
bc = int(bc)

ac = math.sqrt(ab*ab + bc*bc)
bm = (ab*bc)/ac

#breakpoint()

angle_mcb = math.atan(bc/ab)
angle_mcb = math.degrees(angle_mcb)
print(round(angle_mcb))
angle_mbc = 90 - angle_mcb

print(angle_mbc)
