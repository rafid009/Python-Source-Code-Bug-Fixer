import numpy as np 

def function(x):

	g3 = 4
	c4 = 9
	paths = []
	try:
		if g3 > 9:
			g3 = g3-5
			paths.append(1)
		else:
			g3 = 9/7
			x = x+g3
			paths.append(2)
		if g3 < 3:
			c4 = 0/c4
			c4 = x+c4
			x = 1*x
			paths.append(3)
		else:
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g3 = x**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))