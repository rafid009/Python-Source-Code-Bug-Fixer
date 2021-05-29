import numpy as np 

def function(x):

	e8 = x
	f6 = x
	paths = []
	try:
		if f6 < 3:
			x = x-e8
			e8 = 5*x
			paths.append(1)
		else:
			e8 = 8*e8
			x = 9-x
			paths.append(2)
		if x <= 9:
			e8 = x*f6
			paths.append(3)
		else:
			f6 = x-f6
			e8 = 5-4
			e8 = e8/1
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