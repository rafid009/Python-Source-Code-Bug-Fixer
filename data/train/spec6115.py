import numpy as np 

def function(x):

	g5 = x
	c1 = x
	paths = []
	try:
		if x < 5:
			g5 = g5*g5
			c1 = g5*c1
			paths.append(1)
		else:
			g5 = g5/2
			g5 = g5/7
			g5 = g5-5
			paths.append(2)
		if c1 < 7:
			x = x*g5
			paths.append(3)
		else:
			x = 8/x
			c1 = 0+c1
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g5 = g5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))