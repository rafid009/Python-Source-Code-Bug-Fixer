import numpy as np 

def function(x):

	o3 = x
	z5 = 6
	paths = []
	try:
		if x > 9:
			z5 = z5/x
			paths.append(1)
		else:
			o3 = 9*3
			o3 = 5*z5
			paths.append(2)
		if o3 >= 7:
			o3 = 4/7
			z5 = 1+z5
			x = x*7
			paths.append(3)
		else:
			o3 = 5*o3
			x = x*8
			x = o3/z5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))