import numpy as np 

def function(x):

	c7 = x
	g1 = 2
	paths = []
	try:
		if g1 > 2:
			x = 3*x
			x = g1/7
			c7 = 7*3
			paths.append(1)
		else:
			g1 = g1+0
			c7 = g1*c7
			paths.append(2)
		if g1 >= 7:
			g1 = 4*g1
			c7 = 5/c7
			g1 = 4-g1
			paths.append(3)
		else:
			c7 = 8*c7
			x = c7+x
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		g1 = c7**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))