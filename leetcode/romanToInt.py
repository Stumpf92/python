
def romanToInt(s: str) -> int:
    counter = 0
    while len(s) >0 :
        if s[-1:] == 'I':
            print('1+')
            counter += 1
            s = s[:-1]
        if len(s) >=2:
            if s[-1] == 'V' and s[-2] == 'I':
                print('4+')
                counter += 4
                s = s[:-1]
                s = s[:-1]
        if s[-1:] == 'V':
            print('5+')
            counter += 5
            s = s[:-1]
        if len(s) >=2:
            if s[-1] == 'X' and s[-2] == 'I':
                print('9+')
                counter += 9
                s = s[:-1]
                s = s[:-1]
        if s[-1:] == 'X':
            print('10+')
            counter += 10
            s = s[:-1]
        if len(s) >=2:
            if s[-1] == 'L' and s[-2] == 'X':
                print('40+')
                counter += 40
                s = s[:-1]
                s = s[:-1]
        if s[-1:] == 'L':
            print('50+')
            counter += 50
            s = s[:-1]
        if len(s) >=2:
            if s[-1] == 'C' and s[-2] == 'X':
                print('90+')
                counter += 90
                s = s[:-1]
                s = s[:-1]
        if s[-1:] == 'C':
            print('100+')
            counter += 100
            s = s[:-1]
        if len(s) >=2:
            if s[-1] == 'D' and s[-2] == 'C':
                print('400+')
                counter += 400
                s = s[:-1]
                s = s[:-1]
        if s[-1:] == 'D':
            print('500+')
            counter += 500
            s = s[:-1]
        if len(s) >=2:
            if s[-1] == 'M' and s[-2] == 'C':
                print('900+')
                counter += 900
                s = s[:-1]
                s = s[:-1]
        if s[-1:] == 'M':
            print('1000+')
            counter += 1000
            s = s[:-1]

    print('======',counter)        
    return counter


romanToInt("MCMXCIV")
