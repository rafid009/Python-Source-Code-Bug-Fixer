import numpy as np 

def function(x):

	z7 = x
	q1 = 3
	paths = []
	try:
		if z7 >= 8:
			z7 = x*q1
			x = q1/4
			paths.append(1)
		else:
			q1 = q1-x
			paths.append(2)
		if z7 < 4:
			q1 = q1-3
			paths.append(3)
		else:
			x = z7+x
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x = z7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))