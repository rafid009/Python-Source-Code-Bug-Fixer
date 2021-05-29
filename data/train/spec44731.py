import numpy as np 

def function(x):

	j6 = x
	z0 = x
	paths = []
	try:
		if z0 > 3:
			x = x+x
			paths.append(1)
		else:
			j6 = j6+8
			paths.append(2)
		if z0 > 6:
			z0 = z0-j6
			x = x-j6
			paths.append(3)
		else:
			j6 = 3-6
			z0 = x*8
			x = z0*1
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))