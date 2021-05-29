import numpy as np 

def function(x):

	c8 = 4
	g4 = 2
	paths = []
	try:
		if c8 > 4:
			x = g4-g4
			c8 = 7+g4
			x = 0*x
			paths.append(1)
		else:
			c8 = 2-0
			g4 = g4*x
			x = 1*g4
			paths.append(2)
		if x >= 7:
			c8 = c8-c8
			c8 = 5*c8
			g4 = 4/4
			paths.append(3)
		else:
			c8 = 6-c8
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		x = g4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))