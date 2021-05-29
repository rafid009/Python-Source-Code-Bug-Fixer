import numpy as np 

def function(x):

	p6 = 9
	z4 = 9
	paths = []
	try:
		if p6 <= 0:
			x = 9-x
			z4 = 7*5
			z4 = z4*8
			paths.append(1)
		else:
			p6 = p6+8
			p6 = p6*p6
			p6 = p6-z4
			paths.append(2)
		if p6 < 6:
			p6 = z4-p6
			z4 = 3+z4
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))