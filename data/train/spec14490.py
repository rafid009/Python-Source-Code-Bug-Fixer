import numpy as np 

def function(x):

	z4 = x
	k7 = x
	paths = []
	try:
		if x < 9:
			x = x+6
			z4 = 2-z4
			paths.append(1)
		else:
			z4 = z4/8
			x = x/4
			paths.append(2)
		if k7 > 5:
			x = 2/x
			z4 = z4-2
			x = k7-6
			paths.append(3)
		else:
			k7 = 0*k7
			z4 = 3/z4
			z4 = z4*3
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		k7 = z4**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))