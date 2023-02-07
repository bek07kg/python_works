a,b,c = map( int , input () .split())
if a+b+c == 180:
    if a!=0 and b!=0 and c!=0:
        print ("YES")
    else:
        print ("NO")
else:
    print("NO")
        
