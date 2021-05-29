import numpy as np 

def function(x):

	z1 = 3
	w5 = 8
	paths = []
	try:
		if w5 >= 3:
			w5 = 2/w5
			w5 = w5-4
			x = 0-x
			paths.append(1)
		else:
			w5 = w5*w5
			z1 = z1+z1
			paths.append(2)
		if w5 >= 7:
			w5 = w5+x
			z1 = 1+9
			z1 = x-z1
			paths.append(3)
		else:
			z1 = 5+z1
			x = 2-5
			paths.append(4)
		paths.append(5)
		assert w5 >= 0
		x = w5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))