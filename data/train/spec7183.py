import numpy as np 

def function(x):

	f2 = x
	z4 = 4
	paths = []
	try:
		if x < 9:
			x = x*6
			paths.append(1)
		else:
			f2 = f2-z4
			paths.append(2)
		if x > 5:
			f2 = f2-1
			f2 = f2*f2
			z4 = z4+1
			paths.append(3)
		else:
			z4 = x/2
			z4 = z4/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))