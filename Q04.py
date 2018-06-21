def troca(s, velho, novo):
    print(type(novo))
    print(type(velho))
    pos = ''
    b = 0
    aux = ''
    x = ''
    z = len(velho)
    a = z
    y = len(novo)
    c = y
    #print(z)
    #print(y)
    for c in s:
        print(c)
        if c == velho[((z-a)<len(velho))]:
            #print(novo[(y-c)])
            aux += novo[((y-c)<len(novo))]
            z+=1
            #if z-a >= len(velho):
            y+=1
            if len(aux) == z:
                x+=aux
            else:
                pos+=aux
        else:
            x += aux+c
            aux = ''
            pos = ''
            z = len(velho)
            y = len(novo)
    print(x)
