import numpy as np 

def function(x):

	z5 = x
	b8 = 3
	paths = []
	try:
		if b8 > 3:
			z5 = z5-7
			b8 = b8*6
			paths.append(1)
		else:
			b8 = b8-3
			x = x/4
			paths.append(2)
		if z5 > 1:
			b8 = 0*b8
			paths.append(3)
		else:
			x = z5/6
			x = 7*x
			x = 1*x
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))