import numpy as np 

def function(x):

	z4 = x
	b9 = x
	paths = []
	try:
		if x <= 1:
			b9 = b9+x
			paths.append(1)
		else:
			z4 = 9-1
			z4 = 5*6
			x = x-z4
			paths.append(2)
		if b9 < 8:
			b9 = z4/1
			z4 = z4-5
			paths.append(3)
		else:
			z4 = 6/z4
			z4 = 7+z4
			b9 = b9*b9
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))