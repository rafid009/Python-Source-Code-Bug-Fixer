import numpy as np 

def function(x):

	z7 = x
	n4 = x
	paths = []
	try:
		if z7 < 6:
			z7 = z7-x
			paths.append(1)
		else:
			z7 = z7+z7
			paths.append(2)
		if x > 7:
			x = x-9
			x = x/2
			paths.append(3)
		else:
			z7 = n4/4
			x = z7+x
			x = 6-1
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