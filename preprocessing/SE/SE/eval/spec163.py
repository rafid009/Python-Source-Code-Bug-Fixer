import numpy as np 

def function(x):

	q4 = x
	y0 = x
	x = 4
	paths = []
	try:
		if x > 7:
			y0 = 5*7
			x = x-7
			q4 = 3+q4
			paths.append(1)
		else:
			q4 = 8*q4
			x = 5-x
			paths.append(2)
		if x < 5:
			q4 = y0/y0
			paths.append(3)
		else:
			y0 = 2*y0
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		q4 = y0**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))