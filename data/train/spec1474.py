import numpy as np 

def function(x):

	q5 = x
	z0 = x
	paths = []
	try:
		if x <= 5:
			q5 = 5/z0
			paths.append(1)
		else:
			z0 = 5*x
			paths.append(2)
		if x < 1:
			q5 = 9/q5
			q5 = q5-1
			paths.append(3)
		else:
			z0 = 0/x
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))