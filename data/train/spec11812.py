import numpy as np 

def function(x):

	c1 = 5
	g3 = 7
	x = x
	paths = []
	try:
		if c1 < 6:
			x = 4+g3
			x = g3-x
			g3 = g3-4
			paths.append(1)
		else:
			x = x/9
			g3 = g3/1
			g3 = g3*6
			paths.append(2)
		if g3 <= 1:
			c1 = 7-9
			g3 = 0-3
			paths.append(3)
		else:
			g3 = g3+g3
			g3 = 5+x
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