if __name__ == '__main__':
    s = "#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000"
    
    #if s.isalnum():
        #print(s.isalnum())
    flag_0 = False
    flag_1 = False
    flag_2 = False
    flag_3 = False
    flag_4 = False
    for i in range(len(s)):
        if s[i].isalnum():
            flag_0 = True
        if s[i].isalpha():
            flag_1 = True
        if s[i].isdigit():
            flag_2 = True
        if s[i].islower():
            flag_3 = True
        if s[i].isupper():
            flag_4 = True
    print(flag_0)
    print(flag_1)
    print(flag_2)
    print(flag_3)
    print(flag_4)
    #else:
    #    print(False)
    #    print(False)
    #    print(False)
    #    print(False)
    #    print(False)
