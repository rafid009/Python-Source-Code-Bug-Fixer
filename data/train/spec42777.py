import numpy as np 

def function(x):

	q8 = x
	l8 = 9
	paths = []
	try:
		if l8 < 7:
			q8 = q8*7
			paths.append(1)
		else:
			l8 = q8-q8
			l8 = l8/q8
			paths.append(2)
		if x >= 0:
			q8 = 4-7
			paths.append(3)
		else:
			q8 = 4+q8
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