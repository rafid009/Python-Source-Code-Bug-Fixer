import numpy as np 

def function(x):

	z6 = 6
	l9 = x
	paths = []
	try:
		if l9 <= 6:
			l9 = 2*l9
			paths.append(1)
		else:
			z6 = z6-x
			paths.append(2)
		if l9 > 8:
			z6 = z6*l9
			paths.append(3)
		else:
			l9 = 4-8
			l9 = l9*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))