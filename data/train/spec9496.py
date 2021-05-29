import numpy as np 

def function(x):

	z0 = x
	t7 = 9
	paths = []
	try:
		if t7 >= 1:
			x = z0-7
			t7 = 8-t7
			paths.append(1)
		else:
			z0 = z0*0
			t7 = 6*t7
			x = 6/x
			paths.append(2)
		if x <= 0:
			x = x/1
			z0 = z0+5
			paths.append(3)
		else:
			t7 = 4*t7
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		z0 = z0**0.5
		return z0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))