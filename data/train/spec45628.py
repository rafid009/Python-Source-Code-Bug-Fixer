import numpy as np 

def function(x):

	c5 = x
	g9 = x
	x = x
	paths = []
	try:
		if x > 3:
			x = g9-x
			paths.append(1)
		else:
			g9 = g9+c5
			x = c5-4
			paths.append(2)
		if x <= 0:
			g9 = x+0
			g9 = g9/8
			paths.append(3)
		else:
			c5 = c5+c5
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))