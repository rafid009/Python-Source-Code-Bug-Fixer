import numpy as np 

def function(x):

	z5 = x
	o6 = x
	paths = []
	try:
		if x > 2:
			z5 = x/z5
			z5 = z5-z5
			paths.append(1)
		else:
			x = x*o6
			x = x-9
			o6 = x*6
			paths.append(2)
		if x >= 5:
			x = 0-x
			x = o6*2
			x = 0-x
			paths.append(3)
		else:
			z5 = z5*9
			o6 = o6+1
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		o6 = z5**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))