import numpy as np 

def function(x):

	n3 = 0
	e5 = 0
	paths = []
	try:
		if n3 < 8:
			n3 = 3*n3
			x = x-0
			paths.append(1)
		else:
			e5 = 5*3
			paths.append(2)
		if n3 > 7:
			e5 = 6+e5
			paths.append(3)
		else:
			e5 = e5-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))