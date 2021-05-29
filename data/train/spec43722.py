import numpy as np 

def function(x):

	q1 = x
	z3 = 1
	x = 4
	paths = []
	try:
		if q1 < 6:
			z3 = 6*x
			paths.append(1)
		else:
			x = x+q1
			paths.append(2)
		if q1 <= 1:
			z3 = 4/q1
			paths.append(3)
		else:
			x = q1/x
			q1 = 2*q1
			paths.append(4)
		paths.append(5)
		assert z3 >= 0
		q1 = z3**0.5
		return q1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))