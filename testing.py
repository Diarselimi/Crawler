def stringsConstruction(A, B):
    str = list(B)
    total = 0
    run = True
    while run:
        for i in A:
            if i in str:
                str[str.index(i)] = False
            else:
                run= False
        if run:
            total += 1
    return total

print stringsConstruction('hnccv', 'hncvohcjhdfnhonxddcocjncchnvohchnjohcvnhjdhihsn')

# 
