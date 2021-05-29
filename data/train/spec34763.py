import numpy as np 

def function(x):

	z6 = x
	b6 = 6
	paths = []
	try:
		if z6 < 6:
			b6 = b6+x
			paths.append(1)
		else:
			x = x/z6
			x = 4-b6
			x = 4*x
			paths.append(2)
		if b6 > 5:
			z6 = b6*x
			paths.append(3)
		else:
			z6 = b6/b6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))