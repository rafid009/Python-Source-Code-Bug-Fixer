import numpy as np 

def function(x):

	y0 = x
	q6 = x
	paths = []
	try:
		if y0 >= 7:
			x = q6/9
			paths.append(1)
		else:
			x = y0+x
			q6 = 1+x
			paths.append(2)
		if y0 > 6:
			q6 = q6/8
			y0 = 6*y0
			paths.append(3)
		else:
			x = y0*4
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		q6 = y0**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))