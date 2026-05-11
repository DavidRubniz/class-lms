x = 'asdfghjdsmnb'
if len(x) < 10:
    print('len of x must be at list 10 letters')
else:
    if x[7] == 'd' and x[8] == 'e' or x[8] == 'e' and x[9] == 'f':
        print('Version A')
    else:
        print('Version B')
