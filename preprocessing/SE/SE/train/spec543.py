import numpy as np 

def function(x):

	n7 = x
	z4 = x
	paths = []
	try:
		if x < 4:
			x = 1*4
			x = 9-x
			x = x-x
			paths.append(1)
		else:
			n7 = n7+8
			paths.append(2)
		if n7 > 4:
			z4 = z4/z4
			z4 = 8*5
			n7 = 1/n7
			paths.append(3)
		else:
			n7 = 4*n7
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))