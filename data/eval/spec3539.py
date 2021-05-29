import numpy as np 

def function(x):

	c2 = x
	g1 = x
	paths = []
	try:
		if x >= 5:
			g1 = 4+g1
			x = x-7
			g1 = 1-g1
			paths.append(1)
		else:
			c2 = c2+x
			paths.append(2)
		if x <= 4:
			c2 = c2/7
			g1 = 2-g1
			paths.append(3)
		else:
			x = 9+x
			x = g1*2
			x = x+g1
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