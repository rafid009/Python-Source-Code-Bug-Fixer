import numpy as np 

def function(x):

	c2 = x
	g8 = 2
	paths = []
	try:
		if c2 <= 0:
			c2 = 8/g8
			g8 = 9-4
			c2 = 2/4
			paths.append(1)
		else:
			g8 = g8/4
			x = x-9
			x = x+2
			paths.append(2)
		if x > 9:
			c2 = c2/8
			x = x/x
			g8 = x/g8
			paths.append(3)
		else:
			c2 = c2-4
			g8 = 0*1
			x = c2+c2
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