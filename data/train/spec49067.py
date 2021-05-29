import numpy as np 

def function(x):

	x9 = x
	q1 = x
	paths = []
	try:
		if q1 >= 4:
			q1 = 9/x9
			x9 = x9/6
			paths.append(1)
		else:
			x9 = 6*x9
			paths.append(2)
		if x9 >= 2:
			x9 = 9*x9
			q1 = q1+7
			paths.append(3)
		else:
			q1 = q1*q1
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		x9 = x9**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))