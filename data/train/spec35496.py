import numpy as np 

def function(x):

	n9 = x
	q6 = 9
	paths = []
	try:
		if n9 < 4:
			q6 = 6*q6
			q6 = n9-x
			q6 = 5+q6
			paths.append(1)
		else:
			q6 = 2-q6
			paths.append(2)
		if n9 <= 9:
			q6 = 6/q6
			q6 = q6*x
			x = n9+q6
			paths.append(3)
		else:
			n9 = 9+n9
			x = 2*x
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n9 = x**0.5
		return n9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))