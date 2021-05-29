import numpy as np 

def function(x):

	x2 = 7
	e4 = x
	paths = []
	try:
		if e4 >= 4:
			x2 = x*x
			e4 = x-3
			paths.append(1)
		else:
			x = e4/3
			paths.append(2)
		if x <= 4:
			e4 = e4+2
			e4 = x2-e4
			paths.append(3)
		else:
			e4 = 9/2
			x2 = 0/x2
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