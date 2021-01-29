error = 0
def add(a,b):
    c = float()
    c = create(a[0],a[1])
    d = float()
    d = create(b[0],b[1])
    return c+d
    
def mul(a,b):
    c = float()
    c = create(a[0],a[1])
    d = float()
    d = create(b[0],b[1])
    return c*d
    
def sub(a,b):
    c = float()
    c = create(a[0],a[1])
    d = float()
    d = create(b[0],b[1])
    return c-d
    
def div(a,b):
    c = float()
    c = create(a[0],a[1])
    d = float()
    d = create(b[0],b[1])
    return c/d
    
def eq(a,b):
    c = float()
    c = create(a[0],a[1])
    d = float()
    d = create(b[0],b[1])
    if(c==d):
        return true
    else:
        return false
def lt(a,b):
    c = float()
    c = create(a[0],a[1])
    d = float()
    d = create(b[0],b[1])
    if(c<d):
        return true
    else:
        return false
        
def reduce(a,b):
    while(1>0):
        if(a<b):
            b=b-a
        elif(a>b):
            a=a-b
        elif(a==b):
            return(a)
        elif(a[0]<=0 or a[1]<=0):
            return 1
def inp(a,b):
    c = float(input())
    prt(c)
    
def error(a,b):
    pritn((None,None))
              
def prt(a):
    print(a)
    
def create(a,b):
    return a/b
