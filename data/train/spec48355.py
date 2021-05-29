import numpy as np 

def function(x):

	n6 = 4
	z1 = 1
	paths = []
	try:
		if n6 >= 5:
			n6 = 3/n6
			paths.append(1)
		else:
			z1 = z1/n6
			paths.append(2)
		if x < 1:
			x = x+3
			z1 = z1+z1
			paths.append(3)
		else:
			x = 4+0
			x = 7+x
			n6 = n6-n6
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