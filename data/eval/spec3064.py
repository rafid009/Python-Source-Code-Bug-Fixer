import numpy as np 

def function(x):

	z9 = x
	o8 = x
	paths = []
	try:
		if z9 >= 2:
			o8 = 3+o8
			x = 3+x
			z9 = 5+x
			paths.append(1)
		else:
			x = o8-7
			x = 4+x
			x = x/5
			paths.append(2)
		if o8 <= 3:
			x = 8-6
			x = 0*x
			paths.append(3)
		else:
			o8 = z9*9
			o8 = 3-o8
			x = x/o8
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