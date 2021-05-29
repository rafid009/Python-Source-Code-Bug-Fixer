import numpy as np 

def function(x):

	c6 = 9
	g5 = x
	paths = []
	try:
		if g5 <= 4:
			c6 = c6+0
			g5 = g5-3
			paths.append(1)
		else:
			g5 = g5-7
			paths.append(2)
		if c6 <= 8:
			x = 2/x
			g5 = 5/g5
			g5 = g5/g5
			paths.append(3)
		else:
			c6 = 2-c6
			c6 = c6+4
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