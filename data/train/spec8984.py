import numpy as np 

def function(x):

	x8 = 4
	z2 = x
	paths = []
	try:
		if x > 2:
			z2 = z2+8
			z2 = z2-8
			paths.append(1)
		else:
			x = 9+x
			x = x-6
			x8 = 8-x8
			paths.append(2)
		if z2 <= 2:
			x = z2-4
			paths.append(3)
		else:
			x = 6-7
			x = z2/2
			x8 = z2+0
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		x = z2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))