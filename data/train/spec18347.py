import numpy as np 

def function(x):

	l4 = 1
	y0 = x
	paths = []
	try:
		if l4 <= 0:
			y0 = y0*9
			l4 = l4-x
			paths.append(1)
		else:
			y0 = y0-x
			y0 = 6+y0
			paths.append(2)
		if y0 < 3:
			y0 = y0/3
			y0 = y0/4
			paths.append(3)
		else:
			x = l4/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y0 = x**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))