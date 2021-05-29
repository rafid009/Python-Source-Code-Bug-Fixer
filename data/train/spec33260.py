import numpy as np 

def function(x):

	l4 = x
	z2 = 8
	paths = []
	try:
		if x < 6:
			l4 = x+3
			l4 = l4-6
			paths.append(1)
		else:
			x = z2-x
			paths.append(2)
		if x > 9:
			x = 3+4
			paths.append(3)
		else:
			x = l4/x
			z2 = z2/x
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		x = l4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))