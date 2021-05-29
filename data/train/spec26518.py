import numpy as np 

def function(x):

	e0 = 9
	u1 = 7
	x = 5
	paths = []
	try:
		if e0 >= 1:
			u1 = u1-0
			paths.append(1)
		else:
			e0 = e0+e0
			paths.append(2)
		if e0 <= 2:
			e0 = e0-5
			paths.append(3)
		else:
			x = x-9
			u1 = 1-9
			u1 = 7-e0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e0 = x**0.5
		return e0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))