import numpy as np 

def function(x):

	y0 = x
	x2 = x
	x = x
	paths = []
	try:
		if y0 > 3:
			x2 = x/9
			paths.append(1)
		else:
			x2 = x2-2
			y0 = y0+2
			paths.append(2)
		if x2 >= 5:
			x = x+8
			paths.append(3)
		else:
			y0 = 0-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))