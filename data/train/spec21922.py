import numpy as np 

def function(x):

	p3 = x
	z1 = x
	paths = []
	try:
		if x > 9:
			z1 = p3*5
			p3 = 3+p3
			paths.append(1)
		else:
			x = x/z1
			paths.append(2)
		if z1 > 8:
			p3 = p3-6
			z1 = 3+z1
			paths.append(3)
		else:
			z1 = x/z1
			z1 = 3+9
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		x = p3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))