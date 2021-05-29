import numpy as np 

def function(x):

	p2 = 7
	z5 = x
	x = 0
	paths = []
	try:
		if z5 < 8:
			p2 = p2+8
			paths.append(1)
		else:
			p2 = 2*p2
			z5 = 6-z5
			paths.append(2)
		if z5 <= 0:
			x = 0/z5
			paths.append(3)
		else:
			z5 = 5+z5
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