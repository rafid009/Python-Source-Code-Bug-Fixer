import numpy as np 

def function(x):

	z1 = x
	z2 = x
	paths = []
	try:
		if x < 5:
			z1 = z2/7
			z1 = z1-z2
			z1 = z1-4
			paths.append(1)
		else:
			x = x*3
			z1 = x*3
			z2 = z2*3
			paths.append(2)
		if z2 <= 3:
			z2 = x/z2
			paths.append(3)
		else:
			z1 = z2*1
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