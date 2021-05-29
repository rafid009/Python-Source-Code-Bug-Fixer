import numpy as np 

def function(x):

	n4 = 0
	e4 = 6
	paths = []
	try:
		if x <= 1:
			x = 1-x
			paths.append(1)
		else:
			x = x+e4
			n4 = n4-x
			paths.append(2)
		if x >= 3:
			e4 = e4-9
			e4 = x-e4
			x = 7-x
			paths.append(3)
		else:
			x = n4+x
			e4 = 4-x
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