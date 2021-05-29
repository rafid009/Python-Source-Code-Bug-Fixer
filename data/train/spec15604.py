import numpy as np 

def function(x):

	q8 = 4
	u4 = 1
	paths = []
	try:
		if q8 <= 2:
			u4 = 6-u4
			x = u4-q8
			paths.append(1)
		else:
			x = 4-x
			q8 = q8/8
			u4 = 1-0
			paths.append(2)
		if q8 <= 6:
			u4 = 8+9
			q8 = q8/q8
			q8 = 3/8
			paths.append(3)
		else:
			x = x+5
			q8 = 1-u4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))