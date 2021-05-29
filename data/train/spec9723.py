import numpy as np 

def function(x):

	e8 = x
	paths = []
	try:
		if e8 <= 8:
			e8 = e8+4
			paths.append(1)
		else:
			x = 1/7
			paths.append(2)
		if e8 <= 1:
			e8 = e8/x
			e8 = e8+2
			paths.append(3)
		else:
			e8 = 4/6
			e8 = 6/e8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))