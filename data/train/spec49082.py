import numpy as np 

def function(x):

	a4 = 3
	e2 = 3
	paths = []
	try:
		if e2 > 4:
			a4 = 5+a4
			e2 = 1*a4
			paths.append(1)
		else:
			a4 = a4+x
			paths.append(2)
		if e2 > 6:
			x = 9/a4
			x = x+4
			paths.append(3)
		else:
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))