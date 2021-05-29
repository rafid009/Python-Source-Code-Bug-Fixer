import numpy as np 

def function(x):

	z2 = x
	d5 = x
	paths = []
	try:
		if d5 <= 1:
			d5 = d5-2
			paths.append(1)
		else:
			z2 = z2/4
			z2 = z2/1
			paths.append(2)
		if z2 >= 2:
			z2 = z2*5
			paths.append(3)
		else:
			d5 = 0-5
			x = 1/9
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