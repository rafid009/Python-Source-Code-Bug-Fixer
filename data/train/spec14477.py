import numpy as np 

def function(x):

	g1 = 5
	r3 = 9
	paths = []
	try:
		if x >= 7:
			g1 = g1*g1
			r3 = 3*r3
			x = r3-x
			paths.append(1)
		else:
			r3 = 5*g1
			x = 2+x
			paths.append(2)
		if x > 1:
			x = 3/1
			g1 = g1/g1
			x = 9/x
			paths.append(3)
		else:
			r3 = 6/r3
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