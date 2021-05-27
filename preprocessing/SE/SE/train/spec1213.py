import numpy as np 

def function(x):

	v3 = x
	g0 = 2
	paths = []
	try:
		if g0 <= 7:
			v3 = g0-9
			x = 4+x
			g0 = g0-1
			paths.append(1)
		else:
			x = v3-x
			x = x/g0
			paths.append(2)
		if g0 < 9:
			v3 = v3/v3
			paths.append(3)
		else:
			g0 = g0*8
			x = 8/v3
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