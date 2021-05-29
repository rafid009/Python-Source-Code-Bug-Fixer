import numpy as np 

def function(x):

	e5 = x
	u4 = 2
	paths = []
	try:
		if x < 9:
			u4 = 5+4
			paths.append(1)
		else:
			e5 = 5-3
			paths.append(2)
		if x >= 2:
			x = u4-5
			paths.append(3)
		else:
			e5 = e5+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))