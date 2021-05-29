import numpy as np 

def function(x):

	q7 = 4
	e8 = 6
	paths = []
	try:
		if x <= 5:
			e8 = q7/e8
			e8 = 2-4
			q7 = 4/q7
			paths.append(1)
		else:
			q7 = 0-e8
			q7 = 3*q7
			x = 3*x
			paths.append(2)
		if x >= 6:
			e8 = 4/7
			x = 2-x
			x = x/2
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e8 = x**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))