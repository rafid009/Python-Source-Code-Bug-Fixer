import numpy as np 

def function(x):

	g5 = 0
	c4 = 7
	paths = []
	try:
		if x > 0:
			x = x/c4
			paths.append(1)
		else:
			g5 = g5*4
			x = x+7
			paths.append(2)
		if c4 >= 9:
			g5 = x*x
			c4 = c4-1
			x = x+c4
			paths.append(3)
		else:
			c4 = c4+x
			x = x/2
			paths.append(4)
		paths.append(5)
		assert c4 >= 0
		g5 = c4**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))