import numpy as np 

def function(x):

	z2 = 0
	a2 = x
	paths = []
	try:
		if x < 8:
			z2 = z2/5
			x = x/1
			z2 = z2-5
			paths.append(1)
		else:
			x = 8-0
			paths.append(2)
		if a2 > 9:
			a2 = a2-a2
			z2 = z2*1
			z2 = 4/3
			paths.append(3)
		else:
			a2 = z2*6
			z2 = 5+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z2 = x**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))