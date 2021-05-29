import numpy as np 

def function(x):

	e3 = x
	e5 = 1
	paths = []
	try:
		if e3 > 4:
			e5 = e3+e5
			paths.append(1)
		else:
			e3 = 7*e5
			paths.append(2)
		if e5 >= 2:
			x = 1/x
			paths.append(3)
		else:
			e5 = e5*2
			e5 = x-9
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