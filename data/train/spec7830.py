import numpy as np 

def function(x):

	y4 = x
	g7 = 3
	paths = []
	try:
		if g7 >= 6:
			x = x*g7
			x = 3/x
			y4 = 6-y4
			paths.append(1)
		else:
			y4 = y4/7
			y4 = y4*y4
			paths.append(2)
		if g7 >= 5:
			x = x-x
			y4 = 5*8
			paths.append(3)
		else:
			y4 = y4/g7
			g7 = 7/g7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))