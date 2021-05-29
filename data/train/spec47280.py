import numpy as np 

def function(x):

	q1 = x
	u0 = 5
	paths = []
	try:
		if x > 1:
			u0 = u0-0
			x = q1*x
			paths.append(1)
		else:
			q1 = q1/7
			q1 = q1+3
			q1 = x-q1
			paths.append(2)
		if x <= 6:
			x = x-0
			paths.append(3)
		else:
			q1 = u0/q1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q1 = x**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))