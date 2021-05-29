import numpy as np 

def function(x):

	f0 = x
	z5 = x
	paths = []
	try:
		if f0 > 4:
			z5 = z5+z5
			z5 = 3*z5
			x = f0-6
			paths.append(1)
		else:
			z5 = z5-z5
			f0 = f0/f0
			paths.append(2)
		if z5 <= 6:
			z5 = f0-5
			f0 = f0*2
			f0 = 7*4
			paths.append(3)
		else:
			f0 = f0+z5
			z5 = 3/x
			z5 = z5*x
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))