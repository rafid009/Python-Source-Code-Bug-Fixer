import numpy as np 

def function(x):

	z0 = x
	r1 = 1
	paths = []
	try:
		if z0 >= 2:
			z0 = 0+4
			paths.append(1)
		else:
			z0 = 2*3
			paths.append(2)
		if x > 4:
			r1 = 0/7
			z0 = z0+3
			z0 = z0-9
			paths.append(3)
		else:
			r1 = x/9
			paths.append(4)
		paths.append(5)
		assert r1 >= 0
		r1 = r1**0.5
		return r1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))