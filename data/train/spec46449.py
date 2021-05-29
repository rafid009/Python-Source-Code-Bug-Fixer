import numpy as np 

def function(x):

	z2 = x
	o4 = 3
	paths = []
	try:
		if x > 3:
			o4 = 4-o4
			o4 = o4+o4
			x = x/9
			paths.append(1)
		else:
			z2 = z2-o4
			paths.append(2)
		if z2 <= 9:
			z2 = z2/z2
			z2 = z2+9
			z2 = x-9
			paths.append(3)
		else:
			o4 = o4-7
			o4 = z2/o4
			x = x+z2
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		z2 = z2**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))