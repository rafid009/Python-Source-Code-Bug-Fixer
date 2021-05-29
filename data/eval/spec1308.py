import numpy as np 

def function(x):

	e6 = 3
	x5 = x
	paths = []
	try:
		if x5 <= 9:
			e6 = x+x
			e6 = e6-e6
			paths.append(1)
		else:
			x = 9*x
			x5 = x5+3
			paths.append(2)
		if x >= 2:
			e6 = e6+4
			paths.append(3)
		else:
			x = x-x5
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		e6 = x5**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))