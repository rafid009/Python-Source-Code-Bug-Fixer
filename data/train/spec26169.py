import numpy as np 

def function(x):

	o8 = x
	z7 = 7
	paths = []
	try:
		if o8 < 5:
			o8 = o8+0
			z7 = x/9
			paths.append(1)
		else:
			z7 = z7*5
			paths.append(2)
		if z7 > 0:
			o8 = o8/o8
			o8 = 6-z7
			o8 = 1+x
			paths.append(3)
		else:
			o8 = 1-o8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))