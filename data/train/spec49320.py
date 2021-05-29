import numpy as np 

def function(x):

	o3 = x
	z1 = x
	x = x
	paths = []
	try:
		if o3 < 2:
			x = x+x
			o3 = z1*7
			o3 = o3*7
			paths.append(1)
		else:
			z1 = 8*6
			z1 = z1*2
			paths.append(2)
		if z1 <= 2:
			x = 5/o3
			x = 0+x
			x = x*5
			paths.append(3)
		else:
			o3 = o3+2
			z1 = z1/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))