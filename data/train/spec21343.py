import numpy as np 

def function(x):

	z5 = x
	p2 = x
	x = 5
	paths = []
	try:
		if p2 <= 6:
			z5 = z5-1
			x = p2/x
			z5 = 0-z5
			paths.append(1)
		else:
			x = 9*p2
			x = 5+x
			p2 = p2+z5
			paths.append(2)
		if x < 0:
			x = z5*3
			paths.append(3)
		else:
			z5 = 1+z5
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		p2 = p2**0.5
		return p2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))