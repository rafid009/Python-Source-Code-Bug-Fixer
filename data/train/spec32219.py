import numpy as np 

def function(x):

	i9 = 5
	z1 = 0
	paths = []
	try:
		if x <= 3:
			x = 6/x
			paths.append(1)
		else:
			x = 0+x
			x = x-8
			paths.append(2)
		if i9 <= 3:
			z1 = 2/z1
			z1 = 2+x
			x = x-5
			paths.append(3)
		else:
			z1 = z1-3
			z1 = z1+1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))