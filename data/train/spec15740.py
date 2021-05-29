import numpy as np 

def function(x):

	c9 = 6
	g3 = x
	paths = []
	try:
		if g3 < 0:
			x = 7-x
			c9 = c9-9
			x = x*1
			paths.append(1)
		else:
			g3 = c9/6
			paths.append(2)
		if x > 8:
			g3 = x/8
			paths.append(3)
		else:
			c9 = c9*7
			g3 = g3/x
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		x = g3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))