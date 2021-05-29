import numpy as np 

def function(x):

	e0 = x
	a1 = 3
	paths = []
	try:
		if x <= 9:
			e0 = e0-7
			a1 = 9+7
			paths.append(1)
		else:
			a1 = a1/1
			e0 = 6/a1
			paths.append(2)
		if x >= 7:
			e0 = 2+e0
			paths.append(3)
		else:
			e0 = e0+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a1 = x**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))