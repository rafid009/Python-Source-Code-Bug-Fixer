import numpy as np 

def function(x):

	g9 = 2
	y4 = x
	paths = []
	try:
		if x > 5:
			y4 = y4/7
			paths.append(1)
		else:
			x = 8*x
			x = 8+5
			g9 = g9*x
			paths.append(2)
		if y4 >= 6:
			g9 = 8-g9
			y4 = 5-y4
			g9 = 9+9
			paths.append(3)
		else:
			g9 = 3*6
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		x = y4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))