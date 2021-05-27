import numpy as np 

def function(x):

	g9 = x
	y4 = x
	paths = []
	try:
		if y4 < 2:
			y4 = 7+3
			g9 = 2+x
			paths.append(1)
		else:
			y4 = y4-y4
			y4 = y4-8
			g9 = 2*g9
			paths.append(2)
		if y4 < 7:
			g9 = 6*y4
			g9 = g9/7
			paths.append(3)
		else:
			g9 = 9/y4
			g9 = g9-6
			y4 = y4-g9
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))