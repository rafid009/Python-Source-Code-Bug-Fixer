import numpy as np 

def function(x):

	c6 = 1
	g1 = 7
	paths = []
	try:
		if g1 > 8:
			g1 = g1*5
			paths.append(1)
		else:
			x = x+3
			c6 = c6-g1
			paths.append(2)
		if x >= 6:
			g1 = 8/g1
			x = x-8
			paths.append(3)
		else:
			c6 = c6-c6
			g1 = 8/9
			paths.append(4)
		paths.append(5)
		assert c6 >= 0
		g1 = c6**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))