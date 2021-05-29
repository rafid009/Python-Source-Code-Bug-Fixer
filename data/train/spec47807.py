import numpy as np 

def function(x):

	q0 = x
	y6 = 5
	paths = []
	try:
		if q0 >= 0:
			x = 9+x
			y6 = y6/y6
			paths.append(1)
		else:
			y6 = y6/8
			q0 = 4*q0
			x = q0-1
			paths.append(2)
		if y6 >= 1:
			x = 9-q0
			paths.append(3)
		else:
			q0 = q0-8
			x = q0-5
			q0 = 8*x
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))