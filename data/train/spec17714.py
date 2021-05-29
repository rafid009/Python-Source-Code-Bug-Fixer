import numpy as np 

def function(x):

	z9 = 1
	n2 = x
	paths = []
	try:
		if n2 < 4:
			z9 = z9+z9
			paths.append(1)
		else:
			n2 = 8/z9
			paths.append(2)
		if x >= 2:
			x = z9/x
			z9 = z9*6
			x = x*3
			paths.append(3)
		else:
			x = x+8
			z9 = 7+7
			n2 = n2/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))