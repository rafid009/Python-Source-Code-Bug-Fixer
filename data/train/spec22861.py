import numpy as np 

def function(x):

	z9 = x
	i0 = 1
	paths = []
	try:
		if x >= 4:
			i0 = i0+5
			z9 = z9-2
			paths.append(1)
		else:
			x = x*3
			z9 = z9-i0
			i0 = i0/2
			paths.append(2)
		if x >= 9:
			x = i0+x
			z9 = 5+9
			z9 = 9-z9
			paths.append(3)
		else:
			i0 = 2*i0
			x = x+x
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