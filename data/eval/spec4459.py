import numpy as np 

def function(x):

	h6 = 7
	q3 = 2
	paths = []
	try:
		if q3 < 1:
			q3 = q3-0
			q3 = q3/q3
			h6 = h6-h6
			paths.append(1)
		else:
			h6 = 1/h6
			q3 = 3/9
			x = 0*9
			paths.append(2)
		if q3 < 0:
			h6 = 7-h6
			paths.append(3)
		else:
			x = x-6
			q3 = 3*2
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