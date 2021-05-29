import numpy as np 

def function(x):

	z6 = 5
	f3 = x
	paths = []
	try:
		if z6 <= 0:
			z6 = 8-z6
			z6 = z6-x
			paths.append(1)
		else:
			f3 = x+z6
			f3 = f3/3
			paths.append(2)
		if z6 > 5:
			z6 = 8+z6
			x = 8+x
			x = f3*x
			paths.append(3)
		else:
			x = 1*x
			z6 = z6-9
			x = 8*x
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))