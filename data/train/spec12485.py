import numpy as np 

def function(x):

	z9 = 8
	q2 = 1
	paths = []
	try:
		if x > 3:
			q2 = 7/q2
			q2 = q2*4
			paths.append(1)
		else:
			z9 = z9*7
			q2 = 8+q2
			paths.append(2)
		if q2 > 2:
			q2 = x*q2
			paths.append(3)
		else:
			x = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q2 = x**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))