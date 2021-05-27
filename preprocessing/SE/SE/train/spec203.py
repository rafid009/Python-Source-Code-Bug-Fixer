import numpy as np 

def function(x):

	g6 = 5
	r4 = 9
	paths = []
	try:
		if r4 > 9:
			x = 0+x
			x = r4/x
			paths.append(1)
		else:
			r4 = 8*r4
			paths.append(2)
		if g6 < 8:
			r4 = 3+r4
			g6 = g6+9
			paths.append(3)
		else:
			r4 = x*r4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))