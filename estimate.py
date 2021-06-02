def wallis(n):
    sum=1
    while(n>0):
        sum*=(4*n*n)/(4*n*n-1)
        n-=1
    return 2*sum

def monte_carlo(n):
    ctr=0
    num=n
    while(n>0):
        x=random.random()
        y=random.random()
        if x*x + y*y < 1:
            ctr+=1
        n-=1
   
    return 4*(ctr/num)
