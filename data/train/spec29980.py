import numpy as np 

def function(x):

	k2 = x
	z6 = 2
	x = x
	paths = []
	try:
		if k2 < 6:
			k2 = k2*3
			paths.append(1)
		else:
			z6 = k2/8
			paths.append(2)
		if z6 > 2:
			k2 = x/5
			z6 = z6+k2
			k2 = 6/9
			paths.append(3)
		else:
			z6 = k2/z6
			x = x-6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		k2 = z6**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))