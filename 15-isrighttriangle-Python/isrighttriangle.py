# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.

def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
	a = distance(x1,y1,x2,y2)
	b = distance(x2,y2,x3,y3)
	c = distance(x1,y1,x3,y3)
	h = max(a,b,c)
	s = min(a,b,c)
	o = a+b+c-h-s
	h = h**2
	s = s**2
	o = o**2
	if almostEqual(h,s+o):
		return True
	return False

def distance(x1, y1, x2, y2):
	# your code goes here
	X = (x2 - x1)**2
	Y = (y2 - y1)**2
	d = (X+Y)**(1/2)
	return d

def almostEqual(x, y):
	return abs(x - y) < 10**-9