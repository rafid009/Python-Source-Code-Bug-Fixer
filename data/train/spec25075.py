import numpy as np 

def function(x):

	o9 = 8
	z9 = x
	paths = []
	try:
		if z9 > 1:
			x = z9*z9
			x = x+x
			paths.append(1)
		else:
			o9 = z9/o9
			paths.append(2)
		if z9 > 4:
			z9 = o9-z9
			o9 = 7/o9
			x = o9-8
			paths.append(3)
		else:
			z9 = z9/o9
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		z9 = o9**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))