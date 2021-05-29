import numpy as np 

def function(x):

	x4 = 3
	z1 = x
	x = x
	paths = []
	try:
		if z1 > 8:
			x = x*4
			paths.append(1)
		else:
			x4 = x4/3
			paths.append(2)
		if z1 > 2:
			x = x+0
			z1 = x*9
			x4 = z1/2
			paths.append(3)
		else:
			x = x-8
			x = x+2
			x = 3-2
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))