import numpy as np 

def function(x):

	r1 = 0
	z1 = 9
	paths = []
	try:
		if x < 7:
			r1 = x+r1
			z1 = z1+1
			z1 = 0+z1
			paths.append(1)
		else:
			x = 4+3
			x = x-9
			r1 = z1/8
			paths.append(2)
		if z1 > 0:
			z1 = r1+9
			x = 5+z1
			z1 = z1-z1
			paths.append(3)
		else:
			r1 = r1*7
			x = x-5
			z1 = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))