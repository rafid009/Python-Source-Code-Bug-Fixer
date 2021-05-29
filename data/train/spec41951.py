import numpy as np 

def function(x):

	z0 = x
	f7 = 8
	paths = []
	try:
		if f7 < 1:
			x = x*x
			z0 = x+x
			paths.append(1)
		else:
			f7 = f7+3
			paths.append(2)
		if z0 > 8:
			z0 = 1/5
			paths.append(3)
		else:
			f7 = 5-1
			f7 = 5*x
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))