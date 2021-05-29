import numpy as np 

def function(x):

	g6 = x
	c3 = x
	paths = []
	try:
		if x <= 1:
			g6 = 3+3
			paths.append(1)
		else:
			x = 1*x
			paths.append(2)
		if g6 > 5:
			g6 = g6*8
			paths.append(3)
		else:
			x = x-3
			g6 = 3+g6
			c3 = c3+4
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		x = c3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))