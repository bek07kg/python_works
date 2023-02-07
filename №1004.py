from math import sqrt

x , y = map ( int , input () .split() )
x , y = abs(x), abs(y)
if x == 0 and y != 0:
	print (round(sqrt((y**2)*)))
	