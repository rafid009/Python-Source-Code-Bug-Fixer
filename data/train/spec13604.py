import numpy as np 

def function(x):

	n5 = x
	z4 = x
	x = 8
	paths = []
	try:
		if x <= 4:
			x = 9-x
			paths.append(1)
		else:
			x = x+x
			n5 = 3-n5
			paths.append(2)
		if z4 >= 7:
			x = n5-6
			x = x-4
			paths.append(3)
		else:
			z4 = 4+z4
			x = x*z4
			z4 = z4+7
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		n5 = z4**0.5
		return n5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))