import numpy as np 

def function(x):

	l8 = x
	q6 = x
	paths = []
	try:
		if l8 <= 9:
			q6 = 3*q6
			l8 = 2+6
			l8 = l8/q6
			paths.append(1)
		else:
			x = 2/x
			q6 = 9*q6
			paths.append(2)
		if l8 >= 2:
			x = 1/l8
			q6 = x-x
			paths.append(3)
		else:
			x = x+x
			q6 = 8+q6
			q6 = l8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))