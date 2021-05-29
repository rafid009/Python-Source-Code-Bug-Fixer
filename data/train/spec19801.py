import numpy as np 

def function(x):

	b7 = 3
	z6 = 6
	paths = []
	try:
		if b7 < 8:
			x = x/9
			b7 = 1-x
			paths.append(1)
		else:
			z6 = z6*8
			paths.append(2)
		if z6 >= 7:
			b7 = x*x
			paths.append(3)
		else:
			b7 = 6+b7
			b7 = b7-8
			b7 = b7/6
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