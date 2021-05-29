import numpy as np 

def function(x):

	e3 = 9
	e2 = x
	paths = []
	try:
		if e3 >= 6:
			e3 = 2+7
			e3 = x+e3
			paths.append(1)
		else:
			x = x-e2
			e2 = e2/8
			e2 = 1+e2
			paths.append(2)
		if x >= 7:
			x = e2*3
			e3 = 7-e3
			paths.append(3)
		else:
			x = e3/x
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