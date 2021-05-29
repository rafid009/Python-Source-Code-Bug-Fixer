import numpy as np 

def function(x):

	o4 = 9
	z9 = 0
	paths = []
	try:
		if o4 <= 5:
			z9 = 8-5
			paths.append(1)
		else:
			x = x*7
			paths.append(2)
		if x > 4:
			x = o4+o4
			x = o4*o4
			paths.append(3)
		else:
			o4 = o4+x
			x = 2*4
			o4 = 9*o4
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		z9 = o4**0.5
		return z9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))