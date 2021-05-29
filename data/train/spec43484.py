import numpy as np 

def function(x):

	f7 = x
	z0 = 1
	x = 0
	paths = []
	try:
		if x < 9:
			x = x*x
			paths.append(1)
		else:
			z0 = z0+0
			f7 = 5*x
			paths.append(2)
		if f7 >= 0:
			f7 = 9-f7
			x = 1-f7
			paths.append(3)
		else:
			x = f7+x
			z0 = 0-8
			f7 = f7*f7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))