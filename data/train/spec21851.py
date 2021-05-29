import numpy as np 

def function(x):

	k2 = x
	z2 = 7
	paths = []
	try:
		if k2 < 8:
			x = x-9
			x = x*8
			k2 = 3-k2
			paths.append(1)
		else:
			z2 = x/8
			paths.append(2)
		if k2 < 6:
			z2 = z2-0
			x = x+x
			paths.append(3)
		else:
			z2 = z2*1
			z2 = k2-8
			k2 = k2-k2
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		k2 = z2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))