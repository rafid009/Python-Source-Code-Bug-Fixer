import numpy as np 

def function(x):

	z3 = x
	o8 = 8
	paths = []
	try:
		if o8 >= 3:
			x = 4-x
			z3 = 8*z3
			o8 = x-o8
			paths.append(1)
		else:
			o8 = 7+9
			o8 = 6/7
			x = z3/9
			paths.append(2)
		if x > 1:
			o8 = 1*o8
			z3 = 3-z3
			paths.append(3)
		else:
			z3 = 1/x
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		x = o8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))