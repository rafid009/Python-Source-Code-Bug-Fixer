import numpy as np 

def function(x):

	z2 = x
	o3 = x
	paths = []
	try:
		if o3 > 3:
			z2 = z2+8
			paths.append(1)
		else:
			z2 = x-4
			paths.append(2)
		if o3 > 1:
			z2 = z2/8
			x = 0*o3
			o3 = 7-o3
			paths.append(3)
		else:
			z2 = 2/z2
			x = 5/x
			z2 = 4*6
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		o3 = z2**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))