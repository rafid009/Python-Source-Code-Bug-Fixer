import numpy as np 

def function(x):

	z2 = x
	e5 = 5
	paths = []
	try:
		if e5 > 0:
			x = x-z2
			x = x+1
			paths.append(1)
		else:
			z2 = 3+e5
			z2 = z2+x
			paths.append(2)
		if x >= 9:
			z2 = z2-x
			e5 = e5/3
			z2 = z2-8
			paths.append(3)
		else:
			z2 = z2*8
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))