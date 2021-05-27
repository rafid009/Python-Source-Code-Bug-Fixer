import numpy as np 

def function(x):

	n1 = x
	q8 = x
	paths = []
	try:
		if q8 <= 1:
			n1 = 1*n1
			q8 = 1*7
			x = 6*n1
			paths.append(1)
		else:
			x = 3/4
			paths.append(2)
		if x < 1:
			q8 = q8+q8
			n1 = 9+n1
			q8 = n1*q8
			paths.append(3)
		else:
			x = n1+9
			q8 = q8-x
			q8 = q8/n1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))