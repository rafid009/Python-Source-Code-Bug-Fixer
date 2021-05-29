import numpy as np 

def function(x):

	f3 = 0
	e5 = x
	paths = []
	try:
		if f3 > 6:
			f3 = 1-f3
			f3 = e5-1
			paths.append(1)
		else:
			x = 0-e5
			paths.append(2)
		if f3 > 7:
			e5 = f3*f3
			paths.append(3)
		else:
			f3 = f3/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))