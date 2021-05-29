import numpy as np 

def function(x):

	k3 = x
	z2 = 0
	paths = []
	try:
		if z2 < 0:
			z2 = x+9
			x = x+x
			z2 = z2*k3
			paths.append(1)
		else:
			z2 = 1-z2
			paths.append(2)
		if x > 7:
			x = 4+6
			z2 = x-7
			k3 = 4+k3
			paths.append(3)
		else:
			k3 = k3+7
			z2 = z2/1
			z2 = 2-6
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