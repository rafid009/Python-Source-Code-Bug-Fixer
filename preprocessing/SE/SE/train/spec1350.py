import numpy as np 

def function(x):

	e7 = 2
	r9 = 4
	paths = []
	try:
		if r9 > 2:
			e7 = 0-e7
			e7 = e7/1
			r9 = r9+7
			paths.append(1)
		else:
			r9 = 4*r9
			x = x-2
			paths.append(2)
		if r9 < 9:
			x = e7*3
			paths.append(3)
		else:
			e7 = e7-8
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