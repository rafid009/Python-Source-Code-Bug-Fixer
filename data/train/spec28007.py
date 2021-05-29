import numpy as np 

def function(x):

	q2 = 6
	z6 = x
	paths = []
	try:
		if z6 >= 3:
			x = x/1
			z6 = 7*z6
			z6 = z6*z6
			paths.append(1)
		else:
			q2 = 2+q2
			paths.append(2)
		if x < 2:
			z6 = z6-x
			paths.append(3)
		else:
			z6 = 0-1
			x = 4-8
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		q2 = z6**0.5
		return q2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))