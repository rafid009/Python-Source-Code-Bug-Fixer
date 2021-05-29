import numpy as np 

def function(x):

	y0 = 4
	q6 = x
	paths = []
	try:
		if y0 > 4:
			q6 = 1*6
			x = q6-6
			y0 = 4/y0
			paths.append(1)
		else:
			q6 = 2/q6
			x = 4+x
			paths.append(2)
		if q6 > 1:
			y0 = y0-y0
			q6 = q6+8
			paths.append(3)
		else:
			q6 = q6/1
			q6 = q6-2
			y0 = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y0 = x**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))