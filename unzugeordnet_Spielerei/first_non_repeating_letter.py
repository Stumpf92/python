def first_non_repeating_letter(string):
    
    if len(string) == 1:
        return string
    
    if len(string) > 1:
        dic = {}
        for i in range(len(string)):
            if string[i] in dic:
                dic[string[i]] = dic[string[i]] +1
            else:    
                dic[string[i]] = 1

        keys = [k for k, v in dic.items() if v == 1 ]
        
        

        return keys[0]


first_non_repeating_letter("aBBa")