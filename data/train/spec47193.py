import numpy as np 

def function(x):

	k5 = 2
	z2 = x
	paths = []
	try:
		if k5 <= 8:
			z2 = z2/x
			k5 = k5-4
			x = x-5
			paths.append(1)
		else:
			k5 = z2+z2
			z2 = k5+1
			paths.append(2)
		if z2 <= 6:
			z2 = k5/9
			z2 = 5-z2
			paths.append(3)
		else:
			k5 = 1+z2
			paths.append(4)
		paths.append(5)
		assert k5 >= 0
		k5 = k5**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))