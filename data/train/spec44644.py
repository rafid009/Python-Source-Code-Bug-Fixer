import numpy as np 

def function(x):

	k2 = x
	e2 = x
	paths = []
	try:
		if e2 <= 6:
			e2 = e2-x
			paths.append(1)
		else:
			e2 = 7+6
			e2 = e2-0
			paths.append(2)
		if k2 < 2:
			x = 8/x
			e2 = k2*3
			e2 = x+7
			paths.append(3)
		else:
			e2 = e2-9
			e2 = x/6
			x = 3-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e2 = x**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))