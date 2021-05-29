import numpy as np 

def function(x):

	q0 = 4
	e9 = x
	paths = []
	try:
		if q0 <= 4:
			x = x+x
			paths.append(1)
		else:
			x = 8-x
			paths.append(2)
		if x <= 5:
			e9 = x-e9
			x = x-7
			e9 = 3*e9
			paths.append(3)
		else:
			x = 7/x
			x = 6/e9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q0 = x**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))