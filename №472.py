a = str ( input () )
l = []
for char in a:
    l.append (char)
f = l.count ("4")
f1 = l.count ("7")

if f + f1 == len(l):
    print ("YES")

else:
    print ("NO")
