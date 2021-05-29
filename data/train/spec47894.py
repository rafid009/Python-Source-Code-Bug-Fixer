import numpy as np 

def function(x):

	x3 = x
	e4 = x
	paths = []
	try:
		if e4 >= 1:
			x = 9/x
			paths.append(1)
		else:
			x3 = x3+5
			paths.append(2)
		if x >= 6:
			x3 = x3+x3
			paths.append(3)
		else:
			x3 = x3-4
			x3 = x3/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))