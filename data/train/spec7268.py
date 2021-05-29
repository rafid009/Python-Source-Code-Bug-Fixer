import numpy as np 

def function(x):

	z0 = 8
	l0 = x
	paths = []
	try:
		if x < 4:
			l0 = 5/l0
			l0 = 1+l0
			x = x*0
			paths.append(1)
		else:
			z0 = z0*z0
			z0 = z0/4
			paths.append(2)
		if l0 <= 2:
			z0 = l0-0
			l0 = l0+l0
			x = x*0
			paths.append(3)
		else:
			z0 = 2-z0
			l0 = 3/l0
			x = x-x
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))