import numpy as np 

def function(x):

	b0 = x
	z0 = x
	paths = []
	try:
		if x > 2:
			z0 = z0/b0
			paths.append(1)
		else:
			x = 7+x
			z0 = z0*8
			z0 = 9/5
			paths.append(2)
		if b0 <= 9:
			z0 = z0-5
			paths.append(3)
		else:
			b0 = b0+b0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))