

arr = [1,2,3,5,6]

max_n = -1
for x in arr:
    if x > max_n:
        max_n = x

new_max_n = -1
for y in arr:
    if (y > new_max_n and y != max_n):
        new_max_n = y    
print(new_max_n)