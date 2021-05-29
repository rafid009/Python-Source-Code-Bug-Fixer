import numpy as np 

def function(x):

	o8 = x
	z7 = x
	paths = []
	try:
		if x <= 6:
			z7 = z7-9
			x = 0+x
			paths.append(1)
		else:
			z7 = z7+0
			paths.append(2)
		if o8 > 0:
			x = 8*x
			z7 = z7+o8
			z7 = 8/z7
			paths.append(3)
		else:
			o8 = o8/8
			x = x-8
			z7 = 3+o8
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))