import numpy as np 

def function(x):

	e0 = 2
	e6 = 0
	paths = []
	try:
		if e0 <= 5:
			e0 = e6*e0
			e6 = e6*8
			e6 = e6+e6
			paths.append(1)
		else:
			e6 = 5*e6
			x = x+4
			e0 = e0+5
			paths.append(2)
		if e0 < 2:
			e0 = 4*5
			paths.append(3)
		else:
			e0 = 7/e0
			e6 = 4+e6
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