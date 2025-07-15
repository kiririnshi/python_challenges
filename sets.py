# Enter your code here. Read input from STDIN. Print output to STDOUT

#a = input()
#m = input()
#b = input()
#n = input()


m = "2 4 5 9"
n = "2 4 11 12"

m_set = set(m.split())
n_set = set(n.split())

n1 = m_set.difference(n_set)
n2 = n_set.difference(m_set)

#newlis = list(n1.union(n2))
newlis = list(map(int, n1.union(n2)))

newlis.sort() # Sort siempre se hace in-place, asi que no crea un nuevo objeto cuando se usa.

for i in newlis:
    print(i)

#symetric_d = []
#for i in m_set:
#    for j in n_set:
#        if i == j:
#            symetric_d.append(j)
#print(symetric_d)



n = 7
countries = "UK, China, USA, France, New Zealand, UK, France" 
countries = countries.split(",")
s = set(countries)
#for i in range(n):
#    countries.add(input())

print(len(s))