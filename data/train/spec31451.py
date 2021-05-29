import numpy as np 

def function(x):

	r4 = 1
	z6 = x
	paths = []
	try:
		if x > 6:
			r4 = 1-9
			z6 = 9*r4
			paths.append(1)
		else:
			z6 = 2-9
			paths.append(2)
		if x < 1:
			z6 = 7+r4
			paths.append(3)
		else:
			z6 = 8+z6
			r4 = r4/6
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		x = r4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))