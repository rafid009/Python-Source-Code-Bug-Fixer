import numpy as np 

def function(x):

	z4 = 4
	v6 = 5
	paths = []
	try:
		if z4 <= 8:
			v6 = 8/v6
			x = x-0
			paths.append(1)
		else:
			v6 = v6/v6
			z4 = z4+v6
			paths.append(2)
		if x > 9:
			z4 = v6-4
			v6 = 4*v6
			v6 = 3-0
			paths.append(3)
		else:
			x = x-9
			x = v6+4
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))