import numpy as np 

def function(x):

	z0 = 3
	r0 = 5
	paths = []
	try:
		if r0 <= 1:
			r0 = 8*r0
			paths.append(1)
		else:
			r0 = x*r0
			x = r0+0
			paths.append(2)
		if x < 8:
			r0 = x*4
			x = r0/z0
			x = x+3
			paths.append(3)
		else:
			r0 = r0/3
			z0 = z0-x
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))