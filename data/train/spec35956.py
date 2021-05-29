import numpy as np 

def function(x):

	c5 = 3
	g9 = x
	paths = []
	try:
		if c5 <= 7:
			c5 = 1-x
			g9 = g9+7
			paths.append(1)
		else:
			x = c5/x
			c5 = c5*g9
			paths.append(2)
		if c5 <= 8:
			x = g9-6
			paths.append(3)
		else:
			x = x*x
			paths.append(4)
		paths.append(5)
		assert c5 >= 0
		g9 = c5**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))