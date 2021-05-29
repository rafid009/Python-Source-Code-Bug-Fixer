import numpy as np 

def function(x):

	o2 = x
	z1 = x
	paths = []
	try:
		if o2 >= 5:
			x = z1-x
			paths.append(1)
		else:
			z1 = z1-3
			z1 = 3/z1
			x = 3/x
			paths.append(2)
		if z1 <= 3:
			z1 = z1/3
			x = x/8
			o2 = o2-5
			paths.append(3)
		else:
			o2 = o2/8
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))