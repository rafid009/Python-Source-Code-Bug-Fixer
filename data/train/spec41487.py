import numpy as np 

def function(x):

	z2 = x
	o4 = x
	paths = []
	try:
		if z2 < 9:
			o4 = o4+o4
			z2 = x/5
			o4 = o4-x
			paths.append(1)
		else:
			z2 = 6-4
			paths.append(2)
		if o4 < 9:
			o4 = z2/1
			paths.append(3)
		else:
			o4 = o4/9
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		x = z2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))