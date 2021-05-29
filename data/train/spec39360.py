import numpy as np 

def function(x):

	l1 = x
	z6 = x
	paths = []
	try:
		if z6 >= 6:
			z6 = z6+z6
			l1 = l1/4
			paths.append(1)
		else:
			x = x+8
			paths.append(2)
		if z6 < 3:
			l1 = l1-7
			z6 = z6+l1
			l1 = l1+9
			paths.append(3)
		else:
			z6 = l1-z6
			z6 = z6*9
			x = x*5
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))