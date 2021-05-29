import numpy as np 

def function(x):

	z9 = x
	j0 = 1
	paths = []
	try:
		if z9 >= 3:
			x = z9+x
			paths.append(1)
		else:
			z9 = 5/5
			x = x*3
			paths.append(2)
		if j0 <= 7:
			j0 = x+3
			z9 = 7/4
			paths.append(3)
		else:
			z9 = z9-2
			j0 = x*j0
			j0 = 2-j0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))