import numpy as np 

def function(x):

	c7 = x
	g3 = x
	x = x
	paths = []
	try:
		if c7 < 1:
			x = c7-7
			paths.append(1)
		else:
			c7 = c7*x
			paths.append(2)
		if g3 < 3:
			g3 = g3-1
			c7 = c7-3
			paths.append(3)
		else:
			g3 = g3/9
			c7 = c7*8
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		g3 = g3**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))