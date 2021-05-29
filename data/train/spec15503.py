import numpy as np 

def function(x):

	o3 = x
	z7 = x
	paths = []
	try:
		if o3 <= 3:
			x = 9*x
			x = 9-0
			paths.append(1)
		else:
			x = 2-6
			o3 = 2-6
			x = x+o3
			paths.append(2)
		if o3 <= 6:
			o3 = o3-8
			z7 = z7+5
			z7 = 3/z7
			paths.append(3)
		else:
			x = o3/x
			x = 3/x
			o3 = o3/z7
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		z7 = o3**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))