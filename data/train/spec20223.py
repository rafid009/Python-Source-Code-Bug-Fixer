import numpy as np 

def function(x):

	u4 = x
	q8 = x
	paths = []
	try:
		if q8 > 1:
			q8 = q8*3
			paths.append(1)
		else:
			q8 = 4*4
			paths.append(2)
		if q8 < 7:
			x = u4-x
			u4 = x-u4
			paths.append(3)
		else:
			x = x-3
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