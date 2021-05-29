import numpy as np 

def function(x):

	o4 = x
	z4 = 2
	paths = []
	try:
		if o4 <= 7:
			x = x+0
			x = o4/x
			paths.append(1)
		else:
			z4 = z4*5
			o4 = 4*o4
			x = 9+x
			paths.append(2)
		if x > 6:
			o4 = 3/o4
			x = x+4
			paths.append(3)
		else:
			o4 = o4-6
			o4 = o4*7
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		z4 = o4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))