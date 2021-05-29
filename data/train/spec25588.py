import numpy as np 

def function(x):

	a8 = x
	e1 = x
	paths = []
	try:
		if x >= 8:
			e1 = 6*e1
			paths.append(1)
		else:
			x = e1-x
			paths.append(2)
		if a8 >= 2:
			x = x-1
			paths.append(3)
		else:
			a8 = 0-e1
			x = 2-8
			e1 = 2-e1
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))