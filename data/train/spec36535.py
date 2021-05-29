import numpy as np 

def function(x):

	l2 = x
	z5 = x
	paths = []
	try:
		if x < 3:
			l2 = 9/x
			paths.append(1)
		else:
			x = 9/l2
			z5 = x+9
			l2 = l2-6
			paths.append(2)
		if l2 >= 6:
			l2 = l2/z5
			l2 = l2+1
			paths.append(3)
		else:
			l2 = 5-z5
			l2 = 5*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))