import numpy as np 

def function(x):

	z6 = 7
	l5 = x
	paths = []
	try:
		if z6 >= 9:
			z6 = z6*1
			l5 = x*8
			x = 3+2
			paths.append(1)
		else:
			z6 = 8+7
			x = x*4
			paths.append(2)
		if l5 < 9:
			z6 = 8/z6
			z6 = z6*7
			z6 = 3*8
			paths.append(3)
		else:
			x = 6+2
			l5 = z6/l5
			z6 = 1*z6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))