import numpy as np 

def function(x):

	c9 = 7
	g8 = 2
	paths = []
	try:
		if x < 6:
			g8 = 1-5
			paths.append(1)
		else:
			c9 = g8+5
			g8 = c9-2
			paths.append(2)
		if g8 > 2:
			x = 7/g8
			g8 = 1/9
			paths.append(3)
		else:
			g8 = 8+x
			x = x-7
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))