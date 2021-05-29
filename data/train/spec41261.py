import numpy as np 

def function(x):

	u4 = x
	q0 = x
	paths = []
	try:
		if x > 3:
			u4 = 3/x
			u4 = 0+u4
			q0 = q0-4
			paths.append(1)
		else:
			q0 = q0*8
			paths.append(2)
		if q0 < 6:
			x = x-3
			paths.append(3)
		else:
			q0 = x-q0
			q0 = 4*q0
			u4 = u4-u4
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