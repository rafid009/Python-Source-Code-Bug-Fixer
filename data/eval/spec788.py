import numpy as np 

def function(x):

	j2 = 6
	z5 = x
	paths = []
	try:
		if x < 4:
			x = x/j2
			x = x+9
			z5 = z5/3
			paths.append(1)
		else:
			x = 9+x
			x = x-3
			paths.append(2)
		if x >= 8:
			z5 = 9-2
			z5 = 8/4
			x = x+x
			paths.append(3)
		else:
			x = 2+6
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))