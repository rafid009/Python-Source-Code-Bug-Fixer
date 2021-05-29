import numpy as np 

def function(x):

	z1 = 8
	o5 = x
	x = 4
	paths = []
	try:
		if z1 > 9:
			x = 6-8
			paths.append(1)
		else:
			o5 = z1+o5
			paths.append(2)
		if x >= 1:
			z1 = 4-2
			z1 = z1+9
			paths.append(3)
		else:
			x = x-z1
			o5 = x+o5
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		o5 = o5**0.5
		return o5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))