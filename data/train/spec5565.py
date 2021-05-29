import numpy as np 

def function(x):

	g0 = x
	r3 = 9
	paths = []
	try:
		if x >= 6:
			x = 0-1
			paths.append(1)
		else:
			x = g0+6
			paths.append(2)
		if r3 < 8:
			g0 = 9/x
			x = x+2
			paths.append(3)
		else:
			g0 = x/4
			r3 = r3/3
			r3 = r3+r3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g0 = x**0.5
		return g0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))