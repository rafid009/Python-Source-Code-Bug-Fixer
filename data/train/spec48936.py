import numpy as np 

def function(x):

	j0 = 8
	q1 = x
	paths = []
	try:
		if j0 > 0:
			q1 = q1/4
			paths.append(1)
		else:
			j0 = 6/2
			x = q1-x
			x = 7/4
			paths.append(2)
		if x <= 6:
			q1 = x*q1
			q1 = q1*3
			paths.append(3)
		else:
			j0 = j0-3
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