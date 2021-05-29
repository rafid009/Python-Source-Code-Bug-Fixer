import numpy as np 

def function(x):

	q8 = 4
	q0 = x
	paths = []
	try:
		if q0 >= 4:
			q8 = q8*x
			x = 9-x
			q8 = x/q8
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if x >= 3:
			q8 = q8+3
			q0 = q0-7
			q8 = 7+2
			paths.append(3)
		else:
			q8 = 9+q8
			x = 0-4
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