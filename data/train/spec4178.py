import numpy as np 

def function(x):

	g9 = x
	c7 = x
	paths = []
	try:
		if x <= 9:
			g9 = g9*g9
			g9 = c7/5
			x = x-g9
			paths.append(1)
		else:
			g9 = g9+1
			paths.append(2)
		if c7 < 5:
			g9 = x*4
			c7 = g9-0
			c7 = c7*6
			paths.append(3)
		else:
			g9 = g9*g9
			g9 = g9*x
			g9 = c7+g9
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		g9 = g9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))