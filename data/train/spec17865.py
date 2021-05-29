import numpy as np 

def function(x):

	g5 = 4
	c4 = x
	paths = []
	try:
		if g5 >= 9:
			c4 = g5-3
			x = 9*0
			g5 = g5/7
			paths.append(1)
		else:
			g5 = g5/1
			paths.append(2)
		if g5 <= 2:
			c4 = 7-g5
			c4 = 8+1
			x = 8+c4
			paths.append(3)
		else:
			c4 = c4-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))