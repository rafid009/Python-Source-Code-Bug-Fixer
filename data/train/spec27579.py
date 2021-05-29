import numpy as np 

def function(x):

	z1 = x
	x1 = 5
	paths = []
	try:
		if z1 < 0:
			x1 = 6/x1
			x = x+1
			paths.append(1)
		else:
			z1 = z1+z1
			z1 = z1*8
			paths.append(2)
		if x > 4:
			z1 = x/6
			paths.append(3)
		else:
			z1 = x1+x
			x = z1+x1
			x = x*9
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