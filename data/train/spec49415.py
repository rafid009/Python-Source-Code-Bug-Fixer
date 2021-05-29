import numpy as np 

def function(x):

	e3 = 5
	x4 = 4
	paths = []
	try:
		if x <= 9:
			x4 = x+7
			x = 9-4
			paths.append(1)
		else:
			x = 5+x4
			e3 = 9-9
			x4 = 2+x4
			paths.append(2)
		if x4 > 9:
			x = 5*e3
			x4 = x4-7
			e3 = e3-e3
			paths.append(3)
		else:
			x = e3+4
			x4 = x4*x4
			x = x-x4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))