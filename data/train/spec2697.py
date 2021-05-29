import numpy as np 

def function(x):

	q9 = 4
	y0 = 5
	paths = []
	try:
		if x <= 6:
			q9 = q9/2
			q9 = 4-q9
			paths.append(1)
		else:
			y0 = 6/y0
			paths.append(2)
		if q9 >= 6:
			y0 = y0/y0
			y0 = y0-8
			paths.append(3)
		else:
			x = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q9 = x**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))