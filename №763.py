fib1 = fib2 = 1
n = int ( input () ) - 2
if n > 0:
    l = []
    while fib2 < n-1:
        fib1,fib2 = fib2,fib1 + fib2
        l.append(fib2)
    del l[-1]
    k = sum (l) + 2
    print (k)
else:
    print ("ERROR")
