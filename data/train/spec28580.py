import numpy as np 

def function(x):

	o8 = 5
	z5 = 5
	paths = []
	try:
		if o8 <= 4:
			x = x*o8
			paths.append(1)
		else:
			z5 = 5/z5
			paths.append(2)
		if x > 6:
			x = 3-x
			paths.append(3)
		else:
			o8 = o8+x
			o8 = 7+x
			o8 = z5*o8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z5 = x**0.5
		return z5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))