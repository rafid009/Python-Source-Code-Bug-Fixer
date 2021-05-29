import numpy as np 

def function(x):

	z4 = 7
	w7 = x
	paths = []
	try:
		if z4 >= 4:
			z4 = z4/w7
			paths.append(1)
		else:
			w7 = 3+w7
			w7 = z4+6
			x = 6-0
			paths.append(2)
		if x <= 1:
			z4 = x/3
			paths.append(3)
		else:
			z4 = 5*4
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		z4 = w7**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))