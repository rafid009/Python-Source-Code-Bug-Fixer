import numpy as np 

def function(x):

	e5 = 1
	x0 = x
	paths = []
	try:
		if x0 >= 5:
			x = x-8
			x = 9+5
			x = 1/x
			paths.append(1)
		else:
			x0 = x0+x
			x = x+9
			paths.append(2)
		if x <= 7:
			x0 = x0*7
			x = x0-4
			x = 0-x
			paths.append(3)
		else:
			x = 5-x
			e5 = e5*7
			e5 = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e5 = x**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))