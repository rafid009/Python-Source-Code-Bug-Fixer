import numpy as np 

def function(x):

	g6 = 9
	c3 = 0
	paths = []
	try:
		if x >= 8:
			g6 = 5-g6
			paths.append(1)
		else:
			c3 = c3+x
			x = g6+5
			c3 = c3-0
			paths.append(2)
		if g6 < 9:
			c3 = 6/1
			paths.append(3)
		else:
			x = x+g6
			paths.append(4)
		paths.append(5)
		assert g6 >= 0
		x = g6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))