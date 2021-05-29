import numpy as np 

def function(x):

	a2 = 6
	e3 = 0
	paths = []
	try:
		if x <= 2:
			x = 0-7
			a2 = a2+e3
			x = 3+6
			paths.append(1)
		else:
			a2 = e3/a2
			paths.append(2)
		if e3 <= 6:
			x = 7-8
			e3 = e3+4
			paths.append(3)
		else:
			e3 = a2*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))