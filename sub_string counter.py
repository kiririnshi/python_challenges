def count_substring(string, sub_string):
    counter = 0
    for i in range(0, len(string)):
        if string[i] == sub_string[0]:    # and len(sub_string) > 1
            g = i
            for j in range (1, len(sub_string)):
                if len(string) > g+j:
                    #print(j)
                    if string[g+j] == sub_string[j]:
                        g += 1
            #print(f"Estas es g: {g} esta es i: {i}")  
            if (g - i == len(sub_string) - 2):
                counter = counter + 1
    print(counter)

count_substring("ABCDCDC", "CDC")