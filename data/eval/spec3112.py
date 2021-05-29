import numpy as np 

def function(x):

	o4 = x
	z4 = 3
	paths = []
	try:
		if o4 > 5:
			o4 = o4/8
			x = x-z4
			paths.append(1)
		else:
			o4 = x+6
			o4 = 7*6
			paths.append(2)
		if x > 7:
			z4 = x+o4
			x = 9-8
			paths.append(3)
		else:
			o4 = o4+2
			o4 = o4*x
			x = x/4
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		x = o4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))