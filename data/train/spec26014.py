import numpy as np 

def function(x):

	e6 = 8
	e5 = x
	paths = []
	try:
		if e6 < 6:
			e6 = 5+e6
			paths.append(1)
		else:
			e5 = e5/2
			e5 = e5-1
			paths.append(2)
		if e5 > 1:
			e5 = 7-6
			paths.append(3)
		else:
			x = 9*x
			e6 = e6/8
			x = x+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))