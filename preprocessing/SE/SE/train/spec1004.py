import numpy as np 

def function(x):

	y5 = x
	e4 = x
	paths = []
	try:
		if y5 < 7:
			y5 = y5/y5
			x = x-2
			e4 = 0-x
			paths.append(1)
		else:
			e4 = 3+e4
			x = 3/x
			paths.append(2)
		if e4 <= 3:
			e4 = e4/e4
			e4 = e4+0
			paths.append(3)
		else:
			y5 = 1-7
			y5 = 9-y5
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