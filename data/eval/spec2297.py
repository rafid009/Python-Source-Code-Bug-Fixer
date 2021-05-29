import numpy as np 

def function(x):

	z6 = 7
	p6 = x
	paths = []
	try:
		if x < 3:
			z6 = 5/z6
			z6 = 7/7
			paths.append(1)
		else:
			x = z6/7
			z6 = 6*z6
			x = x-x
			paths.append(2)
		if x <= 3:
			p6 = p6+p6
			p6 = p6/1
			paths.append(3)
		else:
			z6 = x/z6
			p6 = 1+9
			x = z6+x
			paths.append(4)
		paths.append(5)
		assert p6 >= 0
		z6 = p6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))