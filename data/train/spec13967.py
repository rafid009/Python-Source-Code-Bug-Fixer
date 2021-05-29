import numpy as np 

def function(x):

	z4 = x
	o2 = 8
	paths = []
	try:
		if x <= 3:
			o2 = o2*6
			o2 = x/z4
			paths.append(1)
		else:
			o2 = x+x
			o2 = o2-z4
			paths.append(2)
		if z4 < 4:
			o2 = o2-7
			z4 = x-z4
			paths.append(3)
		else:
			z4 = 0+z4
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		z4 = o2**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))