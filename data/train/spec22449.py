import numpy as np 

def function(x):

	x5 = 0
	q8 = x
	paths = []
	try:
		if q8 <= 2:
			x5 = x5*6
			paths.append(1)
		else:
			x5 = 1-4
			paths.append(2)
		if q8 > 4:
			q8 = q8+0
			q8 = 6+6
			paths.append(3)
		else:
			q8 = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))