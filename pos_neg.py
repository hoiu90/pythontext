def pos_neg(a, b,negative):
    if negative:
        return a<0 and b<0
    else:
        return (a>0 and b<0) or (a<0 and b>0)
    
print(pos_neg(1,2,True)) # True
print(pos_neg(-1,2,True)) # True
print(pos_neg(1,-2,True)) # True
print(pos_neg(-1,-2,True)) # True
print(pos_neg(1,2,False)) # True
print(pos_neg(-1,2,False)) # True
print(pos_neg(1,-2,False)) # True
print(pos_neg(-1,-2,False)) # True