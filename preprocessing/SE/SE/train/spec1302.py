import numpy as np 

def function(x):

	z1 = 6
	t4 = x
	paths = []
	try:
		if x < 4:
			x = 7/t4
			paths.append(1)
		else:
			t4 = t4+4
			x = z1/x
			z1 = z1/1
			paths.append(2)
		if z1 >= 3:
			z1 = 2*z1
			z1 = 8-t4
			t4 = 7/x
			paths.append(3)
		else:
			t4 = t4-t4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))