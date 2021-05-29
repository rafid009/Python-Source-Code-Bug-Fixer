import numpy as np 

def function(x):

	f7 = x
	z7 = x
	x = 9
	paths = []
	try:
		if z7 < 9:
			z7 = z7/x
			paths.append(1)
		else:
			x = z7+x
			z7 = z7-3
			paths.append(2)
		if x >= 9:
			x = 0/6
			f7 = 9-f7
			paths.append(3)
		else:
			z7 = 7/2
			z7 = f7*8
			z7 = z7*2
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