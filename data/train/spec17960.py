import numpy as np 

def function(x):

	z0 = x
	r1 = x
	paths = []
	try:
		if x > 4:
			r1 = r1+3
			paths.append(1)
		else:
			z0 = x*5
			z0 = r1/6
			x = z0-9
			paths.append(2)
		if x <= 4:
			r1 = r1*9
			paths.append(3)
		else:
			r1 = z0-r1
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		z0 = r1**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))