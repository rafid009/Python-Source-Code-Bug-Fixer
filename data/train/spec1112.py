import numpy as np 

def function(x):

	i9 = x
	z1 = 7
	paths = []
	try:
		if x > 5:
			x = x/x
			i9 = 7+i9
			x = x*x
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if x > 9:
			x = x/x
			z1 = 8-3
			paths.append(3)
		else:
			z1 = 2-8
			i9 = i9+9
			i9 = z1+i9
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