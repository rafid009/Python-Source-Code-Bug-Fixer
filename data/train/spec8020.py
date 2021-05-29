import numpy as np 

def function(x):

	z0 = 2
	i8 = 5
	paths = []
	try:
		if i8 <= 7:
			z0 = 1-4
			z0 = 6-7
			paths.append(1)
		else:
			z0 = x-z0
			paths.append(2)
		if x <= 2:
			x = x-5
			i8 = x+i8
			paths.append(3)
		else:
			x = x*0
			i8 = i8*i8
			i8 = i8/i8
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