import numpy as np 

def function(x):

	e8 = 6
	e6 = x
	paths = []
	try:
		if x <= 3:
			e8 = 7*e8
			e8 = e6/4
			paths.append(1)
		else:
			e6 = e6*e8
			paths.append(2)
		if e6 >= 0:
			x = 2-8
			e6 = 8-e6
			e6 = e6+e8
			paths.append(3)
		else:
			e8 = 7-e8
			e8 = e8-2
			e6 = e6/e6
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