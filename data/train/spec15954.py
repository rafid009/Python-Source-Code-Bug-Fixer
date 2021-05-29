import numpy as np 

def function(x):

	l8 = 6
	e7 = 3
	paths = []
	try:
		if l8 < 8:
			l8 = l8+e7
			e7 = e7/4
			e7 = 0-e7
			paths.append(1)
		else:
			x = 3-l8
			l8 = l8-8
			paths.append(2)
		if l8 >= 1:
			l8 = l8*x
			x = x-6
			paths.append(3)
		else:
			x = e7/e7
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l8 = x**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))