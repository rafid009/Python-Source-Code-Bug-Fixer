import numpy as np 

def function(x):

	z7 = 7
	o5 = x
	x = x
	paths = []
	try:
		if o5 >= 3:
			z7 = z7+3
			o5 = z7-5
			o5 = 7/o5
			paths.append(1)
		else:
			o5 = o5/5
			paths.append(2)
		if z7 >= 2:
			z7 = 6+x
			z7 = 0*z7
			o5 = o5+4
			paths.append(3)
		else:
			o5 = 6/z7
			o5 = x+4
			x = 1*x
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