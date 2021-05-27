import numpy as np 

def function(x):

	v5 = x
	z4 = 0
	paths = []
	try:
		if x >= 3:
			z4 = z4*2
			v5 = z4+v5
			x = 4/x
			paths.append(1)
		else:
			z4 = z4+6
			v5 = 8*v5
			paths.append(2)
		if v5 < 2:
			z4 = 7+4
			z4 = x/8
			paths.append(3)
		else:
			z4 = z4/7
			z4 = x+5
			z4 = x+8
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))