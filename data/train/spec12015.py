import numpy as np 

def function(x):

	z8 = x
	p3 = 6
	paths = []
	try:
		if x < 7:
			x = 2-z8
			paths.append(1)
		else:
			z8 = z8/1
			paths.append(2)
		if x > 2:
			z8 = 3-z8
			p3 = p3/6
			p3 = p3-x
			paths.append(3)
		else:
			x = 1-1
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		p3 = p3**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))