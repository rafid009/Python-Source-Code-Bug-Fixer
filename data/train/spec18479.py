import numpy as np 

def function(x):

	z6 = 3
	o6 = 8
	paths = []
	try:
		if o6 < 8:
			z6 = z6-0
			paths.append(1)
		else:
			z6 = 1/8
			paths.append(2)
		if x >= 3:
			o6 = 1-x
			z6 = z6/o6
			x = 1*z6
			paths.append(3)
		else:
			x = o6*4
			z6 = 5+z6
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))