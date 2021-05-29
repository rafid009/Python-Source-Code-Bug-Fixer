import numpy as np 

def function(x):

	l1 = x
	z0 = x
	paths = []
	try:
		if z0 < 7:
			x = x*x
			z0 = 0/x
			x = x-z0
			paths.append(1)
		else:
			z0 = 8+3
			paths.append(2)
		if x > 4:
			x = 6-x
			paths.append(3)
		else:
			l1 = 4/l1
			z0 = 9*z0
			paths.append(4)
		paths.append(5)
		assert l1 >= 0
		l1 = l1**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))