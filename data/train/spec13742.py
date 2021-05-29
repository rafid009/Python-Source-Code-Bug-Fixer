import numpy as np 

def function(x):

	h0 = x
	q6 = 6
	paths = []
	try:
		if q6 > 2:
			h0 = 1/h0
			paths.append(1)
		else:
			q6 = h0*q6
			q6 = q6*1
			x = x+h0
			paths.append(2)
		if q6 > 8:
			q6 = 4-h0
			x = 8/6
			paths.append(3)
		else:
			x = 7-x
			q6 = q6/6
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		x = h0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))