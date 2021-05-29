import numpy as np 

def function(x):

	z1 = x
	t8 = x
	paths = []
	try:
		if x <= 4:
			x = 4-x
			x = x-t8
			paths.append(1)
		else:
			z1 = 3*z1
			z1 = 0-7
			paths.append(2)
		if t8 < 6:
			t8 = z1+t8
			t8 = 2/t8
			paths.append(3)
		else:
			z1 = 0*z1
			x = 0/t8
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