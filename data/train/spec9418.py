import numpy as np 

def function(x):

	u1 = x
	z2 = 6
	x = x
	paths = []
	try:
		if x <= 8:
			x = 6-u1
			paths.append(1)
		else:
			x = 4*z2
			paths.append(2)
		if x >= 7:
			u1 = 4+2
			paths.append(3)
		else:
			z2 = z2-u1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u1 = x**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))