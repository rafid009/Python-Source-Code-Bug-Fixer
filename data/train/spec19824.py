import numpy as np 

def function(x):

	o3 = x
	z1 = x
	x = 0
	paths = []
	try:
		if x > 2:
			z1 = z1/6
			paths.append(1)
		else:
			z1 = z1*3
			x = z1-x
			paths.append(2)
		if z1 > 8:
			z1 = z1*1
			z1 = 7-z1
			paths.append(3)
		else:
			x = 6/o3
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		o3 = z1**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))