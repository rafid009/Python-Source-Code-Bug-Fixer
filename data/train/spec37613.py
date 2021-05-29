import numpy as np 

def function(x):

	i2 = x
	z1 = x
	x = 2
	paths = []
	try:
		if z1 < 6:
			i2 = x-i2
			i2 = i2-5
			i2 = i2+i2
			paths.append(1)
		else:
			z1 = x*x
			i2 = 1+i2
			paths.append(2)
		if x < 2:
			z1 = 4+z1
			x = x/7
			i2 = i2+4
			paths.append(3)
		else:
			i2 = 4+i2
			z1 = x/x
			z1 = 4-6
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		x = i2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))