import numpy as np 

def function(x):

	c7 = x
	g1 = 1
	paths = []
	try:
		if g1 <= 0:
			x = x-5
			x = c7/x
			g1 = g1*6
			paths.append(1)
		else:
			c7 = x+3
			paths.append(2)
		if x < 6:
			g1 = 7-c7
			paths.append(3)
		else:
			x = 6/c7
			paths.append(4)
		paths.append(5)
		assert c7 >= 0
		x = c7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))