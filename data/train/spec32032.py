import numpy as np 

def function(x):

	v3 = 5
	g3 = 7
	paths = []
	try:
		if g3 >= 8:
			g3 = 2*g3
			g3 = g3-x
			x = x*8
			paths.append(1)
		else:
			g3 = g3*g3
			x = 3-5
			v3 = 2*4
			paths.append(2)
		if g3 > 3:
			x = x-g3
			paths.append(3)
		else:
			v3 = 3+v3
			v3 = v3-g3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g3 = x**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))