import numpy as np 

def function(x):

	q8 = x
	e9 = x
	paths = []
	try:
		if x > 7:
			q8 = q8-7
			x = e9-x
			e9 = e9-4
			paths.append(1)
		else:
			q8 = e9+q8
			e9 = 1/q8
			q8 = 9/1
			paths.append(2)
		if x < 4:
			e9 = e9+5
			x = x-5
			q8 = q8/x
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e9 = x**0.5
		return e9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))