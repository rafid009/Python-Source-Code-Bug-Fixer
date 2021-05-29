import numpy as np 

def function(x):

	z6 = 0
	o1 = x
	paths = []
	try:
		if o1 < 1:
			z6 = z6-3
			o1 = o1/7
			paths.append(1)
		else:
			x = 9/x
			paths.append(2)
		if z6 > 3:
			o1 = 4-z6
			paths.append(3)
		else:
			x = x/2
			paths.append(4)
		paths.append(5)
		assert o1 >= 0
		o1 = o1**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))