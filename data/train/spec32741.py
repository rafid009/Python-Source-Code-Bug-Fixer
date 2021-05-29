import numpy as np 

def function(x):

	x4 = 4
	e1 = 9
	paths = []
	try:
		if x4 >= 0:
			e1 = 1+5
			x4 = x4/4
			x4 = 8-x4
			paths.append(1)
		else:
			x4 = x-6
			e1 = 1/e1
			paths.append(2)
		if e1 <= 5:
			x = 1-x
			e1 = e1/e1
			e1 = x4-e1
			paths.append(3)
		else:
			x4 = x-x4
			x4 = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))