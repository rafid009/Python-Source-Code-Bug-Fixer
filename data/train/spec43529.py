import numpy as np 

def function(x):

	g1 = 0
	r4 = x
	paths = []
	try:
		if x >= 2:
			g1 = 3-g1
			paths.append(1)
		else:
			x = x-r4
			r4 = g1-g1
			r4 = 0*r4
			paths.append(2)
		if r4 <= 4:
			r4 = 3+1
			x = x+g1
			x = x/r4
			paths.append(3)
		else:
			x = r4-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g1 = x**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))