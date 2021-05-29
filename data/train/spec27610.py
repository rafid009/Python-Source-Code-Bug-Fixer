import numpy as np 

def function(x):

	q3 = 6
	y0 = x
	paths = []
	try:
		if x < 0:
			q3 = 8/q3
			paths.append(1)
		else:
			y0 = 5*8
			paths.append(2)
		if x >= 5:
			y0 = 9*q3
			paths.append(3)
		else:
			q3 = q3/y0
			y0 = y0+3
			y0 = y0+2
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		x = q3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))