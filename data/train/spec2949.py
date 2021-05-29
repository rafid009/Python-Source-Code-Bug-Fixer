import numpy as np 

def function(x):

	i2 = x
	z9 = 6
	paths = []
	try:
		if i2 >= 6:
			x = 4*3
			z9 = z9*x
			paths.append(1)
		else:
			i2 = 2+2
			paths.append(2)
		if z9 < 7:
			z9 = z9-4
			i2 = 4-x
			paths.append(3)
		else:
			x = x/i2
			x = 7*x
			i2 = i2-2
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		z9 = i2**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))