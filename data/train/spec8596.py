import numpy as np 

def function(x):

	t9 = x
	z7 = x
	paths = []
	try:
		if z7 >= 4:
			z7 = 4-2
			x = 2*6
			x = 8-x
			paths.append(1)
		else:
			x = x-5
			paths.append(2)
		if x <= 4:
			z7 = 2*8
			t9 = t9+9
			t9 = 9+t9
			paths.append(3)
		else:
			x = 4+4
			z7 = 6/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))