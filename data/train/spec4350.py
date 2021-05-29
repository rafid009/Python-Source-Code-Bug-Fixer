import numpy as np 

def function(x):

	e3 = x
	e0 = 5
	paths = []
	try:
		if x <= 7:
			x = 2-x
			e3 = e3+x
			e3 = 5+e3
			paths.append(1)
		else:
			x = 9-6
			x = 5*x
			e0 = e0*x
			paths.append(2)
		if e3 <= 8:
			e0 = e0-7
			e0 = 1*8
			e3 = 7+e3
			paths.append(3)
		else:
			x = x*x
			x = 1-e0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))