import numpy as np 

def function(x):

	y0 = 3
	q3 = 3
	paths = []
	try:
		if x >= 0:
			q3 = q3+x
			paths.append(1)
		else:
			y0 = y0+y0
			paths.append(2)
		if q3 > 1:
			q3 = 3+6
			y0 = y0-7
			paths.append(3)
		else:
			q3 = y0*q3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q3 = x**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))