import numpy as np 

def function(x):

	q2 = 5
	z1 = x
	paths = []
	try:
		if x <= 2:
			z1 = x+6
			x = q2+x
			paths.append(1)
		else:
			z1 = 6-z1
			x = q2-0
			z1 = z1/1
			paths.append(2)
		if q2 <= 2:
			q2 = q2/8
			paths.append(3)
		else:
			z1 = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))