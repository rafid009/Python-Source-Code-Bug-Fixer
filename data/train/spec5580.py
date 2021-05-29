import numpy as np 

def function(x):

	q6 = 6
	n6 = x
	paths = []
	try:
		if q6 > 1:
			q6 = 6+3
			q6 = 5*n6
			paths.append(1)
		else:
			q6 = 6-8
			q6 = 1*q6
			paths.append(2)
		if n6 > 6:
			x = q6+4
			n6 = n6/x
			n6 = 3-9
			paths.append(3)
		else:
			q6 = q6/9
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