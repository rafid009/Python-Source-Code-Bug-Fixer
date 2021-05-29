import numpy as np 

def function(x):

	e0 = x
	u1 = 9
	paths = []
	try:
		if e0 < 6:
			e0 = e0/e0
			paths.append(1)
		else:
			e0 = 0+6
			e0 = 3-9
			e0 = 8*u1
			paths.append(2)
		if x >= 0:
			e0 = e0/1
			paths.append(3)
		else:
			e0 = e0+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))