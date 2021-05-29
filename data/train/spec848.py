import numpy as np 

def function(x):

	b3 = x
	z7 = x
	x = 4
	paths = []
	try:
		if x <= 8:
			b3 = b3-1
			b3 = 9+2
			x = x/1
			paths.append(1)
		else:
			b3 = x+x
			z7 = 7+z7
			b3 = 4+2
			paths.append(2)
		if z7 >= 0:
			b3 = b3*b3
			z7 = z7-7
			z7 = 6-z7
			paths.append(3)
		else:
			x = x+2
			b3 = b3+z7
			x = x+z7
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		z7 = z7**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))