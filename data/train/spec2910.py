import numpy as np 

def function(x):

	j8 = 4
	z1 = x
	paths = []
	try:
		if x > 6:
			z1 = z1/6
			paths.append(1)
		else:
			j8 = j8+x
			x = 0-x
			x = x/z1
			paths.append(2)
		if j8 > 2:
			j8 = 1*j8
			z1 = 5*j8
			x = 7-x
			paths.append(3)
		else:
			j8 = j8*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))