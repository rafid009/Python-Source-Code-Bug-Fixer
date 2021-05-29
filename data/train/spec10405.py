import numpy as np 

def function(x):

	v4 = x
	z4 = x
	paths = []
	try:
		if x < 3:
			x = x*v4
			z4 = z4/z4
			x = 9-0
			paths.append(1)
		else:
			v4 = 5-z4
			x = x*v4
			v4 = v4/2
			paths.append(2)
		if z4 > 1:
			z4 = 5+v4
			z4 = 8-z4
			z4 = 1+z4
			paths.append(3)
		else:
			z4 = z4/x
			z4 = 8*z4
			x = 7/5
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))