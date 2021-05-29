import numpy as np 

def function(x):

	q3 = 3
	z7 = 2
	paths = []
	try:
		if x < 2:
			q3 = q3*4
			z7 = 7*z7
			paths.append(1)
		else:
			x = z7+9
			paths.append(2)
		if x >= 9:
			z7 = 3/q3
			z7 = 4+z7
			q3 = 1*q3
			paths.append(3)
		else:
			q3 = x*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))