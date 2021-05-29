import numpy as np 

def function(x):

	o3 = 4
	z1 = x
	paths = []
	try:
		if x > 4:
			z1 = z1+o3
			paths.append(1)
		else:
			o3 = o3-x
			x = x/5
			z1 = o3-x
			paths.append(2)
		if o3 < 8:
			x = 6/x
			o3 = 2+o3
			o3 = 4/x
			paths.append(3)
		else:
			o3 = 4+o3
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		z1 = z1**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))