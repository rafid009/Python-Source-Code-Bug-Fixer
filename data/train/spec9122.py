import numpy as np 

def function(x):

	i2 = 6
	z7 = 8
	paths = []
	try:
		if z7 < 5:
			i2 = 5/i2
			z7 = z7/z7
			i2 = 2*4
			paths.append(1)
		else:
			x = x+x
			z7 = 0/1
			paths.append(2)
		if z7 < 5:
			i2 = 1/4
			i2 = 6/9
			paths.append(3)
		else:
			x = x+i2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i2 = x**0.5
		return i2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))