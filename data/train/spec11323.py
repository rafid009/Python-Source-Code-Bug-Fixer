import numpy as np 

def function(x):

	b5 = 5
	z8 = 5
	paths = []
	try:
		if b5 <= 2:
			z8 = z8/9
			x = 4/5
			z8 = z8*4
			paths.append(1)
		else:
			b5 = 8/b5
			z8 = 9-z8
			z8 = 9*x
			paths.append(2)
		if b5 >= 2:
			z8 = 9*b5
			paths.append(3)
		else:
			x = 2/x
			b5 = 0*b5
			b5 = b5-x
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))