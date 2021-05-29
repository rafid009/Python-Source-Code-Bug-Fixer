import numpy as np 

def function(x):

	i2 = x
	z1 = 1
	paths = []
	try:
		if x <= 2:
			z1 = 4*z1
			paths.append(1)
		else:
			z1 = z1+3
			paths.append(2)
		if i2 < 4:
			z1 = 9/z1
			i2 = 1/1
			paths.append(3)
		else:
			i2 = 3-x
			i2 = i2-4
			x = 3/i2
			paths.append(4)
		paths.append(5)
		assert i2 >= 0
		i2 = i2**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))