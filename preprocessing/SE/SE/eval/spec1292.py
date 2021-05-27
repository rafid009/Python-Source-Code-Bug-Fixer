import numpy as np 

def function(x):

	b3 = x
	e7 = 7
	paths = []
	try:
		if x >= 0:
			x = 3*x
			paths.append(1)
		else:
			x = x+3
			x = x*3
			paths.append(2)
		if x <= 6:
			e7 = e7/2
			b3 = b3*5
			paths.append(3)
		else:
			e7 = b3-b3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e7 = x**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))