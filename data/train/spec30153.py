import numpy as np 

def function(x):

	z6 = x
	p8 = 5
	paths = []
	try:
		if z6 > 5:
			p8 = 7*4
			paths.append(1)
		else:
			z6 = 9-z6
			paths.append(2)
		if x > 2:
			x = x/9
			x = p8*x
			z6 = z6*7
			paths.append(3)
		else:
			z6 = x*4
			p8 = p8+7
			p8 = 3*p8
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))