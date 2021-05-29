import numpy as np 

def function(x):

	g6 = 7
	c8 = x
	x = 2
	paths = []
	try:
		if x <= 9:
			c8 = c8+9
			paths.append(1)
		else:
			g6 = g6/4
			g6 = 4-g6
			paths.append(2)
		if g6 < 6:
			x = x*9
			x = 5*x
			paths.append(3)
		else:
			g6 = g6/8
			g6 = g6/c8
			g6 = x/g6
			paths.append(4)
		paths.append(5)
		assert c8 >= 0
		g6 = c8**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))