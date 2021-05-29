import numpy as np 

def function(x):

	a1 = x
	e2 = x
	paths = []
	try:
		if e2 <= 5:
			a1 = 0/a1
			paths.append(1)
		else:
			e2 = 8/e2
			a1 = 9*e2
			paths.append(2)
		if e2 > 2:
			a1 = a1-a1
			x = 3-x
			a1 = a1-0
			paths.append(3)
		else:
			e2 = x/1
			x = 6*x
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