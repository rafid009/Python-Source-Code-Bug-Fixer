import numpy as np 

def function(x):

	z4 = x
	r3 = x
	x = 9
	paths = []
	try:
		if x <= 8:
			r3 = r3-r3
			paths.append(1)
		else:
			r3 = 4/3
			x = x+z4
			z4 = z4*5
			paths.append(2)
		if r3 < 8:
			z4 = z4-6
			paths.append(3)
		else:
			z4 = z4*r3
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		r3 = z4**0.5
		return r3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))