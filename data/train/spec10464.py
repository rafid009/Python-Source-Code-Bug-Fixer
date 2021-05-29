import numpy as np 

def function(x):

	c9 = 7
	g4 = 5
	paths = []
	try:
		if x > 7:
			c9 = c9/8
			c9 = c9+3
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if g4 > 5:
			x = x/4
			g4 = 0/2
			paths.append(3)
		else:
			x = 8/x
			c9 = 6*1
			g4 = g4*7
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