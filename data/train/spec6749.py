import numpy as np 

def function(x):

	c3 = x
	g8 = 8
	paths = []
	try:
		if x <= 3:
			g8 = 3/g8
			c3 = 5-9
			paths.append(1)
		else:
			x = x-c3
			x = 5+3
			paths.append(2)
		if g8 >= 8:
			g8 = 2-6
			x = 0*x
			paths.append(3)
		else:
			x = x+5
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		g8 = g8**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))