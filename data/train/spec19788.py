import numpy as np 

def function(x):

	z9 = x
	v9 = 5
	paths = []
	try:
		if v9 >= 3:
			x = x-0
			paths.append(1)
		else:
			z9 = 5+x
			v9 = v9/x
			v9 = v9/2
			paths.append(2)
		if z9 >= 1:
			v9 = v9-v9
			v9 = x+v9
			paths.append(3)
		else:
			x = 6-x
			z9 = z9*z9
			x = 5-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z9 = x**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))