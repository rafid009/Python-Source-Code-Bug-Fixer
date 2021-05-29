import numpy as np 

def function(x):

	b7 = x
	e5 = 6
	paths = []
	try:
		if e5 >= 3:
			e5 = e5+4
			paths.append(1)
		else:
			e5 = 5/e5
			paths.append(2)
		if e5 < 6:
			e5 = 8-e5
			paths.append(3)
		else:
			e5 = 3*e5
			e5 = e5*1
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		x = b7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))