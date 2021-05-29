import numpy as np 

def function(x):

	p2 = x
	z7 = x
	x = 2
	paths = []
	try:
		if z7 <= 8:
			z7 = z7-3
			paths.append(1)
		else:
			z7 = z7-6
			x = 3*x
			paths.append(2)
		if x >= 6:
			x = 4+x
			p2 = 7+p2
			x = 7+8
			paths.append(3)
		else:
			z7 = z7+3
			z7 = x*z7
			p2 = x-z7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x = z7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))