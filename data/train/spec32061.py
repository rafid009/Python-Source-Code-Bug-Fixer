import numpy as np 

def function(x):

	e9 = 6
	e0 = 7
	paths = []
	try:
		if x <= 1:
			e0 = 0-e0
			e9 = e9+e9
			paths.append(1)
		else:
			e9 = 7-2
			paths.append(2)
		if e9 > 7:
			x = x-1
			e0 = 6/3
			e0 = 0+7
			paths.append(3)
		else:
			e9 = 4*e0
			x = 6+1
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