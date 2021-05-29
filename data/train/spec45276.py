import numpy as np 

def function(x):

	z4 = 5
	z1 = x
	paths = []
	try:
		if z1 <= 3:
			z4 = x+8
			z1 = 9/z1
			paths.append(1)
		else:
			z4 = z1*5
			paths.append(2)
		if x < 8:
			z1 = z1+4
			z4 = 3*z4
			paths.append(3)
		else:
			z1 = x*z1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z4 = z1**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))