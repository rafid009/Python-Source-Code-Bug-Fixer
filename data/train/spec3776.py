import numpy as np 

def function(x):

	z1 = x
	j9 = 0
	paths = []
	try:
		if z1 > 6:
			x = x/4
			j9 = j9+6
			paths.append(1)
		else:
			x = 5*x
			j9 = 9-1
			paths.append(2)
		if x <= 8:
			z1 = 1-z1
			j9 = j9-x
			z1 = 5/7
			paths.append(3)
		else:
			z1 = 4-z1
			j9 = j9+1
			x = x-z1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))