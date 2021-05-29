import numpy as np 

def function(x):

	l4 = x
	z7 = 6
	paths = []
	try:
		if l4 <= 9:
			z7 = z7*z7
			paths.append(1)
		else:
			l4 = 2*3
			z7 = 5*3
			paths.append(2)
		if l4 >= 2:
			z7 = 7-l4
			x = z7/3
			z7 = 8*l4
			paths.append(3)
		else:
			z7 = z7-l4
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))