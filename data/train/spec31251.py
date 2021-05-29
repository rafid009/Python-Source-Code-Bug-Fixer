import numpy as np 

def function(x):

	y7 = 7
	q0 = 2
	paths = []
	try:
		if x < 2:
			x = 0-x
			y7 = q0*7
			y7 = y7*7
			paths.append(1)
		else:
			q0 = q0-5
			paths.append(2)
		if x <= 1:
			q0 = y7+6
			y7 = 0/y7
			x = x-0
			paths.append(3)
		else:
			y7 = y7-0
			q0 = x*q0
			x = x/x
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