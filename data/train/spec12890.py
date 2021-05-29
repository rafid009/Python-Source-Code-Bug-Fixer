import numpy as np 

def function(x):

	e2 = 4
	x6 = x
	paths = []
	try:
		if x >= 2:
			e2 = x6/3
			paths.append(1)
		else:
			e2 = x6*3
			paths.append(2)
		if x < 8:
			e2 = 4+6
			e2 = e2/x6
			e2 = e2+7
			paths.append(3)
		else:
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		e2 = x6**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))