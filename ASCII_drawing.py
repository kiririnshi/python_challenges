
thickness = 5 #This must be an odd number
c = 'H'

#Top Cone
#for i in range(1,thickness+1):
    #new_c = c*i
#    print(
#        ((i)*"H").center(20," ")
#    )
    #(thickness-1)+c+(c*i)"______"(thickness-1))

#width = 30

#s_left = thickness*c

#left = s_left.ljust(width," ")

#print(left)

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))