import numpy as np 

def function(x):

	q5 = 8
	z4 = 3
	paths = []
	try:
		if z4 < 5:
			z4 = z4*x
			paths.append(1)
		else:
			z4 = z4-3
			z4 = z4+0
			x = 0/3
			paths.append(2)
		if z4 <= 8:
			z4 = z4-2
			paths.append(3)
		else:
			z4 = x*z4
			x = 2+7
			q5 = 0-q5
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))