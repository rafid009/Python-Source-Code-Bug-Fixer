import numpy as np 

def function(x):

	a0 = 0
	e9 = x
	paths = []
	try:
		if x <= 1:
			e9 = e9*5
			paths.append(1)
		else:
			a0 = 5-5
			paths.append(2)
		if x < 8:
			e9 = e9/5
			paths.append(3)
		else:
			a0 = a0*9
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