import numpy as np 

def function(x):

	l7 = 7
	z7 = x
	paths = []
	try:
		if x >= 9:
			z7 = 4*z7
			paths.append(1)
		else:
			z7 = 6*9
			z7 = z7*7
			paths.append(2)
		if l7 <= 0:
			z7 = z7/z7
			x = x*8
			paths.append(3)
		else:
			l7 = l7/1
			l7 = l7/x
			x = l7-x
			paths.append(4)
		paths.append(5)
		assert l7 >= 0
		l7 = l7**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))