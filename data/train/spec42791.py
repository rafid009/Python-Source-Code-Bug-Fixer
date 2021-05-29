import numpy as np 

def function(x):

	z6 = 4
	o6 = 4
	paths = []
	try:
		if x <= 1:
			o6 = 1/o6
			paths.append(1)
		else:
			o6 = o6/o6
			z6 = o6-z6
			x = 2-x
			paths.append(2)
		if o6 >= 6:
			o6 = o6*3
			x = x-0
			paths.append(3)
		else:
			o6 = o6/z6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))