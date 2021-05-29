import numpy as np 

def function(x):

	e9 = 3
	e6 = 7
	paths = []
	try:
		if x > 1:
			x = 8+4
			e9 = e9-0
			e6 = 8/e6
			paths.append(1)
		else:
			e6 = 8/e6
			e6 = 2/9
			paths.append(2)
		if e6 <= 2:
			e9 = e9-8
			paths.append(3)
		else:
			e6 = e6*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))