import numpy as np 

def function(x):

	z1 = x
	v3 = 2
	paths = []
	try:
		if z1 > 0:
			z1 = z1+4
			paths.append(1)
		else:
			x = z1*3
			v3 = 2/v3
			paths.append(2)
		if v3 >= 7:
			z1 = z1-z1
			v3 = 7*9
			paths.append(3)
		else:
			z1 = 8*z1
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))