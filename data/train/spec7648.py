import numpy as np 

def function(x):

	z0 = 3
	l1 = 9
	x = x
	paths = []
	try:
		if l1 >= 6:
			l1 = l1/l1
			z0 = z0-6
			paths.append(1)
		else:
			x = x+5
			l1 = l1/l1
			x = x/x
			paths.append(2)
		if l1 <= 5:
			z0 = z0*4
			l1 = 2-6
			paths.append(3)
		else:
			l1 = 8-x
			z0 = z0*1
			l1 = l1-l1
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