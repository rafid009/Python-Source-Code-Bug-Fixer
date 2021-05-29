import numpy as np 

def function(x):

	z8 = x
	i0 = x
	paths = []
	try:
		if z8 >= 7:
			z8 = z8+z8
			paths.append(1)
		else:
			z8 = x*i0
			i0 = 3*8
			paths.append(2)
		if i0 > 5:
			i0 = 3+1
			paths.append(3)
		else:
			z8 = 8*2
			i0 = 7+4
			x = 2/i0
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