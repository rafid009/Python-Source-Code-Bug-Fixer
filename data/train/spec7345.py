import numpy as np 

def function(x):

	b4 = x
	z4 = x
	paths = []
	try:
		if z4 < 3:
			x = 5*x
			z4 = 7+z4
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if b4 >= 0:
			x = z4-x
			z4 = 8*9
			paths.append(3)
		else:
			z4 = b4/2
			x = x*3
			x = 6/5
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		z4 = b4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))