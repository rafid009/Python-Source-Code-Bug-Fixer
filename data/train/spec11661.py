import numpy as np 

def function(x):

	p7 = x
	z4 = x
	paths = []
	try:
		if p7 > 7:
			z4 = p7-6
			x = 2*p7
			paths.append(1)
		else:
			x = x+3
			x = 2-3
			paths.append(2)
		if x < 6:
			z4 = 7+z4
			x = x*8
			paths.append(3)
		else:
			z4 = z4+z4
			z4 = z4/z4
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))