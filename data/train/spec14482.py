import numpy as np 

def function(x):

	z2 = 7
	l2 = x
	paths = []
	try:
		if z2 <= 5:
			x = 5*x
			paths.append(1)
		else:
			x = x+z2
			l2 = l2/x
			paths.append(2)
		if z2 <= 5:
			z2 = z2/l2
			paths.append(3)
		else:
			x = x-7
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		l2 = l2**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))