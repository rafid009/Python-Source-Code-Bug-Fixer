import numpy as np 

def function(x):

	z5 = x
	i8 = x
	paths = []
	try:
		if z5 >= 7:
			x = i8-x
			x = 9/6
			z5 = z5*i8
			paths.append(1)
		else:
			x = x-z5
			z5 = z5*9
			x = 4*z5
			paths.append(2)
		if x < 1:
			x = 1*2
			paths.append(3)
		else:
			z5 = z5*2
			paths.append(4)
		paths.append(5)
		assert i8 >= 0
		x = i8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))