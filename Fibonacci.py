def fibonacci(num):
    if num<0:
        return "Invalid"
    elif num==0:
        return 0
    elif num==1:
        return 1
    else:
        a=0
        b=1
        for i in range(num-2):
            c=a+b
            a,b=b,c
    return c

print(fibonacci(9))