import numpy as np 

def function(x):

	x7 = x
	q1 = 7
	paths = []
	try:
		if q1 >= 0:
			x7 = x7/2
			q1 = q1/7
			paths.append(1)
		else:
			x7 = 1-6
			x7 = 6*x7
			paths.append(2)
		if q1 <= 1:
			x = x*4
			paths.append(3)
		else:
			q1 = q1+7
			x7 = q1+6
			x = 1+6
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))