import numpy as np 

def function(x):

	z1 = 5
	b6 = x
	x = 5
	paths = []
	try:
		if b6 > 0:
			z1 = z1+7
			b6 = x-z1
			b6 = 3*b6
			paths.append(1)
		else:
			x = x/z1
			x = x+x
			x = x-x
			paths.append(2)
		if b6 <= 0:
			z1 = z1-5
			paths.append(3)
		else:
			z1 = z1/x
			b6 = 2*b6
			b6 = b6*1
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		z1 = b6**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))