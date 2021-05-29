import numpy as np 

def function(x):

	p7 = x
	z8 = x
	paths = []
	try:
		if z8 < 5:
			z8 = 6-z8
			paths.append(1)
		else:
			x = x/3
			paths.append(2)
		if z8 <= 6:
			z8 = z8-z8
			p7 = p7+p7
			p7 = p7/1
			paths.append(3)
		else:
			x = 5+x
			z8 = z8-z8
			paths.append(4)
		paths.append(5)
		assert p7 >= 0
		x = p7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))