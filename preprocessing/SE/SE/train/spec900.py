import numpy as np 

def function(x):

	o5 = x
	z6 = 4
	paths = []
	try:
		if x <= 0:
			z6 = 8-o5
			o5 = o5+x
			paths.append(1)
		else:
			x = 4/x
			x = 5+o5
			x = 6*x
			paths.append(2)
		if x > 5:
			o5 = o5*z6
			o5 = o5-z6
			paths.append(3)
		else:
			x = x+3
			o5 = x/o5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o5 = x**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))