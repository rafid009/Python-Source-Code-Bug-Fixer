import numpy as np 

def function(x):

	z6 = 2
	b8 = 3
	paths = []
	try:
		if z6 >= 3:
			b8 = z6/b8
			x = z6+2
			paths.append(1)
		else:
			x = z6*x
			z6 = 5-x
			b8 = 6-b8
			paths.append(2)
		if x > 9:
			x = x-5
			x = x*5
			x = 5-z6
			paths.append(3)
		else:
			x = 8-b8
			z6 = 3+z6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		b8 = z6**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))