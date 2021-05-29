import numpy as np 

def function(x):

	e9 = x
	e1 = x
	paths = []
	try:
		if x > 9:
			e1 = e1/e9
			paths.append(1)
		else:
			e1 = 2*e1
			paths.append(2)
		if e9 > 6:
			e9 = 9*e9
			e9 = x-0
			paths.append(3)
		else:
			e1 = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))