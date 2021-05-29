import numpy as np 

def function(x):

	e4 = 8
	k4 = x
	paths = []
	try:
		if k4 >= 3:
			k4 = x-7
			x = x+1
			e4 = e4*k4
			paths.append(1)
		else:
			e4 = 0/2
			paths.append(2)
		if k4 >= 6:
			x = x+1
			paths.append(3)
		else:
			e4 = e4-k4
			e4 = e4*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e4 = x**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))