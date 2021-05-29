import numpy as np 

def function(x):

	a2 = x
	q8 = 0
	paths = []
	try:
		if q8 <= 1:
			q8 = 9*q8
			paths.append(1)
		else:
			a2 = 8+6
			a2 = 3+a2
			paths.append(2)
		if a2 > 9:
			q8 = q8/9
			paths.append(3)
		else:
			q8 = 9-q8
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