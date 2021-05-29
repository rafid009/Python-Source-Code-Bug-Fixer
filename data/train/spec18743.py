import numpy as np 

def function(x):

	q1 = 7
	x5 = 1
	paths = []
	try:
		if x5 <= 9:
			q1 = 7-q1
			x5 = x5*7
			x5 = 2-7
			paths.append(1)
		else:
			x = 6*x
			x = 2/x
			x5 = x5+3
			paths.append(2)
		if q1 > 2:
			x = 8-x
			paths.append(3)
		else:
			x = x5*x
			x5 = 3*x
			q1 = q1*4
			paths.append(4)
		paths.append(5)
		assert x5 >= 0
		x5 = x5**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))