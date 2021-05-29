import numpy as np 

def function(x):

	z1 = 5
	t4 = x
	paths = []
	try:
		if x <= 4:
			t4 = t4*3
			t4 = 5*t4
			t4 = 8-t4
			paths.append(1)
		else:
			z1 = z1*9
			t4 = z1*7
			paths.append(2)
		if x < 3:
			z1 = z1*x
			x = 7-8
			z1 = z1*5
			paths.append(3)
		else:
			t4 = 6+8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z1 = x**0.5
		return z1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))