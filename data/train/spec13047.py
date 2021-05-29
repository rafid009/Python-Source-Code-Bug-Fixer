import numpy as np 

def function(x):

	z5 = x
	o1 = 0
	paths = []
	try:
		if x > 7:
			o1 = o1+z5
			o1 = 0*o1
			paths.append(1)
		else:
			o1 = o1-7
			paths.append(2)
		if x > 7:
			x = x*9
			paths.append(3)
		else:
			x = x-3
			x = o1+z5
			z5 = x/1
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