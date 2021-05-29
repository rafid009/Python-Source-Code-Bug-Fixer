import numpy as np 

def function(x):

	x2 = x
	y0 = 3
	paths = []
	try:
		if x >= 2:
			y0 = y0/x2
			x = x2-x
			paths.append(1)
		else:
			y0 = y0+x
			paths.append(2)
		if y0 >= 6:
			x2 = 6-x2
			paths.append(3)
		else:
			y0 = x2+x
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x2 = y0**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))