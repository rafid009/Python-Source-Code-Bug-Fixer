import numpy as np 

def function(x):

	q1 = x
	z3 = 7
	paths = []
	try:
		if z3 >= 5:
			x = x-9
			z3 = 3*q1
			paths.append(1)
		else:
			q1 = q1*6
			paths.append(2)
		if x > 0:
			q1 = q1-1
			z3 = 6-z3
			q1 = z3*z3
			paths.append(3)
		else:
			q1 = 6/q1
			paths.append(4)
		paths.append(5)
		assert q1 >= 0
		q1 = q1**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))