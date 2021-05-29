import numpy as np 

def function(x):

	f6 = x
	z5 = x
	paths = []
	try:
		if f6 < 1:
			z5 = 8+3
			x = x-1
			f6 = f6+9
			paths.append(1)
		else:
			z5 = 6+z5
			z5 = 3-z5
			paths.append(2)
		if f6 >= 0:
			f6 = 7-6
			f6 = f6/2
			z5 = 4/z5
			paths.append(3)
		else:
			x = 7/1
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