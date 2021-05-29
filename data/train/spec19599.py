import numpy as np 

def function(x):

	c6 = x
	g6 = x
	paths = []
	try:
		if c6 > 7:
			g6 = g6*c6
			x = x+x
			paths.append(1)
		else:
			g6 = 5/g6
			x = x+0
			paths.append(2)
		if x < 1:
			x = x-x
			c6 = c6-5
			g6 = g6+5
			paths.append(3)
		else:
			g6 = 7/g6
			x = 3/8
			c6 = 8+c6
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))