a = int ( input () )
l = []
for i in range (a):
    b = int ( input ())
    l.append(b)
l = sorted (l)
for j in range (a):
    print ( l [j])
