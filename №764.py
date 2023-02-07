a = str ( input () )
k = []
for i in range (len(a)):
    k.append(a[i])
    k[i] = int (k[i])
print (sum(k))    
