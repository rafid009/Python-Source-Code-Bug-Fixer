import numpy as np 

def function(x):

	z7 = 2
	b5 = 1
	paths = []
	try:
		if z7 > 8:
			z7 = 2+6
			z7 = z7/x
			x = x+0
			paths.append(1)
		else:
			z7 = z7/4
			b5 = b5+x
			x = 6*x
			paths.append(2)
		if b5 < 0:
			b5 = b5/x
			b5 = b5/8
			paths.append(3)
		else:
			z7 = z7*x
			b5 = 8/8
			x = b5+b5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))