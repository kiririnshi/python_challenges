

x = 1 
y = 1 
z = 3
n = 3

#perm_list_x = [x for x in range(x+1)] ** [y for y in range(y+1)]
#perm_list_y = [y for y in range(y+1)]
#perm_list_z = [z for z in range(z+1)]

perm_list = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

#perm_list = []
#for i in range(x+1):
#    for j in range(y+1):
#        for k in range(z+1):
#            perm_list.append([i,j,k])

print(perm_list)


#new_perm_list = [i for i in perm_list if i[0] + i[1] + i[2] != n]

#new_perm_list = []

#for i in perm_list:
#    if i[0] + i[1] + i[2] != 3:
#        new_perm_list.append(i)

#print(new_perm_list)
