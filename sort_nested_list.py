records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name, score])

# [[p,1],[s,0.3],[d,0.3]]

second_highest = sorted(set([score for name, score in records]))[1]
print('\n'.join(sorted([name for name, score in records if score == second_highest]))) #Porque esto funciona???

#l1 = sorted(records, key= lambda x: x[1], reverse = True)
#last_place_mark = l1[-1][1]
#l2 = [x for x in l1 if x[1] != last_place_mark]
#second_place_mark = l2[-1][1]
#records.reverse()
#for n in records: # Sin sort para que esta wea no se equivoque
#    if (n[1] == second_place_mark):
#        print(n[0])

#print(records)