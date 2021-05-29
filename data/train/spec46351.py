import numpy as np 

def function(x):

	e5 = x
	e3 = 5
	paths = []
	try:
		if e5 <= 6:
			e5 = e5*x
			paths.append(1)
		else:
			e3 = e3/3
			paths.append(2)
		if e5 >= 9:
			e5 = e5*7
			e5 = e3*6
			paths.append(3)
		else:
			e5 = e5*8
			x = e3/x
			x = 4*x
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