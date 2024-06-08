from multipledispatch import dispatch 
@dispatch(int,int)
def sum(a,b):
    return a+b

def multp(a,b):
    print(a*b)

@dispatch(int,int,int)
def sum(a,b,c):
    return a+b+c

print(sum(1,2))
print(sum(1,2,4))